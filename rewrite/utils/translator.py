"""
Contains the text for the UI in different languages. The text is stored in a dictionary, with the key being the English
text and the value being the translated text. The dictionary is then imported into the UI.py file, where the text is
displayed in the UI.
"""

from .misc import create_logger

versionNum = '1.1.0'
dateStr = '2023-07-12'

textEN = {
    'lan': 'English',
    'lanOption': 'English',
    'lanMenu': 'Language',
    'uiTitle': 'Petoi Desktop App',
    'calibTitle': 'Joint Calibrator',
    'skillComposerTitle': 'Petoi Skill Composer for OpenCat',
    'Model': 'Model',
    'Utility': 'Utility',
    'Joint Calibrator': 'Joint Calibrator',
    'Skill Composer': 'Skill Composer',
    'Task Scheduler': 'Task Scheduler',
    'Scheduler': 'Scheduler',
    'Firmware Uploader': 'Firmware Uploader',
    'Eye color picker': 'Eye color picker',
    'Creator Information': 'Creator Information',
    'Creator': 'Creator',
    'Location': 'Location',
    'Nature': 'Nature',
    'Earth': 'Earth',
    'InputCreator': 'Please input the nickname of the creator',
    'InputLocation': 'Please input the location of the creator',
    'Exit': 'Exit',
    'Help': 'Help',
    'About': 'About',
    'Repeat': 'Repeat',
    'Loop': 'Loop',
    'Frame': 'Frame',
    'Step': 'Step',
    'Delay': 'Delay',
    'Trig': 'Trigger',
    'Angle': 'Angle',
    'Note': 'Note',
    'Del': 'Del',
    'Add': 'Add',
    'Set': 'Set',
    'Save': 'Save',
    'Stop': 'Stop',
    'Joint Controller': 'Joint Controller',
    'Unbind All': 'Unbind All',
    'Yaw': 'Yaw',
    'Pitch': 'Pitch',
    '-Pitch': '-Pitch',
    'Roll': 'Roll',
    '-Roll': '-Roll',
    'Spinal': 'Spinal',
    'Height': 'Height',
    'Sideway': 'Sideway',
    'Head Pan': 'Head Pan',
    'Head Tilt': 'Head Tilt',
    'Tail Pan': 'Tail Pan',
    'N/A': 'N/A',
    'Left Front': 'Left Front',
    'Right Front': 'Right Front',
    'Right Back': 'Right Back',
    'Left Back': 'Left Back',
    'Shoulder': 'Shoulder',
    'Arm': 'Arm',
    'Knee': 'Knee',
    'State Dials': 'State Dials',
    'Connect': 'Connect',
    'Connected': 'Connected',
    'Listening': 'Listening',
    'All': 'All',
    'None': 'None',
    'Servo': 'Servo',
    'Gyro': 'Gyro',
    'Random': 'Random',
    'Send': 'Send',
    'Postures': 'Preset Postures',
    'Skill Editor': 'Skill Editor',
    'Play': 'Play',
    'Pause': 'Pause',
    'Import': 'Import',
    'Restart': 'Restart',
    'Export': 'Export',
    'Undo': 'Undo',
    'Redo': 'Redo',
    'Open File': 'Open File',
    'Cancel': 'Cancel',
    'OK': 'OK',
    'Refresh': 'Refresh',
    'Multiple': 'Multiple',
    'Skill List': 'Skill List',
    'Type of skill': 'Type of skill',
    'Name of skill': 'Name of skill',
    'exampleFormat': 'Import from files, or copy & paste the skill data from instinct.h in the following format.\n'
                     '* Keep the curly brackets!',
    'Quit': 'Quit',
    'Do you want to quit?': 'Do you want to quit?',
    'mirror': '      MirrorAll',
    '>|<': '>|<',
    'Posture': '  Posture',
    'Gait': '  Gait',
    'Behavior': '  Behavior',
    'Clear': 'Clear',
    'max': 'max',

    'Manual mode': 'Manual mode',
    'Replug mode': 'Replug mode',
    'Replug prompt': '''WARNING: Connection Failed!\n\n
* If the main board is NOT connected to the computer:\n
Click the button below. Connect the USB cable to the main board, then plug the other end to the COMPUTER.\n\n
* If the main board is already connected to the computer via a USB cable:\n
1. Confirm your computer can recognize the USB device.\n
More details can be found at https://docs.petoi.com/upload-firmware\n
2. After clicking the button below, unplug the USB cable from the COMPUTER side, and then plug it back.
''',
    'Confirm': 'Confirm',
    'Counting down to manual mode: ': 'Counting down to manual mode: ',
    'Info': 'Info',
    'New port prompt': 'Discover a new USB device: ',
    'Please select the port from the list': 'Please select the port from the list',
    '* Port ': '* Port ',
    ' cannot be opened': ' cannot be opened',

    'Calibrate': 'Calibrate',
    'Rest': 'Rest',
    'Stand Up': 'Stand Up',
    'Walk': 'Walk',
    'Abort': 'Abort',
    'Do you want to save the offsets?': 'Do you want to save the offsets?',
    'uploaderTitle': 'Firmware Uploader',
    'labTrans': 'Change Language',
    'labChi': 'Chinese',
    'labEng': 'English',
    'labHelp': 'Help',
    'labAbout': 'About',
    'labExit': 'Exit',
    'labFileDir': 'Choose the release folder',
    'btnFileDir': '...',
    'titleFileDir': 'Please choose the release folder',
    'labPort': 'Serial port',
    'labSoftwareVersion': 'Software version',
    'labBoardVersion': 'Board version',
    'labProduct': 'Product',
    'labMode': 'Mode',
    'rbnWalk': 'Walk',
    'rbnUltrasonic': 'Ultrasonic',
    'rbnCamera': 'Camera',
    'Parameters': 'Parameters',
    'Main function': 'Main function',
    'btnFacReset': 'Factory Reset',
    'tipFacReset': ''' After factory reset, you need to do joint calibration, please refer to: 
 https://docs.petoi.com/joint-calibration ''',
    'btnUpgrade': 'Upgrade the Firmware',
    'tipUpgrade': ''' Upgrade both the parameters and the main function. 
 * Mandatory if you just downloaded a new version of this software. 
 * You can select \'N\' to preserve the calibration values. ''',
    'btnUpdateMode': 'Update the Mode Only',
    'tipUpdateMode': ''' If you have upgraded the firmware at least once after a new download, 
 it\'s faster to only switch the modes without refreshing the parameters. ''',
    'Warning': 'Warning',
    'Uploading': 'Uploading ',
    'is successfully uploaded': ' is successfully uploaded',
    'failed to upload': ' failed to upload',
    'Need to manually select the model type (Nybble/Bittle)': 'Need to manually select the model type (Nybble/Bittle)',
    'msgFileDir': 'Please choose the release folder!',
    'msgPort': 'Please choose the correct serial port!',

    'msgNoneAvrdude': '''There is no avrdude. Please install avrdude at first! For details, please refer to :
    https://docs.petoi.com/desktop-app/firmware-uploader#install-avrdude-in-the-linux-os''',

    'titleVersion': 'Version information',

    'msgVersion': 'Version: ' + versionNum + '\n' +
                  '''Firmware upload tool for OpenCat
    Copyright © 2018-2023
    All rights reserved Petoi LLC
    https://www.petoi.com\n''' + dateStr,

    'reset joints?': 'Reset joint offsets? (Y/N)',
    'resetting joints': 'Reset joint offsets...',
    'joints reset': 'Reset joint offsets complete!',

    'update instincts?': 'Update Instinct? (Y/N)',
    'updating instincts': 'Updating Instincts......',
    'instincts updated': 'Instincts updated',

    'calibrate IMU?': '''Calibrate IMU? (Y/N)
    Note: Lay the mainboard FLAT on a table!''',
    'calibrating IMU': 'Calibrating IMU...',
    'IMU calibrated': 'Calibrate IMU complete!',

    'parameterFinish': '''Parameters initialized!
     The next step is uploading the Main Function!''',
    '9685 Calibrated': 'PCA9685 has been calibrated successfully!',
    'msgFinish': 'Firmware upload complete!',
    'msgMode': 'Invalid, please select another mode!',

    'Standard': 'Standard',
    'RandomMind': 'RandomMind',
    'Ultrasonic': 'Ultrasonic',
    'Voice': 'Voice',
    'Camera': 'Camera',
    'Mind+': 'Mind+',
    'RandomMind_Ultrasonic': 'RandomMind_Ultrasonic',

    'Breath': 'Breath',
    'Rotate': 'Rotate',
    'Flash': 'Flash',
    'Meow': 'Meow',

    'labEdit': 'Edit',
    'labTheme': 'Theme',
    'tipConnect': 'Keep updating the active serial\nports until it\'s disabled',
    'tipPortMenu': 'Control single or all of the devices',
    'tipServo': 'Activate/deactivate the servos',
    'tipGyro': 'Activate/deactivate the gyroscope',
    'tipRandom': 'Activate/deactivate the random behaviors\n* in certain modes',
    'tipBinder': 'Bind to other joints',
    'tipRevBinder': 'Reversely bind to other joints',
    'tipPlay': 'Go through the sheduler from the active frame\nYou may stop while playing',
    'tipImport': 'Import skills from files or texts',
    'tipRestart': 'Clear all the frames in the scheduler!',
    'tipExport': 'The skill will be sent in real time and saved\nin the static memory of the robot\n'
                 'Use serial token \'T\' to call the last sent skill',
    'tipMirror': 'Mirror the current frame',
    'tipMirrorXport': 'Mirror the whole skill when exporting\n* Effective when exporting the whole skill',
    'tipGorB': 'A behavior interpolates between the key frames and excutes only once\nA gait loops over all the frames '
               'without any smoothing',
    'tipLoop': 'Set the starting and ending frames for looping\n* Effective when exporting the whole skill',
    'tipRepeat': 'Enter the number of loops\n-1 for infinite loop. Only the \"reset\" button can break the loop!\n'
                 '* Effective when exporting the whole skill',
    'tipSet': 'Jump to/save the current frame',
    'tipStep': 'Unit: degree/step\n* Effective when exporting the whole skill',
    'tipDelay': 'Unit: millisecond\nDelay after the current frame, before entering the next frame\n'
                'If the trigger is valid, the delay starts after the trigger\n'
                '* Effective when exporting the whole skill',
    'tipTrig': 'Trigger the next frame only when the body rolls\nover the triggering angle in a certain direction\n'
               '* Effective when exporting the whole skill',
    'tipTrigAngle': 'The critical angle for the trigger\n* Effective when exporting the whole skill',
    'tipNote': 'Give the frame an easy to remember name',
    'tipAdd': 'Copy the active frame and\ninsert it to the next row',
    'tipDel': 'Delete the current frame',

    'tipImgWiring': 'Pay attention to the location and direction of the servo plugs\n'
                    'Long-press the battery\'s button to turn on the power\nClick \"Calibrate\" to '
                    'rotate all the servos to the calibration state\nAttach the legs and head perpendicularly\n'
                    'Use the slider to align the edges of the legs and the reference ruler parallelly',
    'tipImgPosture': 'Switch between postures to test the calibration results\nSave the offsets in time\n'
                     'No need for calibration in the future',
}
textCN = {
    'lan': 'Simplified Chinese',
    'lanOption': '中文',
    'lanMenu': '语言',
    'uiTitle': '派拓艺桌面应用',
    'skillComposerTitle': '派拓艺技能创作坊',
    'calibTitle': '关节校准器',
    'Skill Composer': '技能创作坊',
    'Task Scheduler': '任务时序器',
    'Model': '产品',
    'Utility': '应用工具',
    'Joint Calibrator': '关节校准',
    'Scheduler': '时序器',
    'Firmware Uploader': '固件上载',
    'Eye color picker': '眼色选择器',
    'Creator Information': '创作者信息',
    'Creator': '创作者',
    'Location': '位置',
    'Nature': '自然',
    'Earth': '地球',
    'InputCreator': '请输入创作者昵称',
    'InputLocation': '请输入创作者位置',
    'Exit': '退出',
    'Help': '帮助',
    'About': '关于',
    'Repeat': '重复',
    'Loop': '循环',
    'Frame': '帧',
    'Step': '速度',
    'Delay': '延时',
    'Trig': '触发轴',
    'Angle': '触发角',
    'Note': '标记',
    'Del': '删除',
    'Add': '添加',
    'Set': '设置',
    'Save': '保存',
    'Stop': '停止',
    'Joint Controller': '关节控制器',
    'Unbind All': '取消所有联动',
    'Yaw': '偏航',
    'Pitch': '俯仰',
    '-Pitch': '逆俯仰',
    'Roll': '横滚',
    '-Roll': '逆横滚',
    'Spinal': '脊向',
    'Height': '高度',
    'Sideway': '侧向',
    'Head Pan': '头部平转',
    'Head Tilt': '头部俯仰',
    'Tail Pan': '尾巴平转',
    'N/A': '闲置',
    'Left Front': '左前',
    'Right Front': '右前',
    'Right Back': '右后',
    'Left Back': '左后',
    'Shoulder': '肩',
    'Arm': '臂',
    'Knee': '膝',
    'State Dials': '状态开关',
    'Connect': '连接',
    'Connected': '已连接',
    'Listening': '检测中',
    'All': '全部',
    'None': '无',
    'Servo': '舵机',
    'Pause': '暂停',
    'Gyro': '陀螺仪',
    'Random': '随机行为',
    'Send': '发送',
    'Postures': '预设姿态',
    'Skill Editor': '技能编辑器',
    'Play': '播放',
    'Import': '导入',
    'Restart': '重置',
    'Export': '导出',
    'Undo': '撤消',
    'Redo': '重复',
    'Open File': '打开文件',
    'Cancel': '取消',
    'OK': '确认',
    'Multiple': '载入多个',
    'Skill List': '技能表',
    'Type of skill': '技能类型',
    'Name of skill': '技能名',
    'exampleFormat': '从文件导入，或以下列格式从 instinct.h 复制粘贴技能数组。\n* 保留大括号！',
    'Quit': '退出',
    'Do you want to quit?': '要退出吗？',
    'mirror': '      镜像导出',
    '>|<': '>|<',
    'Posture': '   姿势',
    'Gait': '   步态',
    'Behavior': '   行为',
    'Clear': '清空',
    'max': '最快',
    'Calibrate': '校准位',
    'Rest': '休息',
    'Stand Up': '站立',
    'Walk': '行走',
    'Abort': '放弃',
    "Refresh": "刷新",

    'Manual mode': '手动模式',
    'Replug mode': '重新拔插',
    'Replug prompt': '''警告：上传失败！\n\n
* 如果主板未连接到计算机：\n
点击下面的按钮，将USB数据线连接到主板，然后将另一端插入电脑。\n\n
* 如果主板已经通过USB数据线连接到计算机：\n
1. 确认您的计算机可以识别 USB 设备。\n
   更多详情请参考 https://docs.petoi.com/upload-firmware\n
2. 点击下面的按钮后，从电脑端拔下USB数据线，然后再插回去。
''',
    'Confirm': '确认',
    'Counting down to manual mode: ': '切换到手动模式倒计时：',
    'Info': '提示',
    'New port prompt': '发现新的USB口串口设备：',
    'Please select the port from the list': '请从列表中选择串口名称',
    '* Port ': '* 端口 ',
    ' cannot be opened': ' 无法打开',

    'Do you want to save the offsets?': '要保存校准值吗？',
    'Need to manually select the model type (Nybble/Bittle)': '请手动选择型号(Nybble/Bittle)',
    'uploaderTitle': '上传工具',
    'title': '上传工具',
    'labTrans': '切换语言',
    'labChi': '中文',
    'labEng': '英文',
    'labHelp': '帮助',
    'labAbout': '关于',
    'labExit': '退出',
    'labFileDir': '选择release文件夹',
    'btnFileDir': '...',
    'titleFileDir': '请选择release文件夹',
    'labPort': '串口',
    'labSoftwareVersion': '软件版本',
    'labBoardVersion': '主板型号',
    'labProduct': '产品',
    'labMode': '模式',
    'Warning': "警告",
    'msgFileDir': '请选择release文件夹！',
    'msgPort': '请选择正确的串口！',

    'msgNoneAvrdude': '''没有找到可执行程序文件 avrdude。请先安装 avrdude！详细说明请参考：
    https://docs.petoi.com/v/chinese/zhuo-mian-ying-yong/gu-jian-shang-zai#linux-xi-tong-zhong-an-zhuang-avrdude''',

    'Uploading': '上传',
    'is successfully uploaded': ' 上传成功！',
    'failed to upload': ' 上传失败！',
    'titleVersion': '版本信息',

    'msgVersion': '版本：' + versionNum + '\n' +
                  '''OpenCat固件上传工具
    版权所有 © 2018-2023
    派拓艺（深圳）科技有限责任公司
    https://www.petoi.com\n''' + dateStr,

    'reset joints?': '舵机校准参数清零？(Y/N)',
    'reseting joints': '校准参数清零中......',
    'joints reset': '校准参数清零完成！',

    'update instincts?': '更新技能? (Y/N)',
    'updating instincts': '刷新EEPROM数据......',
    'instincts updated': '更新技能完成!',

    'calibrate IMU?': '''校准 IMU？(Y/N)
            注意: 请务必将主板保持水平放置！''',
    'calibrating IMU': 'IMU校准中...',
    'IMU calibrated': 'IMU校准完成！',

    'parameterFinish': '''参数初始化完成！
                       接下来将开始上传主程序！''',
    '9685 Calibrated': 'PCA9685校准完成！',
    'msgFinish': '固件上传完成！',
    'msgMode': '无效模式，请选择其他模式！',
    'Standard': '标准',
    'RandomMind': '随机',
    'Ultrasonic': '超声波',
    'Voice': '语音',
    'Camera': '摄像头',
    'Mind+': 'Mind+',
    'RandomMind_Ultrasonic': '随机_超声波',
    'Parameters': '参数',
    'Main function': '主程序',
    'btnFacReset': '恢复出厂设置',
    'tipFacReset': ''' 恢复出厂设置后，你需要重新校准关节舵机，请参考：
 https://docs.petoi.com/joint-calibration ''',
    'btnUpgrade': '升级固件',
    'tipUpgrade': ''' 升级参数固件和主程序固件。
 * 如果您初次下载了该软件的新版本，则必须点击此按钮升级固件。
 * 您可以选择 “N” 来保留校准值。''',
    'btnUpdateMode': '只更新模式',
    'tipUpdateMode': ''' 如果您在下载后至少升级过一次固件，
 只切换模式而不刷新参数固件会更快。''',
    'Breath': '渐变',
    'Rotate': '旋转',
    'Flash': '闪烁',
    'Meow': '喵！',
    'labEdit': '编辑',
    'labTheme': '主题',
    'tipConnect': '持续更新活跃串口列表直到被挂起',
    'tipPortMenu': '控制单个或所有设备',
    'tipServo': '启用或禁用舵机',
    'tipGyro': '启用或禁用陀螺仪',
    'tipRandom': '启用或禁用随机动作\n* 只在某些模式下',
    'tipBinder': '正向联动其他关节',
    'tipRevBinder': '反向联动其他关节',
    'tipPlay': '从当前帧开始播放时序器中的动作\n可以中途停止',
    'tipImport': '从文件或文本导入技能',
    'tipRestart': '清空时序器中的所有帧！',
    'tipExport': '技能会实时发送并保存在机器人的静态内存\n可以通过串口指令\'T\'调用上次发送的技能',
    'tipMirror': '镜像当前帧',
    'tipMirrorXport': '导出整个技能的镜像\n* 在导出整体技能时生效',
    'tipGorB': '行为给关键帧插值并只执行一轮\n步态循环执行所有帧并且不加平滑处理',
    'tipLoop': '选择循环的起止帧\n* 在导出整体技能时生效',
    'tipRepeat': '输入循环次数\n-1为无限循环，只有按复位键才能跳出循环!\n* 在导出整体技能时生效',
    'tipSet': '跳入/保存当前帧',
    'tipStep': '单位：度/步长\n* 在导出整体技能时生效',
    'tipDelay': '单位：毫秒\n完成当前帧后延时，再执行下一帧\n如触发器有效，则在触发后才开始延时\n* 在导出整体技能时生效',
    'tipTrig': '当机身以特定方向越过触发角时触发下一帧\n* 在导出整体技能时生效',
    'tipTrigAngle': '触发临界角\n* 在导出整体技能时生效',
    'tipNote': '给当前帧起一个便于记忆的名字',
    'tipAdd': '复制当前帧并插入到下一行',
    'tipDel': '删除当前帧',
    'tipImgWiring': '接舵机线时注意插头的位置和正反\n长按电池按钮通电\n点击“校准“使所有舵机旋转到校准位\n按垂直关系安装四肢和头\n控制滑条使大小腿边缘与校准尺平行',
    'tipImgPosture': '在各姿势间切换，检查校准效果\n及时保存修正值\n后续使用无需再校准',
}

