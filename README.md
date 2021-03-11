
# Simon Says Discord Bot
 > Authors: [Dylan Riffel](https://github.com/driff001), [Rohit Manimaran](https://github.com/Rohit-M17)

 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 PHASE I: 
 
 Project Title: <Simon Says> Bot         https://github.com/orgs/cs100/teams/rmani010-driff001-jwalk057/discussions

Group member names:
Dylan Riffel          https://github.com/driff001
Rohit Manimaran https://github.com/Rohit-M17
Jeremy Walker    https://github.com/jwalk057

Project Description:
	Why is it interesting?
	
**This project is interesting to use because we want to learn exactly how discord bots function in tandem with spotify. Also, we see it as an opportunity to learn Python since the majority of the group has little experience with it. The project also may help to inform us about how APIs are sourced and how they can apply to our bot.**


**Language/tools/technology used: Python, Discord, Spotify, Github** 


What is the input/output of the project:
**The input of the bot would require the user to type commands (i.e., Simon says…) into the server to output music depending on the user’s command/mood. We would also have the bot output recommendations of playlists and could make playlists for users as a result of the user’s input.**


Two design patterns used(descriptions of them and why they were picked):
	
**Abstract factory(large scale):** 
“User interface that supports multiple look-and-feel standards”
The abstract class that declares the interface is the iteration commands that are given to Simon
I.e., Simon 
recommend me some songs
Add If I ain’t got you by alicia keys to my playlist
This will provide the user feel of interacting with Simon
The concrete classes that the user would not see or access is what happens under the hood of this program. The Spotify API posts and gets that create playlists for the users of the discord channel

**Composite(smaller scale):**
"The key to the Composite pattern is an abstract class that represents both primitives and their containers”
Treat some data members of Simon Says Bot as abstract base class objects with pure virtual functions. We can then derive classes to use these functions, as well as containers of derived classes. An example would be a derived class being a Playlist, which would be a container of other derived classes being Songs. A call of play() to the Playlist would recursively call the play() function of each song as well.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Phase II
## Class Diagram

### Description:
 We made two patterns to tackle the two primary features of the “Simon Says Discord Bot”: 

*Composite Pattern:*

* Implements the searching and creating of a song object at runtime depending on the input provided by the user in Discord upon summoning Simon
	* Song objects can either be of Spotify Song or Youtube Song type and they derive from the abstract base class Song
		* Therefore we have implemented the creation of them separately in the event that we would like to support another streaming service
		* We want users in a discord server to have the ability to queue up songs with Simon
			* This is implemented by creating another derived class that stores a Playlist which is a vector of Songs which has functions that can perform operations on the songs so that the order of the songs in the queue are manipulated to the user’s desire(i.e., shuffle randomly, by genre, by user, by last added, deque)

*Strategy Pattern:*

* Implements the SongFromRecommender class
	* If a user would like the discord bot to recommend them a song they can choose to have a recommendation come from Spotify or Youtube.
	* The derived classes will break up the work into two classes:
		* RecommenderFromSpotify - Uses Spotify API seed_track to get a recommendation.
		* RecommenderFromYoutube - Will query Youtube for one of the top song played that day.
 


*Attached is a link to the SIMON DISCORD OMT PDF

[Discord Simon Bot OMT.pdf](https://github.com/cs100/final-project-rmani010-driff001-jwalk057/files/6008155/Discord.Simon.Bot.OMT.pdf)

 
 ## Phase III
 You will need to schedule a check-in with the TA (during lab hours or office hours). Your entire team must be present. 
 * Before the meeting you should perform a sprint plan like you did in Phase II
 * In the meeting with your TA you will discuss: 
   - How effective your last sprint was (each member should talk about what they did)
   - Any tasks that did not get completed last sprint, and how you took them into consideration for this sprint
   - Any bugs you've identified and created issues for during the sprint. Do you plan on fixing them in the next sprint or are they lower priority?
   - What tasks you are planning for this next sprint.
 ## Final deliverable
> All group members will give a demo to the TA during lab time. The TA will check the demo and the project GitHub repository and ask a few questions to all the team members. 
> Before the demo, you should do the following:
> * Complete the sections below (i.e. Screenshots, Installation/Usage, Testing)
> * Plan one more sprint (that you will not necessarily complete before the end of the quarter). Your In-progress and In-testing columns should be empty (you are not doing ore work currently) but your TODO column should have a full sprint plan in it as you have done before. This should include any known bugs (there should be some) or new eatures you would like to add. These should appear as issues/cards on your Kanban board. 

## Screenshots
![valgrind](/Picture/valgrind.png)
![queue](/Picture/workingqueue.PNG)
![functions](/Picture/workingfunctions.PNG)
![help](/Picture/helpfunction.PNG)
![Omt](/Picture/Omt.PNG)

## Installation/Usage

Alvinnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn... Hi its Simon here. Working online can be really boring but I am here to make things more fun. Simon bot is still in production and is not available in the Discord Bot store but no worries you can go ahead and test the beta yourself. First you will need to download the SimonSays.py Discord file from our Repo and run it on your local machine.In order to properly utilize this discord bot, you must run command prompt in Administrator mode and install python directly to command propmt. To do this, you must a recent version of python at www.python.org . Once that is done, go to the windows search bar and type "Edit environment variables." Once that's selected, click add path. Then you must include the python executable as path. You will then need to create a discord bot by visiting the discord developer portal online at https://discord.com/developers/applications. There you will get access to your own Discord bot token. In the code there will be a variable called 'TOKEN = ' there you will enter your unique token. Make sure not to share this with anyone. In the developer portal you can invite simon into a server of your choice. Simon will  enter a voice chat when you give him a !join commmand in the chat and he will enter your voice room. Not sure what simon can do. Enter !help tp get a description of the available commands. Simon will be active while you are running the python file in your machine.Then, in order for the bot to function properly, run command prompt as administrator and type "pip install youtube_dl." When this final part is done, run your given .py file in command prompt as administrator by accessing the using cd to access the appropriate file and call "python <yourfilename>.py." 
	
## Testing
Our testing was validated partially by creating a tester bot in order to check the various input of the bot. This project was tested using valgrind and profile memory check for checking function's memory leakage using leak check full. We also explored the options of creating a tester discord bot that will be able to run automatic tests such as distest and unittest but they were not able to simulate some of the functionality of a discord server.

