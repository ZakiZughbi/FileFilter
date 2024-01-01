import os

# THESE ARE FAILED TESTS

# def doesFileExist(filePathAndName):
#     return os.path.exists(filePathAndName)
#
# if doesFileExist(./runn)

# path = "/Users/admin/google drive/programming/scripts/JS"

# for root, dirs, files in os.walk(path):
#     print(files)



# array = ['index.html', 'dom2.js', 'dom.js', 'dom3.js']
#
# for i in array:
#     path = pathlib.Path(i)
#     print(i)
#     path.exists()
#     print('------------------')

# path = pathlib.Path('app.js')
# path.exists()
#
# os.path.exists('dsaf-dir')



# if os.path.isfile('app.js') == True:
#     print('true')
# else:
#     print('false')













# Physical List of root directories
rootList = [
'/Users/admin/google drive/programming/scripts',
'/Users/admin/google drive/programming/scripts/Portal',
'/Users/admin/google drive/programming/scripts/Portal/EmbedPdf',
'/Users/admin/google drive/programming/scripts/Portal/WebFolder',
'/Users/admin/google drive/programming/scripts/Python',
'/Users/admin/google drive/programming/scripts/Python/FirstScripts',
'/Users/admin/google drive/programming/scripts/Python/FirstScripts/Previous Proj.',
'/Users/admin/google drive/programming/scripts/Python/FirstScripts/Previous Proj./Cook_Book',
'/Users/admin/google drive/programming/scripts/Python/FirstScripts/Previous Proj./Journal_App',
'/Users/admin/google drive/programming/scripts/Python/FirstScripts/__pycache__',
'/Users/admin/google drive/programming/scripts/Python/FirstScripts/Python_Chalenge',
'/Users/admin/google drive/programming/scripts/Python/FirstScripts/Current Proj.',
'/Users/admin/google drive/programming/scripts/Python/FirstScripts/Current Proj./Quran Program',
'/Users/admin/google drive/programming/scripts/Python/FirstScripts/Current Proj./Quran Program/__pycache__',
'/Users/admin/google drive/programming/scripts/Python/FirstScripts/.ipynb_checkpoints',
'/Users/admin/google drive/programming/scripts/Python/FileChecker',
'/Users/admin/google drive/programming/scripts/Python/OOP',
'/Users/admin/google drive/programming/scripts/Python/FileAutoScripts',
'/Users/admin/google drive/programming/scripts/Python/FileAutoScripts/Practice',
'/Users/admin/google drive/programming/scripts/CSS',
'/Users/admin/google drive/programming/scripts/CSS/responsive-design',
'/Users/admin/google drive/programming/scripts/CSS/responsive-design/images',
'/Users/admin/google drive/programming/scripts/CSS/FlipBoxTest',
'/Users/admin/google drive/programming/scripts/CSS/css-flex-box',
'/Users/admin/google drive/programming/scripts/CSS/css-flex-box/example-1',
'/Users/admin/google drive/programming/scripts/CSS/css-flex-box/example-3',
'/Users/admin/google drive/programming/scripts/CSS/css-flex-box/example-3/img',
'/Users/admin/google drive/programming/scripts/CSS/css-flex-box/example-2',
'/Users/admin/google drive/programming/scripts/CSS/css-flex-box/example-2/img',
'/Users/admin/google drive/programming/scripts/CSS/CSS-Variables',
'/Users/admin/google drive/programming/scripts/CSS/css-grid',
'/Users/admin/google drive/programming/scripts/CSS/css-animations',
'/Users/admin/google drive/programming/scripts/CSS/css-animations/rotate-examples',
'/Users/admin/google drive/programming/scripts/CSS/css-animations/web-examples',
'/Users/admin/google drive/programming/scripts/CSS/css-animations/web-examples/img',
'/Users/admin/google drive/programming/scripts/CSS/css-animations/mario-examples',
'/Users/admin/google drive/programming/scripts/CSS/css-animations/mario-examples/img',
'/Users/admin/google drive/programming/scripts/CSS/css-animations/CSS Animations',
'/Users/admin/google drive/programming/scripts/JS',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-17',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-10',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-6',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-1',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-8',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-11',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-18',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-9',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-7',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/master',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-2',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-5',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-4',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-3',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-15',
'/Users/admin/google drive/programming/scripts/JS/JS-DOM/lesson-12',
'/Users/admin/google drive/programming/scripts/JS/domcrashcourse',
'/Users/admin/google drive/programming/scripts/HTML',
'/Users/admin/google drive/programming/scripts/Swift',
'/Users/admin/google drive/programming/scripts/Swift/Swift OOP.playground',
'/Users/admin/google drive/programming/scripts/Swift/Swift OOP.playground/playground.xcworkspace',
'/Users/admin/google drive/programming/scripts/Swift/Swift OOP.playground/playground.xcworkspace/xcuserdata',
'/Users/admin/google drive/programming/scripts/Swift/Swift OOP.playground/playground.xcworkspace/xcuserdata/Zaki.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/Swift OOP.playground/playground.xcworkspace/xcshareddata',
'/Users/admin/google drive/programming/scripts/Swift/ClassDemo',
'/Users/admin/google drive/programming/scripts/Swift/ClassDemo/ClassesDemo',
'/Users/admin/google drive/programming/scripts/Swift/ClassDemo/ClassesDemo.xcodeproj',
'/Users/admin/google drive/programming/scripts/Swift/ClassDemo/ClassesDemo.xcodeproj/xcuserdata',
'/Users/admin/google drive/programming/scripts/Swift/ClassDemo/ClassesDemo.xcodeproj/xcuserdata/Zaki.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/ClassDemo/ClassesDemo.xcodeproj/xcuserdata/Zaki.xcuserdatad/xcschemes',
'/Users/admin/google drive/programming/scripts/Swift/ClassDemo/ClassesDemo.xcodeproj/project.xcworkspace',
'/Users/admin/google drive/programming/scripts/Swift/ClassDemo/ClassesDemo.xcodeproj/project.xcworkspace/xcuserdata',
'/Users/admin/google drive/programming/scripts/Swift/ClassDemo/ClassesDemo.xcodeproj/project.xcworkspace/xcuserdata/Zaki.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/ClassDemo/ClassesDemo.xcodeproj/project.xcworkspace/xcshareddata',
'/Users/admin/google drive/programming/scripts/Swift/OOP',
'/Users/admin/google drive/programming/scripts/Swift/OOP/OOP.xcodeproj',
'/Users/admin/google drive/programming/scripts/Swift/OOP/OOP.xcodeproj/xcuserdata',
'/Users/admin/google drive/programming/scripts/Swift/OOP/OOP.xcodeproj/xcuserdata/Zaki.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/OOP/OOP.xcodeproj/xcuserdata/Zaki.xcuserdatad/xcschemes',
'/Users/admin/google drive/programming/scripts/Swift/OOP/OOP.xcodeproj/project.xcworkspace',
'/Users/admin/google drive/programming/scripts/Swift/OOP/OOP.xcodeproj/project.xcworkspace/xcuserdata',
'/Users/admin/google drive/programming/scripts/Swift/OOP/OOP.xcodeproj/project.xcworkspace/xcuserdata/Zaki.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/OOP/OOP.xcodeproj/project.xcworkspace/xcshareddata',
'/Users/admin/google drive/programming/scripts/Swift/OOP/OOP',
'/Users/admin/google drive/programming/scripts/Swift/ClassesDemo 2',
'/Users/admin/google drive/programming/scripts/Swift/ClassesDemo 2/ClassesDemo',
'/Users/admin/google drive/programming/scripts/Swift/ClassesDemo 2/ClassesDemo.xcodeproj',
'/Users/admin/google drive/programming/scripts/Swift/ClassesDemo 2/ClassesDemo.xcodeproj/xcuserdata',
'/Users/admin/google drive/programming/scripts/Swift/ClassesDemo 2/ClassesDemo.xcodeproj/xcuserdata/Zaki.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/ClassesDemo 2/ClassesDemo.xcodeproj/xcuserdata/Zaki.xcuserdatad/xcschemes',
'/Users/admin/google drive/programming/scripts/Swift/ClassesDemo 2/ClassesDemo.xcodeproj/project.xcworkspace',
'/Users/admin/google drive/programming/scripts/Swift/ClassesDemo 2/ClassesDemo.xcodeproj/project.xcworkspace/xcuserdata',
'/Users/admin/google drive/programming/scripts/Swift/ClassesDemo 2/ClassesDemo.xcodeproj/project.xcworkspace/xcuserdata/Zaki.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/ClassesDemo 2/ClassesDemo.xcodeproj/project.xcworkspace/xcshareddata',
'/Users/admin/google drive/programming/scripts/Swift/Swift Fundementals.playground',
'/Users/admin/google drive/programming/scripts/Swift/Swift Fundementals.playground/playground.xcworkspace',
'/Users/admin/google drive/programming/scripts/Swift/Swift Fundementals.playground/playground.xcworkspace/xcuserdata',
'/Users/admin/google drive/programming/scripts/Swift/Swift Fundementals.playground/playground.xcworkspace/xcuserdata/Zaki.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/Swift Fundementals.playground/playground.xcworkspace/xcshareddata',
'/Users/admin/google drive/programming/scripts/Swift/OptionalsDemo',
'/Users/admin/google drive/programming/scripts/Swift/OptionalsDemo/OptionalsDemo',
'/Users/admin/google drive/programming/scripts/Swift/OptionalsDemo/OptionalsDemo.xcodeproj',
'/Users/admin/google drive/programming/scripts/Swift/OptionalsDemo/OptionalsDemo.xcodeproj/xcuserdata',
'/Users/admin/google drive/programming/scripts/Swift/OptionalsDemo/OptionalsDemo.xcodeproj/xcuserdata/Zaki.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/OptionalsDemo/OptionalsDemo.xcodeproj/xcuserdata/Zaki.xcuserdatad/xcschemes',
'/Users/admin/google drive/programming/scripts/Swift/OptionalsDemo/OptionalsDemo.xcodeproj/project.xcworkspace',
'/Users/admin/google drive/programming/scripts/Swift/OptionalsDemo/OptionalsDemo.xcodeproj/project.xcworkspace/xcuserdata',
'/Users/admin/google drive/programming/scripts/Swift/OptionalsDemo/OptionalsDemo.xcodeproj/project.xcworkspace/xcuserdata/Zaki.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/OptionalsDemo/OptionalsDemo.xcodeproj/project.xcworkspace/xcshareddata',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice.xcodeproj',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice.xcodeproj/xcuserdata',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice.xcodeproj/xcuserdata/a1.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice.xcodeproj/xcuserdata/a1.xcuserdatad/xcschemes',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice.xcodeproj/xcuserdata/Zaki.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice.xcodeproj/xcuserdata/Zaki.xcuserdatad/xcschemes',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice.xcodeproj/xcuserdata/angelayu.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice.xcodeproj/xcuserdata/angelayu.xcuserdatad/xcschemes',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice.xcodeproj/project.xcworkspace',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice.xcodeproj/project.xcworkspace/xcuserdata',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice.xcodeproj/project.xcworkspace/xcuserdata/Zaki.xcuserdatad',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice.xcodeproj/project.xcworkspace/xcshareddata',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice/Assets.xcassets',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice/Assets.xcassets/AppIcon.appiconset',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice/Assets.xcassets/artBoard.imageset',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice/Assets.xcassets/notebook.imageset',
'/Users/admin/google drive/programming/scripts/Swift/Auto-Layout-Practice-iOS12-master/Auto Layout Practice/Base.lproj',
'/Users/admin/google drive/programming/scripts/Assets',
'/Users/admin/google drive/programming/scripts/Git',
'/Users/admin/google drive/programming/scripts/Git/git-two',
'/Users/admin/google drive/programming/scripts/Git/git-two/.git',
'/Users/admin/google drive/programming/scripts/Git/git-two/.git/objects',
'/Users/admin/google drive/programming/scripts/Git/git-two/.git/objects/pack',
'/Users/admin/google drive/programming/scripts/Git/git-two/.git/objects/info',
'/Users/admin/google drive/programming/scripts/Git/git-two/.git/info',
'/Users/admin/google drive/programming/scripts/Git/git-two/.git/hooks',
'/Users/admin/google drive/programming/scripts/Git/git-two/.git/refs',
'/Users/admin/google drive/programming/scripts/Git/git-two/.git/refs/heads',
'/Users/admin/google drive/programming/scripts/Git/git-two/.git/refs/tags',
'/Users/admin/google drive/programming/scripts/Git/git-two/.git/branches',
'/Users/admin/google drive/programming/scripts/Git/git-one',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/92',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/0c',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/94',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/60',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/34',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/05',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/9c',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/a4',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/a3',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/c6',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/pack',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/16',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/80',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/74',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/7e',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/4c',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/4d',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/2f',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/9f',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/info',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/65',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/96',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/37',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/6d',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/6c',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/a7',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/d2',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/aa',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/cd',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/e6',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/f7',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/fa',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/f6',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/cb',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/46',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/2d',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/82',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/49',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/47',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/8b',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/13',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/objects/14',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/info',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/logs',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/logs/refs',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/logs/refs/heads',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/logs/refs/remotes',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/logs/refs/remotes/orgin',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/hooks',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/refs',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/refs/heads',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/refs/tags',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/refs/remotes',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/refs/remotes/orgin',
'/Users/admin/google drive/programming/scripts/Git/git-one/.git/branches',
'/Users/admin/google drive/programming/scripts/Git/fake-profile',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/objects',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/objects/ab',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/objects/e2',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/objects/pack',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/objects/info',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/objects/a8',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/objects/fa',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/objects/1e',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/objects/84',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/info',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/logs',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/logs/refs',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/logs/refs/heads',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/logs/refs/remotes',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/logs/refs/remotes/origin',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/hooks',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/refs',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/refs/heads',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/refs/tags',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/refs/remotes',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/refs/remotes/origin',
'/Users/admin/google drive/programming/scripts/Git/fake-profile/.git/branches',
'/Users/admin/google drive/programming/scripts/Git/gitPractice',
'/Users/admin/google drive/programming/scripts/Git/gitPractice/.git',
'/Users/admin/google drive/programming/scripts/Git/gitPractice/.git/objects',
'/Users/admin/google drive/programming/scripts/Git/gitPractice/.git/objects/pack',
'/Users/admin/google drive/programming/scripts/Git/gitPractice/.git/objects/info',
'/Users/admin/google drive/programming/scripts/Git/gitPractice/.git/info',
'/Users/admin/google drive/programming/scripts/Git/gitPractice/.git/hooks',
'/Users/admin/google drive/programming/scripts/Git/gitPractice/.git/refs',
'/Users/admin/google drive/programming/scripts/Git/gitPractice/.git/refs/heads',
'/Users/admin/google drive/programming/scripts/Git/gitPractice/.git/refs/tags',
'/Users/admin/google drive/programming/scripts/Git/gitPractice/.git/branches',
]

#This Program Filters the same file. It takes dir1 files looks in dir2 to see if it repeats then deletes that repeat file in dir1. It filters dir1 for any existing files in dir2.


# Grabs all file names in dir1 and puts it in "theFileList" array as strings.
#List of all the files that is needed to iterate through. This list is in a seperate directory.
theFileList = []
for root, dirs, files in os.walk(path):
   print(files)
   theFileList.append(files)

# Grabs all roots directories in dir2 and puts it in "theRootList" array as strings.
theRootList = []
for root, dirs, files in os.walk(path):
   print(root)
   theRootList.append(root)


#Filter
#   this program takes a file runs through all possible roots in dir2 that file can be in. If it finds a existing identical file in dir2 runs one small test to see if it is in dir1 again. Then deltes that repeat file. If that files is not existant is dir2 than it skipps to test the next file (in dir1).
for file in fileList:
    for root in rootList:
        os.chdir(root)
        if os.path.isfile(file) == True:
            print('true')
            print(file)
            print(root)
            os.chdir('/Users/admin/desktop/see')
            os.remove(file)
            print('---------------')

#Changes the program back to the desired directory after program completed its task
os.chdir('/Users/admin/Google Drive/Programming/Scripts/Python/FileChecker')