textCN_TW = {
    'lan': 'Traditional Chinese',
    'lanOption': '繁体中文',
    'lanMenu': '語言',
    'uiTitle': 'Petoi桌面應用',
    'skillComposerTitle': 'Petoi技能創作坊',
    'calibTitle': '關節校準器',
    'Skill Composer': '技能創作坊',
    'Task Scheduler': '任務排程器',
    'Model': '產品',
    'Utility': '應用工具',
    'Joint Calibrator': '關節校準',
    'Scheduler': '排程器',
    'Firmware Uploader': '固件上傳',
    'Eye color picker': '眼睛顏色選擇器',
    'Creator Information': '創作者信息',
    'Creator': '創作者',
    'Location': '位置',
    'Nature': '自然',
    'Earth': '地球',
    'InputCreator': '請輸入創作者昵稱',
    'InputLocation': '請輸入創作者位置',
    'Exit': '退出',
    'Help': '幫助',
    'About': '關於',
    'Repeat': '重複',
    'Loop': '循環',
    'Frame': '幀',
    'Step': '速度',
    'Delay': '延遲',
    'Trig': '觸發',
    'Angle': '角度',
    'Note': '標記',
    'Del': '刪除',
    'Add': '添加',
    'Set': '設置',
    'Save': '儲存',
    'Stop': '停止',
    'Joint Controller': '關節控制器',
    'Unbind All': '取消所有聯動',
    'Yaw': '偏航',
    'Pitch': '俯仰',
    '-Pitch': '逆俯仰',
    'Roll': '横滾動',
    '-Roll': '逆横滾動',
    'Spinal': '脊向',
    'Height': '高度',
    'Sideway': '側向',
    'Head Pan': '頭部平轉',
    'Head Tilt': '頭部俯仰',
    'Tail Pan': '尾巴平轉',
    'N/A': '閒置',
    'Left Front': '左前',
    'Right Front': '右前',
    'Right Back': '右後',
    'Left Back': '左後',
    'Shoulder': '肩',
    'Arm': '臂',
    'Knee': '膝',
    'State Dials': '狀態開關',
    'Connect': '連接',
    'Connected': '已連接',
    'Listening': '檢測中',
    'All': '全部',
    'None': '無',
    'Servo': '伺服',
    'Pause': '暫停',
    'Gyro': '陀螺儀',
    'Random': '随機行為',
    'Send': '發送',
    'Postures': '預設姿態',
    'Skill Editor': '技能编輯器',
    'Play': '播放',
    'Import': '導入',
    'Restart': '重置',
    'Export': '導出',
    'Undo': '撤消',
    'Redo': '重複',
    'Open File': '打開文件',
    'Cancel': '取消',
    'OK': '確認',
    'Multiple': '載入多個',
    'Skill List': '技能表',
    'Type of skill': '技能類型',
    'Name of skill': '技能名',
    'exampleFormat': '從文件導入，或以下列格式從 instinct.h 複製黏貼技能數組。\n* 保留大括號！',
    'Quit': '退出',
    'Do you want to quit?': '要退出嗎？',
    'mirror': '      鏡像導出',
    '>|<': '>|<',
    'Posture': '   姿勢',
    'Gait': '   步態',
    'Behavior': '   行為',
    'Clear': '清空',
    'max': '最快',
    'Calibrate': '校準位',
    'Rest': '休息',
    'Stand Up': '站立',
    'Walk': '行走',
    'Abort': '放棄',
    'Refresh': '刷新',

    'Manual mode': '手動模式',
    'Replug mode': '重新拔插',
    'Replug prompt': '''警告：上傳失敗！\n\n
* 如果主機板未連接到電腦：\n
點擊下面的按鈕後，將USB資料線連接到主機板，然後將另一端插入電腦。\n\n
* 如果主機板已經通過USB資料線連接到電腦：\n
1. 確認您的電腦可以識別 USB 設備。\n
   更多詳情請參考 https://docs.petoi.com/upload-firmware\n
2. 點擊下面的按鈕後，從電腦端拔下USB資料線，然後再插回去。
''',
    'Confirm': '確認',
    'Counting down to manual mode: ': '切換到手動模式倒計時：',
    'Info': '提示',
    'New port prompt': '發現新的USB口串口設備：',
    'Please select the port from the list': '請從列表中選擇串口名稱',
    '* Port ': '* 埠 ',
    ' cannot be opened': ' 無法打開',

    'Do you want to save the offsets?': '要保存校準值嗎？',
    'Need to manually select the model type (Nybble/Bittle)': '請手動選擇型號(Nybble/Bittle)',
    'uploaderTitle': '上傳者標題',
    'labTrans': '切換語言',
    'title': '標題',
    'labChi': '中文',
    'labEng': '英文',
    'labHelp': '幫助',
    'labAbout': '關於',
    'labExit': '退出',
    'labFileDir': '選擇release文件夾',
    'btnFileDir': '...',
    'titleFileDir': '請選擇release文件夾',
    'labPort': '端口',
    'labSoftwareVersion': '軟件版本',
    'labBoardVersion': '主板型號',
    'labProduct': '產品',
    'labMode': '模式',
    'Warning': '警告',
    'msgFileDir': '請選擇release文件夾！',
    'msgPort': '請選擇正確的端口！',

    'msgNoneAvrdude': '''沒有找到可執行程式文件 avrdude。請先安裝 avrdude！詳細說明請參考：
    https://docs.petoi.com/v/chinese/zhuo-mian-ying-yong/gu-jian-shang-zai#linux-xi-tong-zhong-an-zhuang-avrdude''',

    'Uploading': '上傳',
    'is successully uploaded': ' 上傳成功！',
    'failed to upload': ' 上傳失敗！',
    'titleVersion': '版本信息',

    'msgVersion': '版本：' + versionNum + '\n' +
                  '''OpenCat固件上傳工具
    版權所有 © 2018-2023
    派拓藝（深圳）科技有限责任公司
    https://www.petoi.com\n''' + dateStr,

    'reset joints?': '舵機校準參數清零？(Y/N)',
    'reseting joints': '校準參數清零中......',
    'joints reset': '校準參數清零完成！',

    'update instincts?': '更新技能？(Y/N)',
    'updating instincts': '刷新EEPROM數據......',
    'instincts updated': '更新技能完成！',

    'calibrate IMU?': '''校準 IMU？(Y/N)
            注意: 請務必將主板保持水平放置！''',
    'calibrating IMU': 'IMU校準中......',
    'IMU calibrated': 'IMU校準完成！',

    'parameterFinish': '''參數初始化完成！
                       接下來將開始上傳主程序！''',
    '9685 Calibrated': 'PCA9685校準完成！',
    'msgFinish': '固件上傳完成!',
    'msgMode': '無效模式，請選擇其他模式!',
    'Standard': '標準',
    'RandomMind': '随機',
    'Ultrasonic': '超聲波',
    'Voice': '語音',
    'Camera': '鏡頭',
    'Mind+': 'Mind+',
    'RandomMind_Ultrasonic': '随機_超聲波',
    'Parameters': '參數',
    'Main function': '主程序',
    'btnFacReset': '恢復出廠設置',
    'tipFacReset': ''' 恢復出廠設置後，你需要重新校準關節舵機，請參考：
 https://docs.petoi.com/joint-calibration ''',
    'btnUpgrade': '升級固件',
    'tipUpgrade': ''' 升級參數固件和主程序固件。
 * 如果您初次下載了該軟體的新版本，則必須點擊此按鈕升級固件。
 * 您可以選擇 “N” 來保留校準值。''',
    'btnUpdateMode': '僅更新模式',
    'tipUpdateMode': ''' 如果您在下載後至少升級過一次固件，
 僅切換模式而不刷新參數固件會更快。''',
    'Breath': '漸變',
    'Rotate': '旋轉',
    'Flash': '閃爍',
    'Meow': '喵！',

    'labEdit': '编辑',
    'labTheme': '主题',
    'tipConnect': '持續更新活耀端口列表直到被掛起',
    'tipPortMenu': '控制單個或所有設備',
    'tipServo': '啟用或禁用舵機',
    'tipGyro': '啟用或禁用陀螺儀',
    'tipRandom': '啟用或禁用随機動作\n* 只在某些模式下',
    'tipBinder': '正向聯動其他關節',
    'tipRevBinder': '反向聯動其他關節',
    'tipPlay': '從當前幀開始播放時序器中的動作\n可以中途停止',
    'tipImport': '從文件或文本導入技能',
    'tipRestart': '清空时序器中的所有幀！',
    'tipExport': '技能會實時發送並保存在機器人的静態内存\n可以通過端口指令\'T\'適用上次發送的技能',
    'tipMirror': '鏡像當前幀',
    'tipMirrorXport': '導出整個技能的鏡像\n* 在導出整體技能時生效',
    'tipGorB': '行為給關鍵幀插值並只執行一輪\n步態循環執行所有幀並且不加平滑處理',
    'tipLoop': '選擇循環的起止幀\n* 在導出整體技能時生效',
    'tipRepeat': '輸入循環次數\n-1為無限循環，只有按復位健才能跳出循環!\n* 在導出整體技能時生效',
    'tipSet': '跳入/保存當前幀',
    'tipStep': '單位：度/步長\n* 在導出整體技能時生效',
    'tipDelay': '單位：毫秒\n完成當前幀後延時，再執行下一幀\n如觸發器有效，則在觸發後才開始延時\n* 在導出整體技能時生效',
    'tipTrig': '當機身以特定方向越過觸發角時觸發下一幀\n* 在導出整體技能時生效',
    'tipTrigAngle': '觸發臨界角\n* 在導出整體技能時生效',
    'tipNote': '给當前幀起一個便於記憶的名字',
    'tipAdd': '複製當前幀並插入到下一行',
    'tipDel': '刪除當前幀',
    'tipImgWiring': '接舵機線时注意插頭的位置和正反\n長按電池按鈕通電\n點擊“校準“使所有舵機旋轉到校準位\n按垂直關係安装四肢和頭\n控制滑條使大小腿邊緣與校準尺平行',
    'tipImgPosture': '在各姿勢間切换，檢查校準效果\n及時保存修正值\n後續使用無需再校準',
}

