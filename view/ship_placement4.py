# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ship_placement4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 527)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(34, 61, 400, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_0 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_0.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_0.setSpacing(0)
        self.horizontalLayout_0.setObjectName("horizontalLayout_0")
        self.graphicsView_1 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.horizontalLayout_0.addWidget(self.graphicsView_1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_0.addWidget(self.graphicsView_2)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_0.addWidget(self.graphicsView_3)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.horizontalLayout_0.addWidget(self.graphicsView_4)
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.horizontalLayout_0.addWidget(self.graphicsView_5)
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.horizontalLayout_0.addWidget(self.graphicsView_6)
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.horizontalLayout_0.addWidget(self.graphicsView_7)
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.horizontalLayout_0.addWidget(self.graphicsView_8)
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.horizontalLayout_0.addWidget(self.graphicsView_9)
        self.graphicsView_10 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_10.setObjectName("graphicsView_10")
        self.horizontalLayout_0.addWidget(self.graphicsView_10)
        self.verticalLayout.addLayout(self.horizontalLayout_0)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setSpacing(0)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.graphicsView_11 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_11.setObjectName("graphicsView_11")
        self.horizontalLayout_1.addWidget(self.graphicsView_11)
        self.graphicsView_12 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_12.setObjectName("graphicsView_12")
        self.horizontalLayout_1.addWidget(self.graphicsView_12)
        self.graphicsView_13 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_13.setObjectName("graphicsView_13")
        self.horizontalLayout_1.addWidget(self.graphicsView_13)
        self.graphicsView_14 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_14.setObjectName("graphicsView_14")
        self.horizontalLayout_1.addWidget(self.graphicsView_14)
        self.graphicsView_15 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_15.setObjectName("graphicsView_15")
        self.horizontalLayout_1.addWidget(self.graphicsView_15)
        self.graphicsView_16 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_16.setObjectName("graphicsView_16")
        self.horizontalLayout_1.addWidget(self.graphicsView_16)
        self.graphicsView_17 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_17.setObjectName("graphicsView_17")
        self.horizontalLayout_1.addWidget(self.graphicsView_17)
        self.graphicsView_18 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_18.setObjectName("graphicsView_18")
        self.horizontalLayout_1.addWidget(self.graphicsView_18)
        self.graphicsView_19 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_19.setObjectName("graphicsView_19")
        self.horizontalLayout_1.addWidget(self.graphicsView_19)
        self.graphicsView_20 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_20.setObjectName("graphicsView_20")
        self.horizontalLayout_1.addWidget(self.graphicsView_20)
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView_21 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_21.setObjectName("graphicsView_21")
        self.horizontalLayout_2.addWidget(self.graphicsView_21)
        self.graphicsView_22 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_22.setObjectName("graphicsView_22")
        self.horizontalLayout_2.addWidget(self.graphicsView_22)
        self.graphicsView_23 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_23.setObjectName("graphicsView_23")
        self.horizontalLayout_2.addWidget(self.graphicsView_23)
        self.graphicsView_24 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_24.setObjectName("graphicsView_24")
        self.horizontalLayout_2.addWidget(self.graphicsView_24)
        self.graphicsView_25 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_25.setObjectName("graphicsView_25")
        self.horizontalLayout_2.addWidget(self.graphicsView_25)
        self.graphicsView_26 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_26.setObjectName("graphicsView_26")
        self.horizontalLayout_2.addWidget(self.graphicsView_26)
        self.graphicsView_27 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_27.setObjectName("graphicsView_27")
        self.horizontalLayout_2.addWidget(self.graphicsView_27)
        self.graphicsView_28 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_28.setObjectName("graphicsView_28")
        self.horizontalLayout_2.addWidget(self.graphicsView_28)
        self.graphicsView_29 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_29.setObjectName("graphicsView_29")
        self.horizontalLayout_2.addWidget(self.graphicsView_29)
        self.graphicsView_30 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_30.setObjectName("graphicsView_30")
        self.horizontalLayout_2.addWidget(self.graphicsView_30)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.graphicsView_31 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_31.setObjectName("graphicsView_31")
        self.horizontalLayout_3.addWidget(self.graphicsView_31)
        self.graphicsView_32 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_32.setObjectName("graphicsView_32")
        self.horizontalLayout_3.addWidget(self.graphicsView_32)
        self.graphicsView_33 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_33.setObjectName("graphicsView_33")
        self.horizontalLayout_3.addWidget(self.graphicsView_33)
        self.graphicsView_34 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_34.setObjectName("graphicsView_34")
        self.horizontalLayout_3.addWidget(self.graphicsView_34)
        self.graphicsView_35 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_35.setObjectName("graphicsView_35")
        self.horizontalLayout_3.addWidget(self.graphicsView_35)
        self.graphicsView_36 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_36.setObjectName("graphicsView_36")
        self.horizontalLayout_3.addWidget(self.graphicsView_36)
        self.graphicsView_37 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_37.setObjectName("graphicsView_37")
        self.horizontalLayout_3.addWidget(self.graphicsView_37)
        self.graphicsView_38 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_38.setObjectName("graphicsView_38")
        self.horizontalLayout_3.addWidget(self.graphicsView_38)
        self.graphicsView_39 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_39.setObjectName("graphicsView_39")
        self.horizontalLayout_3.addWidget(self.graphicsView_39)
        self.graphicsView_40 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_40.setObjectName("graphicsView_40")
        self.horizontalLayout_3.addWidget(self.graphicsView_40)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.graphicsView_41 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_41.setObjectName("graphicsView_41")
        self.horizontalLayout_4.addWidget(self.graphicsView_41)
        self.graphicsView_42 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_42.setObjectName("graphicsView_42")
        self.horizontalLayout_4.addWidget(self.graphicsView_42)
        self.graphicsView_43 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_43.setObjectName("graphicsView_43")
        self.horizontalLayout_4.addWidget(self.graphicsView_43)
        self.graphicsView_44 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_44.setObjectName("graphicsView_44")
        self.horizontalLayout_4.addWidget(self.graphicsView_44)
        self.graphicsView_45 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_45.setObjectName("graphicsView_45")
        self.horizontalLayout_4.addWidget(self.graphicsView_45)
        self.graphicsView_46 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_46.setObjectName("graphicsView_46")
        self.horizontalLayout_4.addWidget(self.graphicsView_46)
        self.graphicsView_47 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_47.setObjectName("graphicsView_47")
        self.horizontalLayout_4.addWidget(self.graphicsView_47)
        self.graphicsView_48 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_48.setObjectName("graphicsView_48")
        self.horizontalLayout_4.addWidget(self.graphicsView_48)
        self.graphicsView_49 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_49.setObjectName("graphicsView_49")
        self.horizontalLayout_4.addWidget(self.graphicsView_49)
        self.graphicsView_50 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_50.setObjectName("graphicsView_50")
        self.horizontalLayout_4.addWidget(self.graphicsView_50)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.graphicsView_51 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_51.setObjectName("graphicsView_51")
        self.horizontalLayout_5.addWidget(self.graphicsView_51)
        self.graphicsView_52 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_52.setObjectName("graphicsView_52")
        self.horizontalLayout_5.addWidget(self.graphicsView_52)
        self.graphicsView_53 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_53.setObjectName("graphicsView_53")
        self.horizontalLayout_5.addWidget(self.graphicsView_53)
        self.graphicsView_54 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_54.setObjectName("graphicsView_54")
        self.horizontalLayout_5.addWidget(self.graphicsView_54)
        self.graphicsView_55 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_55.setObjectName("graphicsView_55")
        self.horizontalLayout_5.addWidget(self.graphicsView_55)
        self.graphicsView_56 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_56.setObjectName("graphicsView_56")
        self.horizontalLayout_5.addWidget(self.graphicsView_56)
        self.graphicsView_57 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_57.setObjectName("graphicsView_57")
        self.horizontalLayout_5.addWidget(self.graphicsView_57)
        self.graphicsView_58 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_58.setObjectName("graphicsView_58")
        self.horizontalLayout_5.addWidget(self.graphicsView_58)
        self.graphicsView_59 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_59.setObjectName("graphicsView_59")
        self.horizontalLayout_5.addWidget(self.graphicsView_59)
        self.graphicsView_60 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_60.setObjectName("graphicsView_60")
        self.horizontalLayout_5.addWidget(self.graphicsView_60)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.graphicsView_61 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_61.setObjectName("graphicsView_61")
        self.horizontalLayout_6.addWidget(self.graphicsView_61)
        self.graphicsView_62 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_62.setObjectName("graphicsView_62")
        self.horizontalLayout_6.addWidget(self.graphicsView_62)
        self.graphicsView_63 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_63.setObjectName("graphicsView_63")
        self.horizontalLayout_6.addWidget(self.graphicsView_63)
        self.graphicsView_64 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_64.setObjectName("graphicsView_64")
        self.horizontalLayout_6.addWidget(self.graphicsView_64)
        self.graphicsView_65 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_65.setObjectName("graphicsView_65")
        self.horizontalLayout_6.addWidget(self.graphicsView_65)
        self.graphicsView_66 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_66.setObjectName("graphicsView_66")
        self.horizontalLayout_6.addWidget(self.graphicsView_66)
        self.graphicsView_67 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_67.setObjectName("graphicsView_67")
        self.horizontalLayout_6.addWidget(self.graphicsView_67)
        self.graphicsView_68 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_68.setObjectName("graphicsView_68")
        self.horizontalLayout_6.addWidget(self.graphicsView_68)
        self.graphicsView_69 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_69.setObjectName("graphicsView_69")
        self.horizontalLayout_6.addWidget(self.graphicsView_69)
        self.graphicsView_70 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_70.setObjectName("graphicsView_70")
        self.horizontalLayout_6.addWidget(self.graphicsView_70)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.graphicsView_71 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_71.setObjectName("graphicsView_71")
        self.horizontalLayout_7.addWidget(self.graphicsView_71)
        self.graphicsView_72 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_72.setObjectName("graphicsView_72")
        self.horizontalLayout_7.addWidget(self.graphicsView_72)
        self.graphicsView_73 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_73.setObjectName("graphicsView_73")
        self.horizontalLayout_7.addWidget(self.graphicsView_73)
        self.graphicsView_74 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_74.setObjectName("graphicsView_74")
        self.horizontalLayout_7.addWidget(self.graphicsView_74)
        self.graphicsView_75 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_75.setObjectName("graphicsView_75")
        self.horizontalLayout_7.addWidget(self.graphicsView_75)
        self.graphicsView_76 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_76.setObjectName("graphicsView_76")
        self.horizontalLayout_7.addWidget(self.graphicsView_76)
        self.graphicsView_77 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_77.setObjectName("graphicsView_77")
        self.horizontalLayout_7.addWidget(self.graphicsView_77)
        self.graphicsView_78 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_78.setObjectName("graphicsView_78")
        self.horizontalLayout_7.addWidget(self.graphicsView_78)
        self.graphicsView_79 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_79.setObjectName("graphicsView_79")
        self.horizontalLayout_7.addWidget(self.graphicsView_79)
        self.graphicsView_80 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_80.setObjectName("graphicsView_80")
        self.horizontalLayout_7.addWidget(self.graphicsView_80)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.graphicsView_81 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_81.setObjectName("graphicsView_81")
        self.horizontalLayout_8.addWidget(self.graphicsView_81)
        self.graphicsView_82 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_82.setObjectName("graphicsView_82")
        self.horizontalLayout_8.addWidget(self.graphicsView_82)
        self.graphicsView_83 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_83.setObjectName("graphicsView_83")
        self.horizontalLayout_8.addWidget(self.graphicsView_83)
        self.graphicsView_84 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_84.setObjectName("graphicsView_84")
        self.horizontalLayout_8.addWidget(self.graphicsView_84)
        self.graphicsView_85 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_85.setObjectName("graphicsView_85")
        self.horizontalLayout_8.addWidget(self.graphicsView_85)
        self.graphicsView_86 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_86.setObjectName("graphicsView_86")
        self.horizontalLayout_8.addWidget(self.graphicsView_86)
        self.graphicsView_87 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_87.setObjectName("graphicsView_87")
        self.horizontalLayout_8.addWidget(self.graphicsView_87)
        self.graphicsView_88 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_88.setObjectName("graphicsView_88")
        self.horizontalLayout_8.addWidget(self.graphicsView_88)
        self.graphicsView_89 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_89.setObjectName("graphicsView_89")
        self.horizontalLayout_8.addWidget(self.graphicsView_89)
        self.graphicsView_90 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_90.setObjectName("graphicsView_90")
        self.horizontalLayout_8.addWidget(self.graphicsView_90)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.graphicsView_91 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_91.setObjectName("graphicsView_91")
        self.horizontalLayout_9.addWidget(self.graphicsView_91)
        self.graphicsView_92 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_92.setObjectName("graphicsView_92")
        self.horizontalLayout_9.addWidget(self.graphicsView_92)
        self.graphicsView_93 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_93.setObjectName("graphicsView_93")
        self.horizontalLayout_9.addWidget(self.graphicsView_93)
        self.graphicsView_94 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_94.setObjectName("graphicsView_94")
        self.horizontalLayout_9.addWidget(self.graphicsView_94)
        self.graphicsView_95 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_95.setObjectName("graphicsView_95")
        self.horizontalLayout_9.addWidget(self.graphicsView_95)
        self.graphicsView_96 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_96.setObjectName("graphicsView_96")
        self.horizontalLayout_9.addWidget(self.graphicsView_96)
        self.graphicsView_97 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_97.setObjectName("graphicsView_97")
        self.horizontalLayout_9.addWidget(self.graphicsView_97)
        self.graphicsView_98 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_98.setObjectName("graphicsView_98")
        self.horizontalLayout_9.addWidget(self.graphicsView_98)
        self.graphicsView_99 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_99.setObjectName("graphicsView_99")
        self.horizontalLayout_9.addWidget(self.graphicsView_99)
        self.graphicsView_100 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_100.setObjectName("graphicsView_100")
        self.horizontalLayout_9.addWidget(self.graphicsView_100)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout.addWidget(self.groupBox)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setAcceptDrops(False)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(40, 60, 430, 251))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setGeometry(QtCore.QRect(10, 70, 76, 40))
        self.frame_5.setAcceptDrops(False)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.graphicsView_101 = QtWidgets.QGraphicsView(self.frame_5)
        self.graphicsView_101.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphicsView_101.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.graphicsView_101.setLineWidth(1)
        self.graphicsView_101.setObjectName("graphicsView_101")
        self.horizontalLayout_11.addWidget(self.graphicsView_101)
        self.graphicsView_102 = QtWidgets.QGraphicsView(self.frame_5)
        self.graphicsView_102.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphicsView_102.setLineWidth(1)
        self.graphicsView_102.setObjectName("graphicsView_102")
        self.horizontalLayout_11.addWidget(self.graphicsView_102)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setGeometry(QtCore.QRect(10, 120, 114, 40))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setLineWidth(0)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.graphicsView_103 = QtWidgets.QGraphicsView(self.frame_6)
        self.graphicsView_103.setObjectName("graphicsView_103")
        self.horizontalLayout_12.addWidget(self.graphicsView_103)
        self.graphicsView_104 = QtWidgets.QGraphicsView(self.frame_6)
        self.graphicsView_104.setObjectName("graphicsView_104")
        self.horizontalLayout_12.addWidget(self.graphicsView_104)
        self.graphicsView_105 = QtWidgets.QGraphicsView(self.frame_6)
        self.graphicsView_105.setLineWidth(0)
        self.graphicsView_105.setObjectName("graphicsView_105")
        self.horizontalLayout_12.addWidget(self.graphicsView_105)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setGeometry(QtCore.QRect(10, 170, 152, 40))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.graphicsView_106 = QtWidgets.QGraphicsView(self.frame_7)
        self.graphicsView_106.setObjectName("graphicsView_106")
        self.horizontalLayout_13.addWidget(self.graphicsView_106)
        self.graphicsView_107 = QtWidgets.QGraphicsView(self.frame_7)
        self.graphicsView_107.setObjectName("graphicsView_107")
        self.horizontalLayout_13.addWidget(self.graphicsView_107)
        self.graphicsView_108 = QtWidgets.QGraphicsView(self.frame_7)
        self.graphicsView_108.setObjectName("graphicsView_108")
        self.horizontalLayout_13.addWidget(self.graphicsView_108)
        self.graphicsView_109 = QtWidgets.QGraphicsView(self.frame_7)
        self.graphicsView_109.setObjectName("graphicsView_109")
        self.horizontalLayout_13.addWidget(self.graphicsView_109)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.label_1 = QtWidgets.QLabel(self.frame_3)
        self.label_1.setGeometry(QtCore.QRect(80, 20, 34, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(10, 20, 38, 38))
        self.frame_4.setAcceptDrops(False)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\../images/shape.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(120, 72, 34, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(170, 120, 34, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(200, 170, 34, 34))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_1 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_1.setGeometry(QtCore.QRect(50, 400, 140, 61))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 400, 140, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "x4"))
        self.label_2.setText(_translate("MainWindow", "x3"))
        self.label_3.setText(_translate("MainWindow", "x2"))
        self.label_4.setText(_translate("MainWindow", "x1"))
        self.pushButton_1.setText(_translate("MainWindow", "Сброс"))
        self.pushButton_2.setText(_translate("MainWindow", "Играть"))
