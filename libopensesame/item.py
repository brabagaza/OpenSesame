#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

import openexp.mouse
import openexp.keyboard
from libopensesame import exceptions, debug, regexp
import string
import shlex
import os
import sys
import pygame

class item:

	"""
	item is an abstract class that serves as the basis for all OpenSesame items,
	such as sketchpad, keyboard_response, experiment, etc.
	"""

	def __init__(self, name, experiment, string=None):

		"""
		Constructor

		Arguments:
		name -- the name of the item
		experiment -- the experiment

		Keyword arguments:
		string -- an item definition string (default = None)
		"""

		self.name = name
		self.experiment = experiment
		self.debug = debug.enabled
		self.count = 0
		self.reserved_words = "run", "prepare", "get", "set", "has"
		self._get_lock = None
		
		if not hasattr(self, "item_type"):
			self.item_type = "item"
		if not hasattr(self, "description"):
			self.description = "Default description"
		if not hasattr(self, "round_decimals"):
			self.round_decimals = 2
		self.variables = {}
		self.comments = []

		if string != None:
			self.from_string(string)			

	def prepare(self):

		"""
		Derived classes should use this function to prepare the item for speedy
		execution during the run phase.

		Returns:
		True on succes, False on failure
		"""

		self.time = self.experiment._time_func
		self.sleep = self.experiment._sleep_func		
		self.experiment.set("count_%s" % self.name, self.count)
		self.count += 1
		return True

	def run(self):

		"""
		Derived classes should use this function to perform the item specific
		function.

		Returns:
		True on succes, False on failure
		"""

		return True

	def parse_variable(self, line):

		"""
		Reads a single variable from a single definition line

		Arguments:
		line -- a single definition line

		Returns:
		True on succes, False on failure
		"""

		# It is a little ugly to call parse_comment() here, but otherwise
		# all from_string() derivatives need to be modified
		if self.parse_comment(line):
			return True

		try:
			l = shlex.split(line.strip())
		except Exception as e:
			raise exceptions.script_error( \
				"Error parsing '%s' in item '%s': %s" % (line, self.name, e))

		if len(l) > 0 and l[0] == "set":
			if len(l) != 3:
				raise exceptions.script_error( \
					"Error parsing variable definition: '%s'" % line)
			else:
				self.set(l[1], l[2])
				return True

		return False

	def parse_comment(self, line):

		"""
		Parses comments from a single definition line, indicated by # // or '

		Arguments:
		line -- a single definition line

		Returns:
		True on succes, False on failure
		"""

		line = line.strip()
		if len(line) > 0 and line[0] == "#":
			self.comments.append(line[1:])
			return True
		elif len(line) > 1 and line[0:2] == "//":
			self.comments.append(line[2:])
			return True
		return False

	def variable_to_string(self, var):

		"""
		Encode a variable into a definition string

		Arguments:
		var -- the variable to encode

		Returns:
		A definition string
		"""

		# Multiline variables are stored as a block
		if type(self.variables[var]) == str and ("\n" in self.variables[var] \
			or "\"" in self.variables[var]):
			s = "__%s__\n" % var
			for l in self.variables[var].split("\n"):
				s += "\t%s\n" % l

			while s[-1] in ("\t", "\n"):
				s = s[:-1]
			s += "\n"

			#if s[-1] != "\n":
			#	s += "\n"
			s += "\t__end__\n"
			return s

		# Regular variables
		else:
			return "set %s \"%s\"\n" % (var, self.variables[var])

	def from_string(self, string):

		"""
		Read the item from a definition string

		Arguments:
		string -- the definition string
		"""

		debug.msg()
		textblock_var = None
		self.variables = {}
		for line in string.split("\n"):				
			line_stripped = line.strip()
			# The end of a textblock
			if line_stripped == "__end__":
				self.set(textblock_var, textblock_val)
				textblock_var = None
			# The beginning of a textblock
			elif line_stripped[:2] == "__" and line_stripped[-2:] == "__":
				textblock_var = line_stripped[2:-2]
				if textblock_var in self.reserved_words:
					textblock_var = "_" + textblock_var
				if textblock_var != "":
					textblock_val = ""
				else:
					textblock_var = None
				# We cannot just strip the multiline code, because that may mess
				# up indentation. So we have to detect if the string is indented
				# based on the opening __varname__ line.
				strip_tab = line[0] == "\t"
			# Collect the contents of a textblock
			elif textblock_var != None:
				if strip_tab:
					textblock_val += line[1:] + "\n"
				else:
					textblock_val += line + "\n"
			# Parse regular variables
			else:
				self.parse_variable(line)
					
	def to_string(self, item_type = None):

		"""
		Encode the item into a definition string

		Keyword arguments:
		item_type -- the type of the item or None for autodetect
					 (default = None)

		Returns:
		The definition string
		"""

		if item_type == None:
			item_type = self.item_type

		s = "define %s %s\n" % (item_type, self.name)
		for comment in self.comments:
			s += "\t# %s\n" % comment.strip()
		for var in self.variables:
			s += "\t" + self.variable_to_string(var)

		return s

	def set(self, var, val):

		"""<DOC>
		Set a variable. Note: if you want to set a variable so that it is
		available in other items as well (notably the logger item, so you can
		log the variable), you need to use the set function from the experiment.
		So, in an inline_script item you would generally set a variable with
		self.experiment.set(), rather than self.set().

		Arguments:
		var -- the name of the variable
		val -- the value
		</DOC>"""

		if regexp.sanitize_var_name.sub('_', var) != var:
			raise exceptions.runtime_error( \
				'"%s" is not a valid variable name. Variable names must consist of alphanumeric characters and underscores, and may not start with a digit.' \
				% var)
						
		val = self.auto_type(val)
		if type(val) == float:
			exec("self.%s = %f" % (var, val))
		elif type(val) == int:
			exec("self.%s = %d" % (var, val))
		else:
			exec("self.%s = \"\"\"%s\"\"\"" % (var, val.replace("\"", "\\\"")))
		self.variables[var] = val

	def unset(self, var):

		"""<DOC>
		Unset (forget) a variable

		Arguments:
		var -- the name of the variable
		</DOC>"""

		if var in self.variables:
			del self.variables[var]
		try:
			exec("del self.%s" % var)
		except:
			pass

	def get(self, var, _eval=True):

		"""<DOC>
		Return the value of a variable. Checks first if the variable exists
		'locally' in the item and, if not, checks if the vaiable exists
		'globally' in the experiment. Raises a runtime_error if the variable
		is not found.

		Arguments:
		var -- the name of the variable
		_eval -- indicates whether the variable should be evaluated, i.e.
				 whether containing variables should be processed (default=True)		

		Returns:
		The value
		</DOC>"""

		# Avoid recursion
		if var == self._get_lock:
			raise exceptions.runtime_error( \
				"Recursion detected! Is variable '%s' defined in terms of itself (e.g., 'var = [var]') in item '%s'" \
				% (var, self.name))
		# Get the variable				
		if hasattr(self, var):
			val = eval("self.%s" % var)
		else:
			try:
				val = eval("self.experiment.%s" % var)
			except:
				raise exceptions.runtime_error( \
					"Variable '%s' is not set in item '%s'.<br /><br />You are trying to use a variable that does not exist. Make sure that you have spelled and capitalized the variable name correctly. You may wish to use the variable inspector (Control + I) to find the intended variable." \
					% (var, self.name))
		if _eval:					
			# Lock to avoid recursion and start evaluating possible variables		
			self._get_lock = var
			val = self.eval_text(val)
			self._get_lock = None
			# Done!
		return val

	def get_check(self, var, default=None, valid=None, _eval=True):

		"""<DOC>
		Similar to get(), but falls back to a default if the variable has not
		been set. It also raises an error if the value is not part of the valid
		list.

		Arguments:
		var -- the name of the variable
		default -- a default 'fallback' value or None for no fallback, in which
				   case an exception is rased if the value does not exist.
		valid -- a list of allowed values (or None for no restrictions). An
				 exception is raised if the value is not an allowed value.
		_eval -- indicates whether the variable should be evaluated, i.e.
				 whether containing variables should be processed (default=True)

		Exceptions:
		Raises a runtime_error if the variable is not defined and there is no
		default value, or if the variable value is not part of the 'valid' list.

		Returns:
		The value
		</DOC>"""

		if default == None:
			val = self.get(var, _eval=_eval)
		elif self.has(var):
			val = self.get(var, _eval=_eval)
		else:
			val = default
		if valid != None and val not in valid:
			raise exceptions.runtime_error( \
				"Variable '%s' is '%s', expecting '%s'" % (var, val, \
				" or ".join(valid)))
		return val

	def has(self, var):

		"""<DOC>
		Checks if a variable exists (either in the item or the experiment).

		Arguments:
		var -- the name of the variable

		Returns:
		True if the variable exists, False if not
		</DOC>"""

		return type(var) == str and (hasattr(self, var) or \
			hasattr(self.experiment, var))

	def get_refs(self, text):

		"""<DOC>
		Returns a list of variables that are referred to by the string. (E.g.,
		'this is a [variable]')

		Arguments:
		text -- a string of text

		Returns:
		A list of variable names or an empty list if the string contains no
		references.
		</DOC>"""

		# If the text is not a string, there cannot be any variables,
		# so return right away
		if type(text) != str:
			return []

		l = []
		s = ""
		start = -1
		while True:
			# Find the start and end of a variable definition
			start = text.find("[", start + 1)
			if start < 0:
				break
			end = text.find("]", start + 1)
			if end < 0:
				raise exceptions.runtime_error( \
					"Missing closing bracket ']' in string '%s', in item '%s'" \
					% (text, self.name))
			var = text[start+1:end]
			l.append(var)
			var = var[end:]
		return l

	def auto_type(self, val):

		"""<DOC>
		Convert a value into the 'best fitting' type that is compatible with the
		value. E.g., auto_type('1') -> int, auto_type('1.2') -> float and
		auto_type('one') -> string. Boolean values are converted to 'yes'/ 'no'.
		

		Arguments:
		val -- a value

		Returns:
		The same value converted to the 'best fitting' type
		</DOC>"""
		
		if type(val) == bool:
			if val:
				return 'yes'
			else:
				return 'no'
		try:
			if int(float(val)) == float(val):
				return int(float(val))
			else:
				return float(val)
		except:
			return str(val)

	def set_item_onset(self, time = None):

		"""
		Set a timestamp for the item's executions

		Keyword arguments:
		time -- the timestamp or None to use the current time (default = None)
		"""

		if time == None:
			time = self.time()
		exec("self.experiment.time_%s = %f" % (self.name, time))

	def dummy(self):

		"""Dummy function"""

		pass

	def eval_text(self, text, round_float=False, soft_ignore=False, quote_str=False):

		"""<DOC>
		Replace variables in the text by the actual values

		Arguments:
		text -- the text to be evaluated

		Keyword arguments:
		round_float -- a boolean indicating whether float values should be
					   rounded to a precision of [round_decimals]
					   (default = False)
		soft_ignore -- a boolean indicating whether missing variables should be
					   ignored, rather than cause an exception (default = False)
		quote_str -- a boolean indicating whether string variables should be
					 quoted (default = False)

		Returns:
		The evaluated string
		</DOC>"""

		# If the text is not a string, there cannot be any variables, so return
		if type(text) not in (str, unicode):
			return self.auto_type(text)
		# Prepare a template for rounding floats
		if round_float:
			float_template = "%%.%sf" % self.get("round_decimals")
		# Find and replace all variables in the text
		while True:		
			m = regexp.find_variable.search(text)
			if m == None:
				break			
			var = m.group(0)[1:-1]
			if not soft_ignore or self.has(var):
				val = self.get(var)
				# Quote strings if necessary
				if type(val) == str and quote_str:
					val = "\'" + val + "\'"
				# Round floats
				if round_float and type(val) == float:
					val = float_template % val					
				text = text.replace(m.group(0), str(val), 1)
		return self.auto_type(text)

	def compile_cond(self, cond, bytecode = True):

		"""
		Create Python code for a given conditional statement

		Arguments:
		cond -- the conditional statement (e.g., '[correct] = 1')

		Keyword arguments:
		bytecode -- a boolean indicating whether the generated code should be
					byte compiled (default = True)

		Returns:
		Python code (possibly byte compiled) that reflects the conditional
		statement
		"""

		src = cond

		operators = "!=", "==", "=", "<", ">", ">=", "<=", "+", "-", "(", ")", \
			"/", "*", "%", "~", "**", "^"
		op_chars = "!", "=", "=", "<", ">", "+", "-", "(", ")", "/", "*", "%", \
			"~", "*", "^"
		whitespace = " ", "\t", "\n"
		keywords = "and", "or", "is", "not", "true", "false"
		capitalize = "true", "false", "none"

		# Try to fix missing spaces
		redo = True
		while redo:
			redo = False
			for i in range(len(cond)):
				if cond[i] in op_chars:
					if i != 0 and cond[i-1] not in op_chars + whitespace:
						cond = cond[:i] + " " + cond[i:]
						redo = True
						break
					if i < len(cond)-1 and cond[i+1] not in op_chars+whitespace:
						cond = cond[:i+1] + " " + cond[i+1:]
						redo = True
						break

		# Rebuild the conditional string
		l = []
		i = 0
		for word in shlex.split(cond):
			if len(word) > 2 and word[0] == "[" and word[-1] == "]":
				l.append("str(self.get(\"%s\"))" % word[1:-1])
			elif word == "=":
				l.append("==")
			elif word.lower() == "always":
				l.append("True")
			elif word.lower() == "never":
				l.append("False")
			elif word.lower() in operators + keywords:
				if word.lower() in capitalize:
					l.append(word.capitalize())
				else:
					l.append(word.lower())
			else:
				# For backwards compatibility, the first word is interpreted as
				# a variable name
				if i == 0:
					l.append("str(self.get(\"%s\"))" % word)
				else:
					l.append("\"%s\"" % word)
			i += 1

		code = " ".join(l)
		if code != "True":
			debug.msg("'%s' => '%s'" % (src, code))
		if not bytecode:
			return code
		try:
			bytecode = compile(code, "<conditional statement>", "eval")
		except:
			raise exceptions.runtime_error( \
				"'%s' is not a valid conditional statement in sequence item '%s'" \
				% (cond, self.name))
		return bytecode

	def var_info(self):

		"""
		Give a list of dictionaries with variable descriptions

		Returns:
		A list of (variable, description) tuples
		"""

		return [ ("time_%s" % self.name, "[Timestamp of last item call]"), \
			("count_%s" % self.name, "[Number of item calls]") ]

	def usanitize(self, s, strict=False):

		"""<DOC>
		Convert all special characters to U+XXXX notation. Note that this
		function can rely on the Qt4 QString class.

		Arguments:
		s -- the string to be santized

		Keyword arguments:
		strict -- if True, special characters are ignored rather than recoded
				  (default = False)

		Returns:
		The sanitized string
		</DOC>"""
		
		if type(s) not in (unicode, str):
			try:
				s = unicode(s)
			except:
				return "Error: Unable to create readable text from string"		
		_s = ''
		for ch in s:
			# Encode non ASCII and slash characters
			if ord(ch) > 127 or ord(ch) == 92:
				if not strict:
					_s += 'U+%.4X' % ord(ch)
			else:
				_s += ch
		return _s.replace(os.linesep, "\n")

	def sanitize(self, s, strict=False, allow_vars=True):

		"""<DOC>
		Remove invalid characters (notably quotes) from the string. This is
		stricter than usanitize(), because it removes also quotes and optionally
		all alphanumeric characters.

		Arguments:
		s -- the string to be sanitized

		Keyword arguments:
		strict -- If True, all but underscores and alphanumeric characters are
				  stripped (default=False)
		allow_vars -- If True, square brackets are not sanitized, so you can use
					  variables (default=True)

		Returns:
		The sanitized string
		</DOC>"""
		
		s = unicode(s)
		if strict:
			if allow_vars:
				return regexp.sanitize_strict_vars.sub('', s)
			return regexp.sanitize_strict_novars.sub('', s)
		return regexp.sanitize_loose.sub('', self.usanitize(s, strict))
		
	def unsanitize(self, s):

		"""<DOC>
		Convert the U+XXXX notation back to actual Unicode encoding

		Arguments:
		s -- the input string

		Returns:
		The restored Unicode string
		</DOC>"""

		s = unicode(s)
		while True:
			m = regexp.unsanitize.search(s)
			if m == None:
				break
			s = s.replace(m.group(0), unichr(int(m.group(1), 16)), 1)
		return s

	def color_check(self, s):

		"""<DOC>
		Checks whether a string is a valid color name

		Arguments:
		s -- the string to check

		Returns:
		True i the string is a color, False otherwise
		</DOC>"""

		try:
			if type(s) == unicode:
				s = str(s)
			pygame.Color(s)
		except Exception as e:
			raise exceptions.script_error( \
				"'%s' is not a valid color. See http://www.w3schools.com/html/html_colornames.asp for an overview of valid color names" \
				% s)

	def sleep(self, ms):

		"""<DOC>
		Sleep for a specified duration

		Arguments:
		ms -- a duration in milliseconds
		</DOC>"""

		# This function is set by item.prepare()
		raise exceptions.openexp_error( \
			"item.sleep(): This function should be set by the canvas backend.")

	def time(self):

		"""<DOC>
		Return current time

		Returns:
		A timestamp of the current time
		</DOC>"""

		# This function is set by item.prepare()
		raise exceptions.openexp_error( \
			"item.time(): This function should be set by the canvas backend.")

	def log(self, msg):

		"""<DOC>
		Write a message to the log file

		msg -- a message
		</DOC>"""

		self.experiment._log.write(u"%s\n" % msg)

	def flush_log(self):

		"""<DOC>
		Force any pending write operations to the log file to be written to disk
		</DOC>"""

		self.experiment._log.flush()
		os.fsync(self.experiment._log)


	