textDE = {
    'lan': 'German',
    'lanOption': 'Deutsh',
    'lanMenu': 'Sprache',
    'uiTitle': 'Petoi Desktop-App',
    'calibTitle': 'Gelenkkalibrator',
    'skillComposerTitle': 'Petoi Einstellungen Fähigkeiten für OpenCat',
    'Model': 'Modell',
    'Utility': 'Werkzeug',
    'Joint Calibrator': 'Gelenkkalibrator',
    'Skill Composer': 'Einstellungen Fähigkeiten',
    'Task Scheduler': 'Aufgabenplaner',
    'Scheduler': 'Planer',
    'Firmware Uploader': 'Firmware-Uploader',
    'Eye color picker': 'Augenfarbauswahl',
    'Creator Information': 'Erstellerinformationen',
    'Creator': 'Schöpfer',
    'Location': 'Standort',
    'Nature': 'Natur',
    'Earth': 'Erde',
    'InputCreator': 'Bitte geben Sie den Spitznamen des Erstellers ein',
    'InputLocation': 'Bitte geben Sie den Standort des Erstellers ein',
    'Exit': 'Beenden',
    'Help': 'Hilfe',
    'About': 'Über',
    'Repeat': 'Wiederholen',
    'Loop': 'Schleife',
    'Frame': 'Frame',
    'Step': 'Schritt',
    'Delay': 'Verzögerung',
    'Trig': 'Auslöser',
    'Angle': 'Winkel',
    'Note': 'Notiz',
    'Del': 'Löschen',
    'Add': 'Hinzufügen',
    'Set': 'Einstellen',
    'Save': 'Speichern',
    'Stop': 'Stoppen',
    'Joint Controller': 'Gelenk-Controller',
    'Unbind All': 'Alle lösen',
    'Yaw': 'Gier',
    'Pitch': 'Nick',
    '-Pitch': '-Nick',
    'Roll': 'Roll',
    '-Roll': '-Roll',
    'Spinal': 'Wirbelsäule',
    'Height': 'Höhe',
    'Sideway': 'Seitwärts',
    'Head Pan': 'Kopf-Pan',
    'Head Tilt': 'Kopf-Neigung',
    'Tail Pan': 'Schwanz-Pan',
    'N/A': 'N/V',
    'Left Front': 'Links vorne',
    'Right Front': 'Rechts vorne',
    'Right Back': 'Rechts hinten',
    'Left Back': 'Links hinten',
    'Shoulder': 'Schulter',
    'Arm': 'Arm',
    'Knee': 'Knie',
    'State Dials': 'Zustandsregler',
    'Connect': 'Verbinden',
    'Connected': 'Verbunden',
    'Listening': 'Hören',
    'All': 'Alle',
    'None': 'Keine',
    'Servo': 'Servo',
    'Gyro': 'Gyro',
    'Random': 'Zufällig',
    'Send': 'Schicken',
    'Postures': 'Voreingestellte Haltungen',
    'Skill Editor': 'Skill-Editor',
    'Play': 'Abspielen',
    'Pause': 'Pausieren',
    'Import': 'Importieren',
    'Restart': 'Neustart',
    'Export': 'Exportieren',
    'Undo': 'Rückgängig',
    'Redo': 'Wiederholen',
    'Open File': 'Datei öffnen',
    'Cancel': 'Abbrechen',
    'OK': 'OK',
    'Refresh': 'Aktualisieren',
    'Multiple': 'Mehrere',
    'Skill List': 'Skill-Liste',
    'Type of skill': 'Art des Skills',
    'Name of skill': 'Name des Skills',
    'exampleFormat': 'Importiere aus Dateien oder kopiere die Skill-Daten von instinct.h im folgenden Format.\n'
                     '* Behalte die geschweiften Klammern bei!',
    'Quit': 'Beenden',
    'Do you want to quit?': 'Möchten Sie beenden?',
    'mirror': 'Spiegeln',
    '>|<': '>|<',
    'Posture': '  Posture',
    'Gait': 'Gangart',
    'Behavior': 'Verhalten',
    'Clear': 'Löschen',
    'max': 'max.',

    'Manual mode': 'Manueller Modus',
    'Replug mode': 'Replug-Modus',
    'Replug prompt': '''WARNUNG: Hochladen fehlgeschlagen!\n\n
* Wenn die Hauptplatine NICHT mit dem Computer verbunden ist:\n
Klicken Sie auf die Schaltfläche unten. Verbinden Sie das USB-Kabel mit der Hauptplatine und stecken Sie dann das andere
 Ende in den COMPUTER.\n\n
* Wenn die Hauptplatine bereits über ein USB-Kabel mit dem Computer verbunden ist:\n
1. Vergewissern Sie sich, dass Ihr Computer das USB-Gerät erkennen kann.\n
Weitere Einzelheiten finden Sie unter https://docs.petoi.com/upload-firmware.\n
2. Nachdem Sie auf die Schaltfläche unten geklickt haben, ziehen Sie das USB-Kabel von der COMPUTER-Seite ab und stecken
 Sie es dann wieder ein.
''',
    'Confirm': 'Bestätigen',
    'Counting down to manual mode: ': 'Countdown zum manuellen Modus: ',
    'Info': 'Information',
    'New port prompt': 'Entdecken Sie das neue USB-Gerät: ',
    'Please select the port from the list': 'Bitte wählen Sie den Port aus der Liste aus',
    '* Port ': '* Hafen ',
    ' cannot be opened': ' Kann nicht geöffnet werden',

    'Calibrate': 'Kalibrieren',
    'Rest': 'Ruhe',
    'Stand Up': 'Aufstehen',
    'Walk': 'Gehen',
    'Abort': 'Abbrechen',
    'Do you want to save the offsets?': 'Möchten Sie die Abweichungen speichern?',
    'uploaderTitle': 'Firmware-Uploader',
    'labTrans': 'Sprache ändern',
    'labChi': 'Chinesisch',
    'labEng': 'Englisch',
    'labHelp': 'Hilfe',
    'labAbout': 'Über',
    'labExit': 'Beenden',
    'labFileDir': 'Wählen Sie das Freigabe-Verzeichnis',
    'btnFileDir': '...',
    'titleFileDir': 'Bitte wählen Sie das Freigabe-Verzeichnis',
    'labPort': 'Serielle Schnittstelle',
    'labSoftwareVersion': 'Software-Version',
    'labBoardVersion': 'Board-Version',
    'labProduct': 'Produkt',
    'labMode': 'Modus',
    'rbnWalk': 'Gehen',
    'rbnUltrasonic': 'Ultraschall',
    'rbnCamera': 'Kamera',
    'Parameters': 'Parameter',
    'Main function': 'Hauptfunktion',
    'btnFacReset': 'Werkseinstellungen zurückgesetzt',
    'tipFacReset': ''' Nach dem Zurücksetzen auf die Werkseinstellungen müssen Sie eine gemeinsame Kalibrierung 
    durchführen. 
 Weitere Informationen finden Sie unter: https://docs.petoi.com/joint-calibration ''',
    'btnUpgrade': 'Aktualisieren Sie die Firmware',
    'tipUpgrade': ''' Aktualisieren Sie sowohl die Parameter als auch die Hauptfunktion. 
 * Obligatorisch, wenn Sie gerade eine neue Version dieser Software heruntergeladen haben. 
 * Sie können „N“ wählen, um die Kalibrierungswerte beizubehalten. ''',
    'btnUpdateMode': 'Aktualisieren Sie nur den Modus',
    'tipUpdateMode': ''' Wenn Sie die Firmware nach einem erneuten Download mindestens einmal aktualisiert haben, 
 Es ist schneller, nur die Modi zu wechseln, ohne die Parameter zu aktualisieren. ''',
    'Warning': 'Warnung',
    'Uploading': 'Hochladen ',
    'is successully uploaded': ' erfolgreich hochgeladen',
    'failed to upload': ' konnte nicht hochgeladen werden',
    'Need to manually select the model type (Nybble/Bittle)': 'Sie müssen den Modelltyp manuell auswählen '
                                                              '(Nybble/Bittle)',
    'msgFileDir': 'Bitte wählen Sie das Freigabe-Verzeichnis!',
    'msgPort': 'Bitte wählen Sie die korrekte serielle Schnittstelle!',

    'msgNoneAvrdude': '''Es gibt kein Avrdude. Bitte installieren Sie zuerst avrdude! Einzelheiten finden Sie unter :
    https://docs.petoi.com/desktop-app/firmware-uploader#install-avrdude-in-the-linux-os''',

    'titleVersion': 'Versionsinformation',

    'msgVersion': 'Version: ' + versionNum + '\n' +
                  '''Firmware-Uploader für OpenCat
    Copyright © 2018-2023
    Alle Rechte vorbehalten
    Petoi LLC
    https://www.petoi.com\n''' + dateStr,

    'reset joints?': 'Gelenkabweichungen zurücksetzen? (J/N)',
    'reseting joints': 'Gelenkabweichungen werden zurückgesetzt...',
    'joints reset': 'Gelenkabweichungen erfolgreich zurückgesetzt!',

    'update instincts?': 'Instinkte aktualisieren? (J/n)',
    'updating instincts': 'Instinkte werden aktualisiert...',
    'instincts updated': 'Instinkte aktualisiert',

    'calibrate IMU?': '''IMU kalibrieren? (J/N)
    Hinweis: Legen Sie das Mainboard FLACH auf einen Tisch!''',
    'calibrating IMU': 'IMU wird kalibriert...',
    'IMU calibrated': 'IMU erfolgreich kalibriert!',

    'parameterFinish': '''Parameter initialisiert!
    Der nächste Schritt ist das Hochladen der Hauptfunktion!''',
    '9685 Calibrated': 'PCA9685 wurde erfolgreich kalibriert!',
    'msgFinish': 'Firmware-Hochladen abgeschlossen!',
    'msgMode': 'Ungültig, bitte wählen Sie einen anderen Modus!',

    'Standard': 'Standard',
    'RandomMind': 'Zufallsmodus',
    'Ultrasonic': 'Ultraschall-Modus',
    'Voice': 'Sprachmodus',
    'Camera': 'Kamera',
    'Mind+': 'Mind+',
    'RandomMind_Ultrasonic': 'Zufallsmodus_Ultraschall',

    'Breath': 'Atmen',
    'Rotate': 'Drehen',
    'Flash': 'Blitzen',
    'Meow': 'Miauen',

    'labEdit': 'Bearbeiten',
    'labTheme': 'Thema',
    # '':'',
    'tipConnect': 'Aktive serielle Verbindungen aktualisieren,\nbis diese deaktiviert ist',
    'tipPortMenu': 'Steuerung einzelner oder aller Geräte',
    'tipServo': 'Servos aktivieren/deaktivieren',
    'tipGyro': 'Gyroskop aktivieren/deaktivieren',
    'tipRandom': 'Zufallsverhalten aktivieren/deaktivieren\n*',
    'tipBinder': 'Mit anderen Gelenken verbinden',
    'tipRevBinder': 'Umgekehrt mit anderen Gelenken verbinden',
    'tipPlay': 'Gehe durch den Ablaufplan des aktiven Frames\nDas Abspielen kann jederzeit gestoppt werden',
    'tipImport': 'Fähigkeiten aus Dateien oder Texten importieren',
    'tipRestart': 'Lösche alle Frames im Ablaufplan!',
    'tipExport': 'Die Fähigkeit wird in Echtzeit gesendet und\nim statischen Speicher des Roboters gespeichert\n'
                 'Verwenden Sie den seriellen Token \'T\', um die zuletzt gesendete Fähigkeit aufzurufen',
    'tipMirror': 'Spiegeln des aktuellen Frames',
    'tipMirrorXport': 'Spiegeln der gesamten Fähigkeit beim Exportieren\n'
                      '* Wirksam beim Exportieren der gesamten Fähigkeit',
    'tipGorB': 'Ein Verhalten interpoliert zwischen den Keyframes und wird nur einmal ausgeführt.\n'
               'Ein Gang durchläuft alle Frames ohne Glättung.',
    'tipLoop': 'Setze Start- und Endframes für die Schleife\n* Wirksam beim Exportieren der gesamten Fähigkeit',
    'tipRepeat': 'Geben Sie die Anzahl der Schleifen ein\n-1 für unendliche Schleife. Nur die "Reset"-Taste kann die '
                 'Schleife unterbrechen!\n* Wirksam beim Exportieren der gesamten Fähigkeit',
    'tipSet': 'Springe zu/speichere den aktuellen Frame',
    'tipStep': 'Einheit: Grad/Schritt\n* Wirksam beim Exportieren der gesamten Fähigkeit',
    'tipDelay': 'Einheit: Millisekunde\nVerzögerung nach dem aktuellen Frame, bevor der nächste Frame betreten wird.\n'
                'Wenn der Auslöser gültig ist, beginnt die Verzögerung nach dem Auslöser\n* Wirksam beim Exportieren'
                ' der gesamten Fähigkeit',
    'tipTrig': 'Trigger den nächsten Frame nur, wenn der Körper\nin eine bestimmte Richtung über den Auslösewinkel '
               'rollt\n* Wirksam beim Exportieren der gesamten Fähigkeit',
    'tipTrigAngle': 'Der kritische Winkel um auszulösen',
    'tipNote': 'Gib dem Frame einen einfach zu merkenden Namen',
    'tipAdd': 'Kopiere den aktiven Frame und\nfüge ihn in die nächste Zeile ein',
    'tipDel': 'Lösche den aktuellen Frame',
    'tipImgWiring': 'Achte auf den Standort und die Ausrichtung der Servostecker\nHalte die Taste des Akkus lange '
                    'gedrückt, um die Stromversorgung einzuschalten\nKlicke auf "Kalibrieren", um alle Servos in den '
                    'Kalibrierungsmodus zu drehen\nBefestige die Beine und den Kopf senkrecht\nVerwende den '
                    'Schieberegler, um die Kanten der Beine und der Referenzskala parallel auszurichten',
    'tipImgPosture': 'Wechsle zwischen Haltungen, um die Kalibrierungsergebnisse zu testen\nSpeichere die Abweichungen '
                     'rechtzeitig\nKeine Notwendigkeit für zukünftige Kalibrierung',
}

