Mukioplayer-Py-Mac
===========================
This is a solution of the damn fact that Mac, one of the best OS in human history, does not have a reliable and nice video comment playing software.

Written in Python, based on Mukioplayer, this is a quick way to enjoy comment(DanMu) on Mac.

Also check https://github.com/superwbd/ABPlayerHTML5-Py--nix  , this is the one with HTML5 and ABPlayerHTML5. Works fine and produce less heat with Macbooks for not using Flash, but a tiny bit more unpredictable.

Looking for downloading video and comment from Bilibili really simple and quick? Check Biligrab: https://gist.github.com/superwbd/9605757  , auto download, rename, and concatenate into one file.(For more info, check http://www.cnbeining.com/?p=330)


Download
------
I will upload every version here: https://sourceforge.net/projects/mukioplayerpymac/

However, feel free to download here via the ZIP file. I just want to provide you a way to download all the old versions.

Usage
------
Download all the files, extract into one folder. Personally I do not suggest you go anywhere above ‘~’, for you would meet all kinds of privilege problems, which I suppose would drive you mad.

Make sure you have a web browser which can play Flash.

Make sure you use Python 2.7 (this is provided along with OSX), and run ‘python server.py’.

After “Vid”, drag in the video file you would like to play. Generally speaking, .flv, .hlv, .mp4 files would be fine, however, there ’s no guarantee that they can play in this player. And don’t blame me for that: Personally, I am sure that videos with H.264+AAC won’t have any problem, which would include most of the online videos. Enter.

For XML, drag in the XML file. Commit files from Bilibili would be OK, which had beed tested, while those from other sites are pending test. Please tell me the test result you have, this would be very helpful, and hereby I thank you in advance for your help. If the video name and the comment filename are the same, just press ENTER, and it will get the comment by itself. Enter.

For the first you run it, OSX may ask you for approving the connections. It does not matter whether you choose "Allow" or not, but I would suggest you to select "NO", for once I 've got UToronto 's auto scanner detected the random port, and did a lot of interesting scan. Of course, nothing found, and I wrote the UToronto ITS an angry email.

Now the browser would open by herself, enjoy it!

After you use it, BE SURE to input Ctrl+C in the bash window! Though I have made some improvement to enhance the security, better safe than sorry. 

Things you should know
-----
Please do not include anything besides characters or numbers in your folder or filename. There ’s no guarantee that symbols would be cool.
(Update: This should be fixed in version .05. Open an issue if it does not work.)

Make sure you use Python 2.7, 3.3 won’t work for it doesn’t have some important network modules.

This software is not made for playing anything above the folder “~”. Don’t get surprised if it gives you funny results.
(Update: Now it should can play things regardless the original location.)

If somehow the player failed to load, try refreshing the page, for the programme has to copy the original file first before you can visit.

I am completely new to Python and programming, so do please help me to improve this, and I would appreciate it very much.

About me
-----
Beining, CDC of ACI-CFG, 1st year CS student of UT.

Get in touch with me via cnbeining[at]gmail.com  .

Copyleft
-----
A number of opensource codes are used in this little project, especially the main programme, Mukioplayer. The website of Mukioplayer is https://code.google.com/p/mukioplayer/  ,MIT License.

The part of web server is from http://yige.org  .

This project uses MIT licence. 

Update history
-----
.10: Use raw_input, now you do not need to input " ' "_ before files.

.09: Fix the problem that if ~/.cache does not exist, it will return a 404. Also fix the version number problem.

.08: If the video name and the comment filename are the same, just input " '' " in "XML", and it will get the comment by itself.

.07: Fix the problem that video filename cannot have "#" in it.

.06: Randomise the port, makes it impossible to be scanned.

.05：Fix the problem that file or folder name can't be Chinese or whatever.

.04: Change the way to load the player to make it able to full screen.

.03: Change the way to start server to make it safer(also slower, sorry)

.02: ???

.01: First version
