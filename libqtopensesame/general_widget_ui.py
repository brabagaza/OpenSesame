# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/general_widget.ui'
#
# Created: Sun Oct  9 13:29:05 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(839, 749)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.combobox_start = QtGui.QComboBox(self.widget)
        self.combobox_start.setObjectName(_fromUtf8("combobox_start"))
        self.gridLayout.addWidget(self.combobox_start, 0, 1, 1, 5)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.spinbox_width = QtGui.QSpinBox(self.widget)
        self.spinbox_width.setMinimum(1)
        self.spinbox_width.setMaximum(10000)
        self.spinbox_width.setObjectName(_fromUtf8("spinbox_width"))
        self.gridLayout.addWidget(self.spinbox_width, 3, 1, 1, 1)
        self.spinbox_height = QtGui.QSpinBox(self.widget)
        self.spinbox_height.setMinimum(1)
        self.spinbox_height.setMaximum(10000)
        self.spinbox_height.setObjectName(_fromUtf8("spinbox_height"))
        self.gridLayout.addWidget(self.spinbox_height, 3, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.spinbox_compensation = QtGui.QSpinBox(self.widget)
        self.spinbox_compensation.setMinimum(-100)
        self.spinbox_compensation.setMaximum(100)
        self.spinbox_compensation.setObjectName(_fromUtf8("spinbox_compensation"))
        self.gridLayout.addWidget(self.spinbox_compensation, 4, 1, 1, 3)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 4, 1, 1)
        self.edit_background = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_background.sizePolicy().hasHeightForWidth())
        self.edit_background.setSizePolicy(sizePolicy)
        self.edit_background.setObjectName(_fromUtf8("edit_background"))
        self.gridLayout.addWidget(self.edit_background, 4, 5, 1, 1)
        self.edit_foreground = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_foreground.sizePolicy().hasHeightForWidth())
        self.edit_foreground.setSizePolicy(sizePolicy)
        self.edit_foreground.setObjectName(_fromUtf8("edit_foreground"))
        self.gridLayout.addWidget(self.edit_foreground, 3, 5, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 4, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.combobox_backend = QtGui.QComboBox(self.widget)
        self.combobox_backend.setObjectName(_fromUtf8("combobox_backend"))
        self.gridLayout.addWidget(self.combobox_backend, 5, 1, 1, 5)
        self.verticalLayout.addWidget(self.widget)
        self.group_backend_settings = QtGui.QGroupBox(Form)
        self.group_backend_settings.setCheckable(True)
        self.group_backend_settings.setChecked(False)
        self.group_backend_settings.setObjectName(_fromUtf8("group_backend_settings"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.group_backend_settings)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.scrollarea_backend_settings = QtGui.QScrollArea(self.group_backend_settings)
        self.scrollarea_backend_settings.setWidgetResizable(True)
        self.scrollarea_backend_settings.setObjectName(_fromUtf8("scrollarea_backend_settings"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 819, 262))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.group_canvas = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.group_canvas.setObjectName(_fromUtf8("group_canvas"))
        self.layout_canvas = QtGui.QVBoxLayout(self.group_canvas)
        self.layout_canvas.setContentsMargins(0, -1, 0, 0)
        self.layout_canvas.setObjectName(_fromUtf8("layout_canvas"))
        self.label_canvas = QtGui.QLabel(self.group_canvas)
        self.label_canvas.setObjectName(_fromUtf8("label_canvas"))
        self.layout_canvas.addWidget(self.label_canvas)
        self.verticalLayout_7.addWidget(self.group_canvas)
        self.group_keyboard = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.group_keyboard.setObjectName(_fromUtf8("group_keyboard"))
        self.layout_keyboard = QtGui.QVBoxLayout(self.group_keyboard)
        self.layout_keyboard.setContentsMargins(0, -1, 0, 0)
        self.layout_keyboard.setObjectName(_fromUtf8("layout_keyboard"))
        self.label_keyboard = QtGui.QLabel(self.group_keyboard)
        self.label_keyboard.setObjectName(_fromUtf8("label_keyboard"))
        self.layout_keyboard.addWidget(self.label_keyboard)
        self.verticalLayout_7.addWidget(self.group_keyboard)
        self.group_mouse = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.group_mouse.setObjectName(_fromUtf8("group_mouse"))
        self.layout_mouse = QtGui.QVBoxLayout(self.group_mouse)
        self.layout_mouse.setContentsMargins(0, -1, 0, 0)
        self.layout_mouse.setObjectName(_fromUtf8("layout_mouse"))
        self.label_mouse = QtGui.QLabel(self.group_mouse)
        self.label_mouse.setObjectName(_fromUtf8("label_mouse"))
        self.layout_mouse.addWidget(self.label_mouse)
        self.verticalLayout_7.addWidget(self.group_mouse)
        self.group_sampler = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.group_sampler.setObjectName(_fromUtf8("group_sampler"))
        self.layout_sampler = QtGui.QVBoxLayout(self.group_sampler)
        self.layout_sampler.setContentsMargins(0, -1, 0, 0)
        self.layout_sampler.setObjectName(_fromUtf8("layout_sampler"))
        self.label_sampler = QtGui.QLabel(self.group_sampler)
        self.label_sampler.setObjectName(_fromUtf8("label_sampler"))
        self.layout_sampler.addWidget(self.label_sampler)
        self.verticalLayout_7.addWidget(self.group_sampler)
        self.group_synth = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.group_synth.setObjectName(_fromUtf8("group_synth"))
        self.layout_synth = QtGui.QVBoxLayout(self.group_synth)
        self.layout_synth.setContentsMargins(0, -1, 0, 0)
        self.layout_synth.setObjectName(_fromUtf8("layout_synth"))
        self.label_synth = QtGui.QLabel(self.group_synth)
        self.label_synth.setObjectName(_fromUtf8("label_synth"))
        self.layout_synth.addWidget(self.label_synth)
        self.verticalLayout_7.addWidget(self.group_synth)
        self.scrollarea_backend_settings.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollarea_backend_settings)
        self.verticalLayout.addWidget(self.group_backend_settings)
        self.group_script = QtGui.QGroupBox(Form)
        self.group_script.setCheckable(True)
        self.group_script.setChecked(False)
        self.group_script.setObjectName(_fromUtf8("group_script"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.group_script)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout.addWidget(self.group_script)
        self.spacer = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacer.sizePolicy().hasHeightForWidth())
        self.spacer.setSizePolicy(sizePolicy)
        self.spacer.setObjectName(_fromUtf8("spacer"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.spacer)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget_2 = QtGui.QWidget(self.spacer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        spacerItem = QtGui.QSpacerItem(20, 193, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.label_opensesame = QtGui.QLabel(self.spacer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_opensesame.sizePolicy().hasHeightForWidth())
        self.label_opensesame.setSizePolicy(sizePolicy)
        self.label_opensesame.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_opensesame.setObjectName(_fromUtf8("label_opensesame"))
        self.verticalLayout_2.addWidget(self.label_opensesame)
        self.verticalLayout.addWidget(self.spacer)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Entry point</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">first item to run</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_start.setToolTip(QtGui.QApplication.translate("Form", "This is item (typically a sequence) is the starting point for your experiment.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Display resolution</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">in pixels (width x height)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_width.setToolTip(QtGui.QApplication.translate("Form", "The display resolution (width) in pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_width.setSuffix(QtGui.QApplication.translate("Form", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_height.setToolTip(QtGui.QApplication.translate("Form", "The display resolution (height) in pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_height.setSuffix(QtGui.QApplication.translate("Form", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Timing compensation</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">in milliseconds</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_compensation.setToolTip(QtGui.QApplication.translate("Form", "Automatic timing compensation. Positive values will decrease durations, negative values will increase durations (of sketchpads etc.)", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_compensation.setSuffix(QtGui.QApplication.translate("Form", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Background color</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">E.g., &quot;black&quot; or &quot;#000000&quot;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_background.setToolTip(QtGui.QApplication.translate("Form", "Default background color", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_foreground.setToolTip(QtGui.QApplication.translate("Form", "Default foreground color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Foreground color</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">E.g., &quot;white&quot; or &quot;#FFFFFF&quot;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Back-end</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">The layer controlling display, sound and input</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.group_backend_settings.setTitle(QtGui.QApplication.translate("Form", "Show back-end settings and info", None, QtGui.QApplication.UnicodeUTF8))
        self.group_canvas.setTitle(QtGui.QApplication.translate("Form", "Canvas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_canvas.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.group_keyboard.setTitle(QtGui.QApplication.translate("Form", "Keyboard", None, QtGui.QApplication.UnicodeUTF8))
        self.label_keyboard.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.group_mouse.setTitle(QtGui.QApplication.translate("Form", "Mouse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_mouse.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.group_sampler.setTitle(QtGui.QApplication.translate("Form", "Sampler", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sampler.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.group_synth.setTitle(QtGui.QApplication.translate("Form", "Synth", None, QtGui.QApplication.UnicodeUTF8))
        self.label_synth.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.group_script.setTitle(QtGui.QApplication.translate("Form", "Show script editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_opensesame.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">OpenSesame [version]</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">[codename]</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright Sebastiaan Mathôt (2010-2011)</p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.cogsci.nl/opensesame\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.cogsci.nl/opensesame</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