textTH = {
    'lan': 'Thai',  # 'ภาษาไทย'
    'lanOption': 'ภาษาไทย',
    'lanMenu': 'ภาษา',
    'uiTitle': 'แอพพลิเคชั่น Petoi Desktop',
    'calibTitle': 'การปรับสอดคล้องข้อต่อ',
    'skillComposerTitle': 'คอมโพเซอร์ Petoi Skill สำหรับ OpenCat',
    'Model': 'รุ่น',
    'Utility': 'ยูทิลิตี้',
    'Joint Calibrator': 'การปรับสอดคล้องข้อต่อ',
    'Skill Composer': 'คอมโพเซอร์สกิล',
    'Task Scheduler': 'ตัวจัดตารางงาน',
    'Scheduler': 'ตัวจัดตาราง',
    'Firmware Uploader': 'ตัวอัปโหลดเฟิร์มแวร์',
    'Eye color picker': 'ตัวเลือกสีตา',
    'Creator Information': 'ข้อมูลผู้สร้าง',
    'Creator': 'ผู้สร้าง',
    'Location': 'ที่ตั้ง',
    'Nature': 'ธรรมชาติ',
    'Earth': 'โลก',
    'InputCreator': 'กรุณาใส่ชื่อเล่นของผู้สร้าง',
    'InputLocation': 'โปรดป้อนตำแหน่งของผู้สร้าง',
    'Exit': 'ออก',
    'Help': 'วิธีใช้',
    'About': 'เกี่ยวกับ',
    'Repeat': 'ทำซ้ำ',
    'Loop': 'วนซ้ำ',
    'Frame': 'เฟรม',
    'Step': 'ขั้นตอน',
    'Delay': 'ความล่าช้า',
    'Trig': 'ตัวกระตุ้น',
    'Angle': 'มุม',
    'Note': 'บันทึก',
    'Del': 'ลบ',
    'Add': 'เพิ่ม',
    'Set': 'ตั้งค่า',
    'Save': 'บันทึก',
    'Stop': 'หยุด',
    'Joint Controller': 'ตัวควบคุมข้อต่อ',
    'Unbind All': 'ยกเลิกการผูกทั้งหมด',
    'Yaw': 'หันเห',
    'Pitch': 'ขว้าง',
    '-Pitch': '-ขว้าง',
    'Roll': 'ม้วน',
    '-Roll': '-ม้วน',
    'Spinal': 'ระดับกระดูกสันหลัง',
    'Height': 'ความสูง',
    'Sideway': 'ด้านข้าง',
    'Head Pan': 'หมุนศีรษะ',
    'Head Tilt': 'เอียงศีรษะ',
    'Tail Pan': 'หมุนหาง',
    'N/A': 'N/A',
    'Left Front': 'ด้านหน้าซ้าย',
    'Right Front': 'ด้านหน้าขวา',
    'Right Back': 'ด้านหลังขวา',
    'Left Back': 'ด้านหลังซ้าย',
    'Shoulder': 'ไหล่',
    'Arm': 'แขน',
    'Knee': 'เข่า',
    'State Dials': 'ปุ่มควบคุมสถานะ',
    'Connect': 'เชื่อมต่อ',
    'Connected': 'เชื่อมต่อแล้ว',
    'Listening': 'กำลังฟัง',
    'All': 'ทั้งหมด',
    'None': 'ไม่มี',
    'Servo': 'เซอร์โว',
    'Gyro': 'ไจโรสโคป',
    'Random': 'สุ่ม',
    'Send': 'ส่ง',
    'Postures': 'ท่าทางที่ตั้งค่าไว้',
    'Skill Editor': 'ตัวแก้ไขสกิล',
    'Play': 'เล่น',
    'Pause': 'หยุดชั่วคราว',
    'Import': 'นำเข้า',
    'Restart': 'เริ่มใหม่',
    'Export': 'ส่งออก',
    'Undo': 'ยกเลิก',
    'Redo': 'ทำซ้ำ',
    'Open File': 'เปิดไฟล์',
    'Cancel': 'ยกเลิก',
    'OK': 'ตกลง',
    'Refresh': "รีเฟรช",
    'Multiple': 'หลายตัว',
    'Skill List': 'รายการสกิล',
    'Type of skill': 'ประเภทของสกิล',
    'Name of skill': 'ชื่อของสกิล',
    'exampleFormat': 'นำเข้าจากไฟล์หรือคัดลอกและวางข้อมูลสกิลจาก '
                     'instinct.h ในรูปแบบต่อไปนี้\n* ให้คงเครื่องหมายวงเล็บปีกกา!',
    'Quit': 'ออก',
    'Do you want to quit?': 'คุณต้องการออกหรือไม่?',
    'mirror': ' สะท้อนทั้งหมด',
    '>|<': '>|<',
    'Posture': ' ท่าทาง',
    'Gait': ' รูปแบบการเดิน',
    'Behavior': ' พฤติกรรม',
    'Clear': 'ล้าง',
    'max': 'สูงสุด',

    'Manual mode': 'โหมดแมนนวล',
    'Replug mode': 'โหมดเสียบปลั๊ก',
    'Replug prompt': '''คำเตือน: การอัปโหลดล้มเหลว!\n\n
* ถ้าเมนบอร์ดไม่ได้เชื่อมต่อกับคอมพิวเตอร์:\n
คลิกปุ่มด้านล่าง ต่อสาย USB เข้ากับเมนบอร์ด จากนั้นเสียบปลายอีกด้านเข้ากับคอมพิวเตอร์\n\n
* หากเมนบอร์ดเชื่อมต่อกับคอมพิวเตอร์ผ่านสาย USB อยู่แล้ว:\n
1. ยืนยันว่าคอมพิวเตอร์ของคุณสามารถรู้จักอุปกรณ์ USB ได้\n
ดูรายละเอียดเพิ่มเติมได้ที่ https://docs.petoi.com/upload-firmware.\n
2. หลังจากคลิกปุ่มด้านล่าง ให้ถอดสาย USB จากฝั่งคอมพิวเตอร์ แล้วเสียบกลับเข้าไปใหม่
''',
    'Confirm': 'ยืนยัน',
    'Counting down to manual mode: ': 'นับถอยหลังสู่โหมดแมนนวล: ',
    'Info': 'ข้อมูล',
    'New port prompt': 'ค้นพบอุปกรณ์ USB ใหม่: ',
    'Please select the port from the list': 'โปรดเลือกพอร์ตจากรายการ',
    '* Port ': '* ท่าเรือ ',
    ' cannot be opened': ' ไม่สามารถเปิดได้',

    'Calibrate': 'ปรับสอดคล้อง',
    'Rest': 'พัก',
    'Stand Up': 'ยืนขึ้น',
    'Walk': 'เดิน',
    'Abort': 'ยกเลิก',
    'Do you want to save the offsets?': 'คุณต้องการบันทึกการปรับเทียบหรือไม่?',
    'uploaderTitle': 'ตัวอัปโหลดเฟิร์มแวร์',
    'labTrans': 'เปลี่ยนภาษา',
    'labChi': 'จีน',
    'labEng': 'อังกฤษ',
    'labHelp': 'ช่วยเสนอ',
    'labAbout': 'เกี่ยวกับ',
    'labExit': 'ออก',
    'labFileDir': 'เลือกโฟลเดอร์ปล่อย',
    'btnFileDir': '...',
    'titleFileDir': 'โปรดเลือกโฟลเดอร์ปล่อย',
    'labPort': 'ซีเรียลพอร์ต',
    'labSoftwareVersion': 'เวอร์ชันซอฟต์แวร์',
    'labBoardVersion': 'เวอร์ชันบอร์ด',
    'labProduct': 'ผลิตภัณฑ์',
    'labMode': 'โหมด',
    'rbnWalk': 'เดิน',
    'rbnUltrasonic': 'อัลตราโซนิก',
    'rbnCamera': 'กล้อง',
    'Parameters': 'พารามิเตอร์',
    'Main function': 'ฟังก์ชั่นหลัก',
    'btnFacReset': 'รีเซ็ตเป็นค่าเริ่มต้นจากโรงงาน',
    'tipFacReset': ''' หลังจากการรีเซ็ตเป็นค่าเริ่มต้นจากโรงงาน คุณต้องทำการปรับเทียบร่วม โปรดดูที่: 
 https://docs.petoi.com/joint-calibration ''',
    'btnUpgrade': 'อัพเกรดเฟิร์มแวร์',
    'tipUpgrade': ''' อัปเกรดทั้งพารามิเตอร์และฟังก์ชันหลัก 
 * จำเป็นหากคุณเพิ่งดาวน์โหลดเวอร์ชันใหม่ของซอฟต์แวร์นี้ 
 * คุณสามารถเลือก 'N' เพื่อรักษาค่าการสอบเทียบ ''',
    'btnUpdateMode': 'อัปเดตโหมดเท่านั้น',
    'tipUpdateMode': ''' หากคุณได้อัปเกรดเฟิร์มแวร์อย่างน้อยหนึ่งครั้งหลังจากดาวน์โหลดใหม่ 
 การสลับโหมดเพียงอย่างเดียวโดยไม่รีเฟรชพารามิเตอร์จะเร็วกว่า ''',
    'Warning': 'คำเตือน',
    'Uploading': 'กำลังอัพโหลด',
    'is successully uploaded': ' อัพโหลดสำเร็จ',
    'failed to upload': ' ไม่สามารถอัพโหลด',
    'Need to manually select the model type (Nybble/Bittle)': 'ต้องเลือกประเภทรุ่นด้วยตนเอง (Nybble/Bittle)',
    'msgFileDir': 'โปรดเลือกโฟลเดอร์ปล่อย!',
    'msgPort': 'โปรดเลือกพอร์ตอนุกรมที่ถูกต้อง!',

    'msgNoneAvrdude': '''ไม่มี avrdude โปรดติดตั้ง avrdude ในตอนแรก! สำหรับรายละเอียด โปรดดูที่:
    https://docs.petoi.com/desktop-app/firmware-uploader#install-avrdude-in-the-linux-os''',

    'titleVersion': 'ข้อมูลเวอร์ชัน',

    'msgVersion': 'เวอร์ชัน: ' + versionNum + '\n' +
                  '''เครื่องมืออัพโหลดเฟิร์มแวร์สำหรับ OpenCat
    ลิขสิทธิ์ ©  2018-2023
    สงวนลิขสิทธิ์ทั้งหมด Petoi LLC
    https://www.petoi.com\n''' + dateStr,

    'reset joints?': 'ตั้งค่าเทียบข้อต่อใหม่หรือไม่? (Y/N)',
    'reseting joints': 'กำลังตั้งค่าเทียบข้อต่อใหม่...',
    'joints reset': 'ตั้งค่าเทียบข้อต่อใหม่เสร็จสมบูรณ์!',

    'update instincts?': 'อัปเดตตัวอย่างหรือไม่? (Y/N)',
    'updating instincts': 'กำลังอัปเดตตัวอย่าง...',
    'instincts updated': 'อัปเดตตัวอย่างแล้ว',

    'calibrate IMU?': '''ต้องการปรับแต่ง IMU หรือไม่? (Y/N)
    หมายเหตุ: วางเมนบอร์ดให้ราบไปกับบนโต๊ะ!''',
    'calibrating IMU': 'กำลังปรับแต่ง IMU...',
    'IMU calibrated': 'ปรับแต่ง IMU เสร็จสมบูรณ์!',

    'parameterFinish': '''ตั้งค่าพารามิเตอร์เสร็จแล้ว!
     ขั้นตอนถัดไปคือการโหลดฟังก์ชันหลัก!''',
    '9685 Calibrated': 'PCA9685 ได้รับการปรับเทียบเรียบร้อยแล้ว!',
    'msgFinish': 'การโหลดเฟิร์มแวร์เสร็จสมบูรณ์!',
    'msgMode': 'ไม่ถูกต้อง โปรดเลือกโหมดอื่น!',

    'Standard': 'มาตรฐาน',
    'RandomMind': 'จิตใจสุ่ม',
    'Ultrasonic': 'อัลตราโซนิก',
    'Voice': 'เสียง',
    'Camera': 'กล้อง',
    'Mind+': 'Mind+',
    'RandomMind_Ultrasonic': 'จิตใจสุ่ม_อัลตราโซนิก',

    'Breath': 'หายใจ',
    'Rotate': 'หมุน',
    'Flash': 'รวดเร็ว',
    'Meow': 'เหมียว',

    'labEdit': 'แก้ไข',
    'labTheme': 'ธีม',
    # '':'',
    'tipConnect': 'อัปเดตพอร์ตอนุกรมที่เชื่อมต่ออยู่\nจนกว่าจะปิดใช้งาน',
    'tipPortMenu': 'ควบคุมอุปกรณ์เดียวหรือทั้งหมด',
    'tipServo': 'เปิด/ปิดเซอร์โว',
    'tipGyro': 'เปิด/ปิดไจโรสโคป',
    'tipRandom': 'เปิด/ปิดพฤติกรรมสุ่ม\n* ในบางโหมด',
    'tipBinder': 'ผูกกับข้อต่ออื่น ๆ',
    'tipRevBinder': 'ผูกกับข้อต่ออื่น ๆ อย่างตรงข้าม',
    'tipPlay': 'เล่นตารางงานจากเฟรมที่ใช้งานอยู่\nคุณสามารถหยุดขณะเล่น',
    'tipImport': 'นำเข้าทักษะจากไฟล์หรือข้อความ',
    'tipRestart': 'ล้างเฟรมทั้งหมดในตารางงาน!',
    'tipExport': 'ทักษะจะถูกส่งและบันทึก\nในหน่วยความจำสถิติของหุ่นยนต์\n'
                 'ใช้โทเค็นอนุกรม \'T\' เพื่อเรียกความสามารถสุดท้ายที่ถูกส่ง',
    'tipMirror': 'สะท้อนเฟรมปัจจุบัน',
    'tipMirrorXport': 'สะท้อนทักษะทั้งหมดขณะส่งออก\n* มีประสิทธิภาพเมื่อส่งออกทักษะทั้งหมด',
    'tipGorB': 'พฤติกรรมทำการเชื่อมต่อระหว่างเฟรมคีย์และเล่นเพียงครั้งเดียว\n'
               'การเดินที่ไหลไปทั้งหมดโดยไม่มีการปรับเรียบ',
    'tipLoop': 'ตั้งค่าเฟรมเริ่มต้นและสิ้นสุดสำหรับลูป\n* มีประสิทธิภาพเมื่อส่งออกทักษะทั้งหมด',
    'tipRepeat': 'ป้อนจำนวนลูป\n-1 สำหรับลูปไม่จำกัด ปุ่ม "รีเซ็ต" เท่านั้นที่สามารถหยุดลูป!\n'
                 '* มีประสิทธิภาพเมื่อส่งออกทักษะทั้งหมด',
    'tipSet': 'เปลี่ยนไปยัง/บันทึกเฟรมปัจจุบัน',
    'tipStep': 'หน่วย: องศา/ก้าว\n* มีประสิทธิภาพเมื่อส่งออกทักษะทั้งหมด',
    'tipDelay': 'หน่วย: มิลลิวินาที\nหน่วยเวลาหลังจากเฟรมปัจจุบัน ก่อนเข้าสู่เฟรมถัดไป\n'
                'หากตัวกระตุ้นถูกต้อง ความล่าช้าเริ่มหลังจากตัวกระตุ้น\n* มีประสิทธิภาพเมื่อส่งออกทักษะทั้งหมด',
    'tipTrig': 'เปิดใช้งานเฟรมถัดไปเมื่อตัวหุ่นยนต์หมุน\n'
               'เกินมุมที่กำหนดในทิศทางที่กำหนด\n* มีประสิทธิภาพเมื่อส่งออกทักษะทั้งหมด',
    'tipTrigAngle': 'มุมวิกฤติสำหรับตัวกระตุ้น\n* มีประสิทธิภาพเมื่อส่งออกทักษะทั้งหมด',
    'tipNote': 'ตั้งชื่อเฟรมให้ง่ายต่อการจำ',
    'tipAdd': 'คัดลอกเฟรมที่ใช้งานอยู่และ\nแทรกลงในแถวถัดไป',
    'tipDel': 'ลบเฟรมปัจจุบัน',

    'tipImgWiring': 'ระมัดระวังตำแหน่งและทิศทางของตัวเชื่อมต่อเซอร์โว\n'
                    'กดปุ่มแบตเตอรี่นานเพื่อเปิดเครื่อง\nคลิก "ปรับสอบ" '
                    'เพื่อหมุนเซอร์โวทั้งหมดให้อยู่ในสถานะการปรับสอบ\n'
                    'ติดตั้งขาและหัวให้ตั้งฉาก\nใช้ตัวเลื่อนเพื่อปรับขอบขาให้สอดคล้องกันและตัวชี้วัดอ้างอิง',
    'tipImgPosture': 'สลับระหว่างท่าทางต่าง ๆ เพื่อทดสอบผลการปรับสอบ\n'
                     'บันทึกค่าออฟเซ็ตในเวลาจริง\nไม่จำเป็นต้องปรับสอบในอนาคต',
}

textFR = {
    'lan': 'French',
    'lanOption': 'Français',
    'lanMenu': 'Langue',
    'uiTitle': 'Application Petoi pour ordinateur de bureau',
    'calibTitle': 'Calibrateur d\'articulation',
    'skillComposerTitle': 'Compositeur de compétences Petoi pour OpenCat',
    'Model': 'Modèle',
    'Utility': 'Utilitaire',
    'Joint Calibrator': 'Calibrateur d\'articulation',
    'Skill Composer': 'Compositeur de compétences',
    'Task Scheduler': 'Planificateur de tâches',
    'Scheduler': 'Planificateur',
    'Firmware Uploader': 'Chargeur de firmware',
    'Eye color picker': 'Sélecteur de couleur des yeux',
    'Creator Information': 'Informations sur le créateur',
    'Creator': 'Créateur',
    'Location': 'Emplacement',
    'Nature': 'Nature',
    'Earth': 'Terre',
    'InputCreator': 'Veuillez saisir le pseudo du créateur',
    'InputLocation': 'Veuillez saisir l\'emplacement du créateur',
    'Exit': 'Quitter',
    'Help': 'Aide',
    'About': 'À propos',
    'Repeat': 'Répéter',
    'Loop': 'Boucle',
    'Frame': 'Image',
    'Step': 'Pas',
    'Delay': 'Délai',
    'Trig': 'Déclencheur',
    'Angle': 'Angle',
    'Note': 'Note',
    'Del': 'Supprimer',
    'Add': 'Ajouter',
    'Set': 'Définir',
    'Save': 'Enregistrer',
    'Stop': 'Arrêter',
    'Joint Controller': 'Contrôleur d\'articulation',
    'Unbind All': 'Détacher tout',
    'Yaw': 'Lacet',
    'Pitch': 'Tangage',
    '-Pitch': '-Tangage',
    'Roll': 'Roulis',
    '-Roll': '-Roulis',
    'Spinal': 'Spinal',
    'Height': 'Hauteur',
    'Sideway': 'Côté',
    'Head Pan': 'Rotation de la tête',
    'Head Tilt': 'Inclinaison de la tête',
    'Tail Pan': 'Rotation de la queue',
    'N/A': 'N/A',
    'Left Front': 'Avant gauche',
    'Right Front': 'Avant droit',
    'Right Back': 'Arrière droit',
    'Left Back': 'Arrière gauche',
    'Shoulder': 'Épaule',
    'Arm': 'Bras',
    'Knee': 'Genou',
    'State Dials': 'Indicateurs d\'état',
    'Connect': 'Connecter',
    'Connected': 'Connecté',
    'Listening': 'Écoute',
    'All': 'Tout',
    'None': 'Aucun',
    'Servo': 'Servo',
    'Gyro': 'Gyro',
    'Random': 'Aléatoire',
    'Send': 'Envoyer',
    'Postures': 'Postures prédéfinies',
    'Skill Editor': 'Éditeur de compétences',
    'Play': 'Lecture',
    'Pause': 'Pause',
    'Import': 'Importer',
    'Restart': 'Redémarrer',
    'Export': 'Exporter',
    'Undo': 'Annuler',
    'Redo': 'Rétablir',
    'Open File': 'Ouvrir un fichier',
    'Cancel': 'Annuler',
    'OK': 'OK',
    'Refresh': 'Actualiser',
    'Multiple': 'Multiple',
    'Skill List': 'Liste de compétences',
    'Type of skill': 'Type de compétence',
    'Name of skill': 'Nom de la compétence',
    'exampleFormat': 'Importer depuis des fichiers ou copier et coller les données de compétence à partir de instinct.h'
                     ' dans le format suivant.\n* Conserver les accolades !',
    'Quit': 'Quitter',
    'Do you want to quit?': 'Voulez-vous quitter ?',
    'mirror': ' Tout inverser',
    '>|<': '>|<',
    'Posture': ' Posture',
    'Gait': ' Démarche',
    'Behavior': ' Comportement',
    'Clear': 'Effacer',
    'max': 'max',

    'Manual mode': 'Mode manuel',
    'Replug mode': 'Mode Replug',
    'Replug prompt': '''AVERTISSEMENT : Échec de la connexion !

* Si la carte principale N'EST PAS connectée à l'ordinateur :
Cliquez sur le bouton ci-dessous. Connectez le câble USB à la carte principale, puis branchez l'autre extrémité sur 
l'ORDINATEUR.
* Si la carte principale est déjà connectée à l'ordinateur via un câble USB :
1. Confirmez que votre ordinateur peut reconnaître le périphérique USB.
Vous trouverez plus de détails à l'adresse https://docs.petoi.com/upload-firmware
2. Après avoir cliqué sur le bouton ci-dessous, débranchez le câble USB du côté de l'ORDINATEUR, puis rebranchez-le.
''',
    'Confirm': 'Confirmer',
    'Counting down to manual mode: ': 'Compte à rebours jusqu\'au mode manuel : ',
    'Info': 'Info',
    'New port prompt': 'Découverte d\'un nouveau périphérique USB : ',
    'Please select the port from the list': 'Veuillez sélectionner le port dans la liste',
    '* Port ': '* Port ',
    ' cannot be opened': ' ne peut pas être ouvert',

    'Calibrate': 'Calibrer',
    'Rest': 'Repos',
    'Stand Up': 'Se lever',
    'Walk': 'Marcher',
    'Abort': 'Annuler',
    'Do you want to save the offsets?': 'Voulez-vous enregistrer les décalages ?',
    'uploaderTitle': 'Assistant de mise à jour du micrologiciel',
    'labTrans': 'Changer de langue',
    'labChi': 'Chinois',
    'labEng': 'Anglais',
    'labHelp': 'Aide',
    'labAbout': 'À propos',
    'labExit': 'Quitter',
    'labFileDir': 'Choisir le dossier de la version',
    'btnFileDir': '...',
    'titleFileDir': 'Veuillez choisir le dossier de la version',
    'labPort': 'Port série',
    'labSoftwareVersion': 'Version du logiciel',
    'labBoardVersion': 'Version de la carte',
    'labProduct': 'Produit',
    'labMode': 'Mode',
    'rbnWalk': 'Marcher',
    'rbnUltrasonic': 'Ultrasons',
    'rbnCamera': 'Caméra',
    'Parameters': 'Paramètres',
    'Main function': 'Fonction principale',
    'btnFacReset': 'Réinitialisation d\'usine',
    'tipFacReset': ''' Après la réinitialisation d'usine, vous devrez effectuer l'étalonnage des articulations. Veuillez
     vous référer à :
     https://docs.petoi.com/joint-calibration ''',
    'btnUpgrade': 'Mettre à jour le micrologiciel',
    'tipUpgrade': ''' Met à jour à la fois les paramètres et la fonction principale.
     * Obligatoire si vous venez de télécharger une nouvelle version de ce logiciel.
     * Vous pouvez sélectionner 'N' pour conserver les valeurs d'étalonnage. ''',
    'btnUpdateMode': 'Mettre à jour uniquement le mode',
    'tipUpdateMode': ''' Si vous avez déjà mis à jour le micrologiciel au moins une fois après un nouveau 
    téléchargement,     il est plus rapide de simplement passer d'un mode à l'autre sans rafraîchir les paramètres. ''',
    'Warning': 'Avertissement',
    'Uploading': 'Téléchargement en cours ',
    'is successully uploaded': ' a été téléchargé avec succès',
    'failed to upload': ' n\'a pas pu être téléchargé',
    'Need to manually select the model type (Nybble/Bittle)': 'Vous devez sélectionner manuellement le type de modèle '
                                                              '(Nybble/Bittle)',
    'msgFileDir': 'Veuillez choisir le dossier de la version !',
    'msgPort': 'Veuillez choisir le port série correct !',

    'msgNoneAvrdude': '''Avrdude n'est pas installé. Veuillez d'abord installer avrdude ! Pour plus de détails, 
    veuillez consulter : https://docs.petoi.com/desktop-app/firmware-uploader#install-avrdude-in-the-linux-os''',

    'title Version': 'Informations sur la version',
    'msgVersion': 'Version : ' + versionNum + '\n' +
                  '''Outil de téléchargement du micrologiciel pour OpenCat
    Copyright © 2018-2023
    Tous droits réservés Petoi LLC
    https://www.petoi.com\n''' + dateStr,

    'reset joints?': 'Réinitialiser les décalages des articulations ? (O/N)',
    'reseting joints': 'Réinitialisation des décalages des articulations en cours...',
    'joints reset': 'Réinitialisation des décalages des articulations terminée !',

    'update instincts?': 'Mettre à jour les instincts ? (O/N)',
    'updating instincts': 'Mise à jour des instincts en cours...',
    'instincts updated': 'Instincts mis à jour',

    'calibrate IMU?': '''Calibrer l'IMU ? (O/N)
        Remarque : Placez la carte principale À PLAT sur une table !''',
    'calibrating IMU': 'Calibration de l\'IMU en cours...',
    'IMU calibrated': 'Calibration de l\'IMU terminée !',
    'parameterFinish': '''Paramètres initialisés !
     La prochaine étape consiste à télécharger la Fonction Principale !''',
    '9685 Calibrated': 'PCA9685 a été calibré avec succès !',
    'msgFinish': 'Téléchargement du micrologiciel terminé !',
    'msgMode': 'Mode invalide, veuillez sélectionner un autre mode !',

    'Standard': 'Standard',
    'RandomMind': 'RandomMind',
    'Ultrasonic': 'Ultrason',
    'Voice': 'Voix',
    'Camera': 'Caméra',
    'Mind+': 'Mind+',
    'RandomMind_Ultrasonic': 'RandomMind_Ultrasonic',

    'Breath': 'Respiration',
    'Rotate': 'Rotation',
    'Flash': 'Flash',
    'Meow': 'Miaulement',

    'labEdit': 'Modifier',
    'labTheme': 'Thème',
    'tipConnect': 'Continuer à mettre à jour les ports série actifs jusqu\'à ce qu\'ils soient désactivés',
    'tipPortMenu': 'Contrôler un seul ou tous les appareils',
    'tipServo': 'Activer/désactiver les servomoteurs',
    'tipGyro': 'Activer/désactiver le gyroscope',
    'tipRandom': 'Activer/désactiver les comportements aléatoires\n* dans certains modes',
    'tipBinder': 'Lier à d\'autres articulations',
    'tipRevBinder': 'Lier de manière réversible à d\'autres articulations',
    'tipPlay': 'Parcourir l\'ordonnanceur à partir de la trame active\nVous pouvez vous arrêter en cours de lecture',
    'tipImport': 'Importer des compétences à partir de fichiers ou de textes',
    'tipRestart': 'Effacer toutes les trames de l\'ordonnanceur !',
    'tipExport': 'La compétence sera envoyée en temps réel et enregistrée\ndans la mémoire statique du '
                 'robot\nUtilisez le jeton série \'T\' pour appeler la dernière compétence envoyée',
    'tipMirror': 'Miroir de la trame actuelle',
    'tipMirrorXport': 'Miroir de toute la compétence lors de l\'exportation\n* Efficace lors de l\'exportation de la '
                      'compétence complète',
    'tipGorB': 'Un comportement interpole entre les trames clés et s\'exécute une seule fois\nUne démarche parcourt '
               'toutes les trames sans lissage',
    'tipLoop': 'Définir les trames de départ et de fin pour la boucle\n* Efficace lors de l\'exportation de la'
               'compétence complète',
    'tipRepeat': 'Entrez le nombre de boucles\n-1 pour une boucle infinie. Seul le bouton "réinitialiser" peut '
                 'interrompre la boucle !\n* Efficace lors de l\'exportation de la compétence complète',
    'tipSet': 'Aller à/sauvegarder la trame actuelle',
    'tipStep': 'Unité : degré/pas\n* Efficace lors de l\'exportation de la compétence complète',
    'tipDelay': 'Unité : milliseconde\nDélai après la trame actuelle, avant de passer à la trame suivante\nSi la'
                'gâchette est valide, le délai commence après la gâchette\n* Efficace lors de l\'exportation de la '
                'compétence complète',
    'tipTrig': 'Déclenche la trame suivante uniquement lorsque le corps roule\nau-dessus de l\'angle de déclenchement '
               'dans une certaine direction\n* Efficace lors de l\'exportation de la compétence complète',
    'tipTrigAngle': 'L\'angle critique pour la gâchette\n* Efficace lors de l\'exportation de la compétence complète',
    'tipNote': 'Donnez un nom facile à retenir à la trame',
    'tipAdd': 'Copier la trame active et\nl\'insérer dans la ligne suivante',
    'tipDel': 'Supprimer la trame actuelle',

    'tipImgWiring': 'Faites attention à l\'emplacement et à la direction des prises de servomoteur\nMaintenez le'
                    'bouton de la batterie enfoncé pour allumer l\'alimentation\nCliquez sur "Calibrer" pour faire '
                    'tourner tous les servomoteurs à l\'état de calibration\nFixez les jambes et la tête '
                    'perpendiculairement\nUtilisez le curseur pour aligner les bords des jambes et la règle de '
                    'référence parallèlement',
    'tipImgPosture': 'Basculez entre les postures pour tester les résultats de calibration\nEnregistrez les offsets à '
                     'temps\nAucune calibration nécessaire à l\'avenir',
}

textJP = {
    'lan': 'Japanese',
    'lanOption': '日本語',
    'lanMenu': '言語',
    'uiTitle': 'Petoiデスクトップアプリ',
    'calibTitle': 'ジョイントキャリブレータ',
    'skillComposerTitle': 'OpenCatのためのPetoiスキルコンポーザー',
    'Model': 'モデル',
    'Utility': 'ユーティリティ',
    'Joint Calibrator': 'ジョイントキャリブレータ',
    'Skill Composer': 'スキルコンポーザ',
    'Task Scheduler': 'タスクスケジューラ',
    'Scheduler': 'スケジューラ',
    'Firmware Uploader': 'ファームウェアアップローダ',
    'Eye color picker': '目の色選択',
    'Creator Information': '制作者情報',
    'Creator': '制作者',
    'Location': '場所',
    'Nature': '自然',
    'Earth': '地球',
    'InputCreator': '作成者のニックネームを入力してください',
    'InputLocation': '作成者の所在地を入力してください',
    'Exit': '終了',
    'Help': 'ヘルプ',
    'About': 'について',
    'Repeat': 'リピート',
    'Loop': 'ループ',
    'Frame': 'フレーム',
    'Step': 'ステップ',
    'Delay': '遅延',
    'Trig': 'トリガー',
    'Angle': '角度',
    'Note': 'ノート',
    'Del': '削除',
    'Add': '追加',
    'Set': '設定',
    'Save': '保存',
    'Stop': '停止',
    'Joint Controller': 'ジョイントコントローラ',
    'Unbind All': 'すべてのバインドを解除',
    'Yaw': 'ヨー',
    'Pitch': 'ピッチ',
    '-Pitch': '-ピッチ',
    'Roll': 'ロール',
    '-Roll': '-ロール',
    'Spinal': '脊椎',
    'Height': '高さ',
    'Sideway': '横',
    'Head Pan': 'ヘッドパン',
    'Head Tilt': 'ヘッドチルト',
    'Tail Pan': 'テールパン',
    'N/A': 'N/A',
    'Left Front': '左前',
    'Right Front': '右前',
    'Right Back': '右後',
    'Left Back': '左後',
    'Shoulder': '肩',
    'Arm': 'アーム',
    'Knee': '膝',
    'State Dials': 'ステートダイヤル',
    'Connect': '接続',
    'Connected': '接続済み',
    'Listening': 'リスニング',
    'All': 'すべて',
    'None': 'なし',
    'Servo': 'サーボ',
    'Gyro': 'ジャイロ',
    'Random': 'ランダム',
    'Send': '送信',
    'Postures': 'プリセットポーズ',
    'Skill Editor': 'スキルエディタ',
    'Play': '再生',
    'Pause': '一時停止',
    'Import': 'インポート',
    'Restart': '再起動',
    'Export': 'エクスポート',
    'Undo': '元に戻す',
    'Redo': 'やり直し',
    'Open File': 'ファイルを開く',
    'Cancel': 'キャンセル',
    'OK': 'OK',
    'Refresh': '更新',
    'Multiple': '複数',
    'Skill List': 'スキルリスト',
    'Type of skill': 'スキルの種類',
    'Name of skill': 'スキルの名前',
    'exampleFormat': 'ファイルからインポートするか、以下の形式でinstinct.hからスキルデータをコピー＆ペーストしてください。\n* 波括弧はそのままにしてください！',
    'Quit': '終了',
    'Do you want to quit?': '終了しますか？',
    'mirror': 'ミラーリング',
    '>|<': '>|<',
    'Posture': 'ポーズ',
    'Gait': '歩行',
    'Behavior': 'ビヘイビア',
    'Clear': 'クリア',
    'max': '最大',

    'Manual mode': 'マニュアルモード',
    'Replug mode': 'リプラグモード',
    'Replug prompt': '警告：接続に失敗しました！\n\n* メインボードがコンピュータに接続されていない場合：\n\n以下のボタンをクリックしてください。'
                     'USBケーブルをメインボードに接続し、他の端をコンピュータに接続してください。\n\n* メインボードがすでにUSBケーブルを介してコンピュータに接続されている場合：\n\n1. '
                     'コンピュータがUSBデバイスを認識できることを確認します。\n詳細は、https://docs.petoi.com/upload-firmwareを参照してください。\n\n2. '
                     '以下のボタンをクリックした後、USBケーブルをコンピュータ側から抜き、再び接続します。',
    'Confirm': '確認',
    'Counting down to manual mode: ': 'マニュアルモードまでのカウントダウン：',
    'Info': '情報',
    'New port prompt': '新しいUSBデバイスが見つかりました：',
    'Please select the port from the list': 'リストからポートを選択してください',
    '* Port ': '* ポート ',
    ' cannot be opened': ' は開けません',

    'Calibrate': 'キャリブレーション',
    'Rest': 'リセット',
    'Stand Up': '立ち上がる',
    'Walk': '歩く',
    'Abort': '中止',
    'Do you want to save the offsets?': 'オフセットを保存しますか？',
    'uploaderTitle': 'ファームウェアアップローダ',
    'labTrans': '言語の変更',
    'labChi': '中国語',
    'labEng': '英語',
    'labHelp': 'ヘルプ',
    'labAbout': 'について',
    'labExit': '終了',
    'labFileDir': 'リリースフォルダの選択',
    'btnFileDir': '...',
    'titleFileDir': 'リリースフォルダを選択してください',
    'labPort': 'シリアルポート',
    'labSoftwareVersion': 'ソフトウェアバージョン',
    'labBoardVersion': 'ボードバージョン',
    'labProduct': '製品',
    'labMode': 'モード',
    'rbnWalk': 'ウォーク',
    'rbnUltrasonic': '超音波',
    'rbnCamera': 'カメラ',
    'Parameters': 'パラメーター',
    'Main function': 'メイン機能',
    'btnFacReset': '工場出荷時設定に戻す',
    'tipFacReset': 'ファクトリーリセット後、関節のキャリブレーションを行う必要があります。詳細は次を参照してください：https://docs.petoi.com/joint-calibration',
    'btnUpgrade': 'ファームウェアのアップグレード',
    'tipUpgrade': 'パラメータとメイン機能の両方をアップグレードします。ソフトウェアの新しいバージョンをダウンロードした場合は必須です。キャリブレーション値を保持する場合は、\'N\'を選択できます。',
    'btnUpdateMode': 'モードのみを更新',
    'tipUpdateMode': '新しいダウンロード後、ファームウェアを少なくとも1回アップグレードした場合、パラメータをリフレッシュせずにモードのみを切り替える方が速くなります。',
    'Warning': '警告',
    'Uploading': 'アップロード中 ',
    'is successully uploaded': 'が正常にアップロードされました',
    'failed to upload': 'のアップロードに失敗しました',
    'Need to manually select the model type (Nybble/Bittle)': 'モデルタイプ（Nybble/Bittle）を手動で選択する必要があります',
    'msgFileDir': 'リリースフォルダを選択してください！',
    'msgPort': '正しいシリアルポートを選択してください！',
    'msgNoneAvrdude': 'avrdudeがありません。まずavrdudeをインストールしてください！詳細については次を参照してください：https://docs.petoi.com/desktop-app'
                      '/firmware-uploader#install-avrdude-in-the-linux-os',
    'titleVersion': 'バージョン情報',

    'msgVersion': 'バージョン：' + versionNum + '\n' +
                  '''OpenCat用のファームウェアアップロードツール
著作権 © 2018-2023
全著作権 Petoi LLC
https://www.petoi.com\n''' + dateStr,

    'reset joints?': 'ジョイントオフセットをリセットしますか？（Y/N）',
    'reseting joints': 'ジョイントオフセットをリセット中...',
    'joints reset': 'ジョイントオフセットのリセットが完了しました！',

    'update instincts?': '本能をアップデートしますか？（Y/N）',
    'updating instincts': '本能をアップデート中...',
    'instincts updated': '本能がアップデートされました',

    'calibrate IMU?': 'IMUをキャリブレーションしますか？（Y/N）\n注：メインボードをテーブルの上に平らに置いてください！',
    'calibrating IMU': 'IMUをキャリブレーション中...',
    'IMU calibrated': 'IMUのキャリブレーションが完了しました！',
    'parameterFinish': 'パラメータが初期化されました！次のステップはメイン機能のアップロードです！',
    '9685 Calibrated': 'PCA9685が正常にキャリブレーションされました！',
    'msgFinish': 'ファームウェアのアップロードが完了しました！',
    'msgMode': '無効です。別のモードを選択してください！',

    'Standard': '標準',
    'RandomMind': 'ランダムマインド',
    'Ultrasonic': '超音波',
    'Voice': '音声',
    'Camera': 'カメラ',
    'Mind+': 'マインド+',
    'RandomMind_Ultrasonic': 'ランダムマインド_超音波',

    'Breath': '呼吸',
    'Rotate': '回転',
    'Flash': '点滅',
    'Meow': 'ニャー',

    'labEdit': '編集',
    'labTheme': 'テーマ',
    'tipConnect': '無効化されるまでアクティブなシリアルポートを継続的に更新します',
    'tipPortMenu': '単一またはすべてのデバイスを制御します',
    'tipServo': 'サーボを有効化/無効化します',
    'tipGyro': 'ジャイロスコープを有効化/無効化します',
    'tipRandom': 'ランダムな動作を有効化/無効化します\n特定のモードでのみ',
    'tipBinder': '他のジョイントにバインドします',
    'tipRevBinder': '他のジョイントに逆バインドします',
    'tipPlay': 'アクティブなフレームからスケジューラを実行します\n再生中に停止することができます',
    'tipImport': 'ファイルまたはテキストからスキルをインポートします',
    'tipRestart': 'スケジューラ内のすべてのフレームをクリアします！',
    'tipExport': 'スキルはリアルタイムで送信され、ロボットの静的メモリに保存されます\n最後に送信されたスキルを呼び出すには、シリアルトークン \'T\' を使用します',
    'tipMirror': '現在のフレームをミラーリングします',
    'tipMirrorXport': 'スキル全体をエクスポートするときにスキル全体をミラーリングします\nスキル全体をエクスポートする場合に効果的です',
    'tipGorB': '動作はキーフレーム間を補間し、一度だけ実行されます\n歩行はスムージングなしですべてのフレームをループします',
    'tipLoop': 'ループする開始フレームと終了フレームを設定します\nスキル全体をエクスポートする場合に効果的です',
    'tipRepeat': 'ループ回数を入力します\n-1は無限ループです。「リセット」ボタンのみがループを中断できます！\nスキル全体をエクスポートする場合に効果的です',
    'tipSet': '現在のフレームにジャンプ/保存します',
    'tipStep': '単位：度/ステップ\nスキル全体をエクスポートする場合に効果的です',
    'tipDelay': '単位：ミリ秒\n現在のフレームの後、次のフレームに入る前の遅延時間\nトリガーが有効な場合、遅延はトリガーの後から開始されます\nスキル全体をエクスポートする場合に効果的です',
    'tipTrig': 'トリガー角度を超えたときにのみ次のフレームをトリガーします\nスキル全体をエクスポートする場合に効果的です',
    'tipTrigAngle': 'トリガーの臨界角度\nスキル全体をエクスポートする場合に効果的です',
    'tipNote': 'フレームに覚えやすい名前を付けます',
    'tipAdd': 'アクティブなフレームをコピーして\n次の行に挿入します',
    'tipDel': '現在のフレームを削除します',

    'tipImgWiring': 'サーボプラグの位置と向きに注意してください\nバッテリーのボタンを長押しして電源をオンにします\n「キャリブレーション」をクリックしてすべてのサーボをキャリブレーション状態に回転させます\n'
                    '脚と頭を垂直に取り付けます\nスライダーを使用して脚のエッジと参照定規を平行に揃えます',
    'tipImgPosture': 'ポーズを切り替えてキャリブレーションの結果をテストします\nオフセットをタイムリーに保存します\n将来のキャリブレーションは不要です',
}

textIT = {
    'lan': 'Italian',
    'lanOption': 'Italiano',
    'lanMenu': 'Lingua',
    'uiTitle': 'Applicazione desktop Petoi',
    'calibTitle': 'Calibratore articolare',
    'skillComposerTitle': 'Petoi compositore per OpenCat',
    'Model': 'Modello',
    'Utility': 'Utilità',
    'Joint Calibrator': 'Calibratore articolare',
    'Skill Composer': 'Compositore di abilità',
    'Task Scheduler': 'Agenda',
    'Scheduler': 'Sequenza',
    'Firmware Uploader': 'Caricatore di firmware',
    'Eye color picker': 'Selettore del colore degli occhi',
    'Creator Information': 'Informazioni sul creatore',
    'Creator': 'Creatore',
    'Location': 'Posizione',
    'Nature': 'Natura',
    'Earth': 'Terra',
    'InputCreator': 'Inserisci il nickname del creatore',
    'InputLocation': 'Inserisci la posizione del creatore',
    'Exit': 'Uscita',
    'Help': 'Aiuto',
    'About': 'Chi siamo',
    'Repeat': 'Ripeti',
    'Loop': 'Loop',
    'Frame': 'Quadro',
    'Step': 'Velocita',
    'Delay': 'Ritardo',
    'Trig': 'Trig',
    'Angle': 'Angolo',
    'Note': 'Nota',
    'Del': 'Canc',
    'Add': 'Aggingi',
    'Set': 'Set',
    'Save': 'Salva',
    'Stop': 'Stop',
    'Joint Controller': 'Controllo multiplo',
    'Unbind All': 'Separa tutto',
    'Yaw': 'Yaw',
    'Pitch': 'Pitch',
    '-Pitch': '-Pitch',
    'Roll': 'Roll',
    '-Roll': '-Roll',
    'Spinal': 'Spinal',
    'Height': 'Altezza',
    'Sideway': 'Di lato',
    'Head Pan': 'Rotazione testa',
    'Head Tilt': 'Inclinazione testa',
    'Tail Pan': 'Scodinzolo',
    'N/A': 'N/A',
    'Left Front': 'Sinistra Frontale',
    'Right Front': 'Destra Frontale',
    'Right Back': 'Destra Posteriore',
    'Left Back': 'Sinistra Posteriore',
    'Shoulder': 'Spalla',
    'Arm': 'Arto superiore',
    'Knee': 'Arto Inferiore',
    'State Dials': 'Selezioni connessioni',
    'Connect': 'Connetti',
    'Connected': 'Connesso',
    'Listening': 'In ascolto',
    'All': 'Tutti',
    'None': 'Nessuno',
    'Servo': 'Servo',
    'Gyro': 'Gyro',
    'Random': 'Random',
    'Send': 'Inviare',
    'Postures': 'Posizioni Preset',
    'Skill Editor': 'Skill Editor',
    'Play': 'Start',
    'Pause': 'Pausa',
    'Import': 'Importa',
    'Restart': 'Restart',
    'Export': 'Esporta',
    'Undo': 'Undo',
    'Redo': 'Redo',
    'Open File': 'Apri File',
    'Cancel': 'Cancella',
    'OK': 'OK',
    'exampleFormat': 'Importa da file o copia e incolla i dati delle abilità da instinct.h nel seguente formato.\n* '
                     'Mantieni le parentesi graffe!',
    'Quit': 'Esci',
    'Do you want to quit?': 'Vuoi uscire ?',
    'mirror': 'Specchio',
    '>|<': '>|<',
    'Gait': 'Cammina',
    'Behavior': 'Comportamento',
    'Clear': 'Cancella',
    'max': 'max',

    'Manual mode': 'Modalità manuale',
    'Replug mode': 'Modalità di ricarica',
    'Replug prompt': '''ATTENZIONE: caricamento fallito!\n\n
* Se la scheda principale NON è collegata al computer:\n
Fare clic sul pulsante in basso. Collegare il cavo USB alla scheda principale, quindi collegare l\'altra estremità al 
COMPUTER.\n\n
* Se la scheda principale è già collegata al computer tramite un cavo USB:\n
1. Verificare che il computer sia in grado di riconoscere il dispositivo USB.\n
Ulteriori dettagli sono disponibili su https://docs.petoi.com/upload-firmware.\n
2. Dopo aver fatto clic sul pulsante in basso, scollegare il cavo USB dal lato COMPUTER, quindi ricollegarlo.
''',
    'Confirm': 'Confermare',
    'Counting down to manual mode: ': 'Conto alla rovescia per la modalità manuale: ',
    'Info': 'Informazione',
    'New port prompt': 'Scopri il nuovo dispositivo USB: ',
    'Please select the port from the list': 'Seleziona la porta dall\'elenco',
    '* Port ': '* Porta ',
    ' cannot be opened': ' non può essere aperto',

    'Calibrate': 'Calibrate',
    'Rest': 'Riposo',
    'Stand Up': 'In piedi',
    'Walk': 'Camminare',
    'Abort': 'Interrompi',
    'Do you want to save the offsets?': 'Vuoi salvare gli offset?',
    'uploaderTitle': 'Caricatore di firmware',
    'labTrans': 'Cambia lingua',
    'labChi': 'Cinese',
    'labEng': 'Inglese',
    'labHelp': 'Aiuto',
    'labAbout': 'Di',
    'labExit': 'Uscita',
    'labFileDir': 'Scegli la cartella di rilascio',
    'btnFileDir': '...',
    'titleFileDir': 'Si prega di scegliere la cartella di rilascio',
    'labPort': 'Porta seriale',
    'labSoftwareVersion': 'Versione software',
    'labBoardVersion': 'Versione da tavolo',
    'labProduct': 'Prodotto',
    'labMode': 'Modalità',
    'rbnWalk': 'Camminare',
    'rbnUltrasonic': 'Ultrasonico',
    'rbnCamera': 'Telecamera',
    'Parameters': 'Parametri',
    'Main function': 'Funzione principale',
    'btnFacReset': 'Ripristino delle impostazioni di fabbrica',
    'tipFacReset': ''' Dopo il ripristino delle impostazioni di fabbrica, 
 è necessario eseguire la calibrazione del giunto, fare riferimento a: 
 https://docs.petoi.com/joint-calibration ''',
    'btnUpgrade': 'Aggiorna il firmware',
    'tipUpgrade': ''' Aggiorna sia i parametri che la funzione principale. 
 * Obbligatorio se hai appena scaricato una nuova versione di questo software. 
 * È possibile selezionare \'N\' per conservare i valori di calibrazione. ''',
    'btnUpdateMode': 'Aggiorna solo la modalità',
    'tipUpdateMode': ''' Se hai aggiornato il firmware almeno una volta dopo un nuovo download, 
 è più veloce cambiare solo modalità senza aggiornare i parametri. ''',
    'Warning': 'Avvertimento',
    'Uploading': 'Caricamento in corso ',
    'is successully uploaded': ' è caricato con successo',
    'failed to upload': ' impossibile caricare',

    'msgFileDir': 'Si prega di scegliere la cartella di rilascio!',
    'msgPort': 'Si prega di scegliere la porta seriale corretta!',
    'msgNoneAvrdude': '''Non c\'è avrdude. Si prega di installare avrdude all\'inizio! Per i dettagli, 
    fare riferimento a: https://docs.petoi.com/desktop-app/firmware-uploader#install-avrdude-in-the-linux-os''',
    'titleVersion': 'Informazioni sulla versione',
    'msgVersion': 'Versione: ' + versionNum + '\n' +
                  '''Strumento di caricamento del firmware per OpenCat
    Diritto d'autore © 2018-2022
    Tutti i diritti riservati Petoi LLC
    https://www.petoi.com\n''' + dateStr,
    'reset joints?': 'Reimpostare gli offset dei giunti? (S/N)',
    'reseting joints': 'Reimposta gli offset del giunto...',
    'joints reset': 'Ripristino offset giunti completato!',

    'update instincts?': 'Aggiornare l\'istinto? (S/N)',
    'updating instincts': 'Aggiornamento degli istinti......',
    'instincts updated': 'Istinti aggiornati',

    'calibrate IMU?': '''Calibrare l\'IMU? (S/N)
    Nota: Appoggia la scheda madre PIATTA su un tavolo!''',
    'calibrating IMU': 'Taratura dell\'IMU...',
    'IMU calibrated': 'Calibrazione IMU completata!',

    'parameterFinish': '''Parametri inizializzati!
     Il prossimo passo è caricare la funzione principale!''',
    '9685 Calibrated': 'PCA9685 è stato calibrato con successo!',
    'msgFinish': 'Caricamento del firmware completato!',
    'msgMode': 'Non valido, selezionare un\'altra modalità!',
    'Standard': 'Standard',
    'RandomMind': 'MenteCasuale',
    'Ultrasonic': 'Ultrasonico',
    'Voice': 'Voce',
    'Camera': 'Telecamera',
    'Mind+': 'Mind+',
    'RandomMind_Ultrasonic': 'MenteCasuale_Ultrasonico',

    'Breath': 'Respiro',
    'Rotate': 'Ruotare',
    'Flash': 'Veloce',
    'Meow': 'Miao',
    'labEdit': 'Modificare',
    'labTheme': 'Tema',
    # '':'',
    'tipConnect': 'Continua ad aggiornare le porte seriali\nattive fino a quando non viene disabilitato',
    'tipPortMenu': 'Controlla dispositivon singolo o tutti',
    'tipServo': 'Attiva/Disattiva servos',
    'tipGyro': 'Attiva/Disattiva giroscopio',
    'tipRandom': 'Attiva/Disattiva comportamento random\n* in alcune modalita',
    'tipBinder': 'Legare ad altre articolazioni',
    'tipRevBinder': 'Legare inversamente ad altre articolazioni',
    'tipPlay': 'Passa attraverso lo sheduler dal frame attivo\nPuoi fermarti mentre giochi',
    'tipImport': 'Importa competenze da file o testi',
    'tipRestart': 'Cancella tutti i frame nello scheduler!',
    'tipExport': 'La skill verrà inviata in tempo reale e salvata\nnella memoria statica del robot\nUsa il token'
                 'seriale \'T\' per chiamare l\'ultima abilità inviata',
    'tipMirror': 'Specchia il fotogramma corrente',
    'tipMirrorXport': 'Rispecchia l\'intera abilità durante l\'esportazione\n* Efficace quando si esporta l\'intera '
                      'abilità',
    'tipGorB': 'Un comportamento esegue l\'interpolazione tra i fotogrammi chiave ed esegue una sola '
               'volta\nUn\'andatura scorre su tutti i fotogrammi senza alcuna levigatura',
    'tipLoop': 'Imposta i fotogrammi iniziale e finale per il looping\n* Efficace quando si esporta l\'intera abilità',
    'tipRepeat': 'Immettere il numero di loop\n-1 per loop infinito. Solo il pulsante \"reset\" può interrompere il '
                 'loop!\n* Efficace quando si esporta l\'intera abilità',
    'tipSet': 'Passa a/salva il fotogramma corrente',
    'tipStep': 'Unità: grado/passo\n* Efficace quando si esporta l\'intera abilità',
    'tipDelay': 'Unità: millisecondi\nRitardo dopo il fotogramma corrente, prima di entrare nel fotogramma '
                'successivo\nSe il trigger è valido, il ritardo inizia dopo il trigger\n* Efficace quando si esporta '
                'l\'intera abilità',
    'tipTrig': 'Attiva il fotogramma successivo solo quando il corpo rotola\noltre l\'angolo di innesco in una certa '
               'direzione\n* Efficace quando si esporta l\'intera abilità',
    'tipTrigAngle': 'L\'angolo critico per il grilletto\n* Efficace quando si esporta l\'intera abilità',
    'tipNote': 'Dai alla cornice un nome facile da ricordare',
    'tipAdd': 'Copia il frame attivo e\ninseriscilo nella riga successiva',
    'tipDel': 'Elimina il fotogramma corrente',

    'tipImgWiring': 'Prestare attenzione alla posizione e alla direzione dei connettori dei servi\nPremere a lungo il '
                    'pulsante della batteria per accendere l\'alimentazione\nFare clic su \"Calibra\" per ruotare '
                    'tutti i servi allo stato di calibrazione\nAttacca le gambe e la testa perpendicolarmente\nUsa il '
                    'cursore per allineare parallelamente i bordi delle gambe e il righello di riferimento',
    'tipImgPosture': 'Passa da una postura all\'altra per testare i risultati della calibrazione\nSalva gli offset in '
                     'tempo\nNon c\'è bisogno di calibrazione in futuro',
}


class Translator:
    """
    Translator class for translating text to different languages for the UI.
    """

    def __init__(self, language: str = "English"):
        self.logger = create_logger("Translator", "Translator", "Translator_", level="ERROR")
        self.languageList = {
            'English': textEN,
            'Simplified Chinese': textCN,
            'Traditional Chinese': textCN_TW,
            'German': textDE,
            'Italian': textIT,
            'French': textFR,
            'Japanese': textJP,
            'Thai': textTH,
            # to be added
        }
        self.language = language

    @property
    def languages(self) -> list:
        """
        Returns a list of all available languages.

        Returns:
            list: List of all available languages.
        """
        return list(self.languageList.keys())

    def getTranslation(self, text: str) -> str:
        """
        Gets the translation for a given string in the above translation dictionaries in a specific language.

        Returns:
            str: Translated text

        Raises:
            KeyError: When the requested text is not found in the luggage pack.
        """
        try:
            return self.languageList[self.language][text]

        except KeyError as error:  # Catches the error in order for the error to be logged and then re-raises the error
            self.logger.error(f"Key {text} not found for language {self.language}")
            raise error

    def getIndependentTranslation(self, language: str, element: str) -> str:
        """
        Gets the translation for a given string in the above translation dictionaries in a specific language.

        Returns:
            str: Translated text
        """
        try:
            return self.languageList[language][element]

        except KeyError as error:  # Catches the error in order for the error to be logged and then re-raises the error
            self.logger.error(f"Key {element} not found for language {language}")
            raise error



# Classes named after the language they translate to. This is done to make it easier to add new languages.
class English:
    """
    English translation class.
    """

    def __str__(self):
        return "English"

    def __repr__(self):
        return "English"


class SimplifiedChinese:
    """
    Simplified Chinese translation class.
    """

    def __str__(self):
        return "Simplified Chinese"

    def __repr__(self):
        return "Simplified Chinese"


class TraditionalChinese:
    """
    Traditional Chinese translation class.
    """

    def __str__(self):
        return "Traditional Chinese"

    def __repr__(self):
        return "Traditional Chinese"


class German:
    """
    German translation class.
    """

    def __str__(self):
        return "German"

    def __repr__(self):
        return "German"


class Italian:
    """
    Italian translation class.
    """

    def __str__(self):
        return "Italian"

    def __repr__(self):
        return "Italian"


class French:
    """
    French translation class.
    """

    def __str__(self):
        return "French"

    def __repr__(self):
        return "French"


class Japanese:
    """
    Japanese translation class.
    """

    def __str__(self):
        return "Japanese"

    def __repr__(self):
        return "Japanese"


class Thai:
    """
    Thai translation class.
    """

    def __str__(self):
        return "Thai"

    def __repr__(self):
        return "Thai"
