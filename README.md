
# Simon Says Discord Bot
 > Authors: [Dylan Riffel](https://github.com/driff001), [Rohit Manimaran](https://github.com/Rohit-M17), [Jeremy Walker](https://github.com/jwalk057)

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
 > ## Phase II
 > In addition to completing the "Class Diagram" section below, you will need to 
 > * Set up your GitHub project board as a Kanban board for the project. It should have columns that map roughly to 
 >   * Backlog, TODO, In progress, In testing, Done
 >   * You can change these or add more if you'd like, but we should be able to identify at least these.
 > * There is no requirement for automation in the project board but feel free to explore those options.
 > * Create an "Epic" (note) for each feature and each design pattern and assign them to the appropriate team member. Place these in the `Backlog` column
 > * Complete your first *sprint planning* meeting to plan out the next 7 days of work.
 >   * Create smaller development tasks as issues and assign them to team members. Place these in the `Backlog` column.
 >   * These cards should represent roughly 7 days worth of development time for your team, taking you until your first meeting with the TA
## Class Diagram
 > Include a class diagram(s) for each design pattern and a description of the diagram(s). Your class diagram(s) should include all the main classes you plan for the project. This should be in sufficient detail that another group could pick up the project this point and successfully complete it. Use proper OMT notation (as discussed in the course slides). You may combine multiple design patterns into one diagram if you'd like, but it needs to be clear which portion of the diagram represents which design pattern (either in the diagram or in the description). 

>#Description:
>We made two patterns to tackle the two primary features of the “Simon Says Discord Bot”: 

>*Composite Pattern:*

>* Implements the searching and creating of a song object at runtime depending on the input provided by the user in Discord upon summoning Simon
>	* Song objects can either be of Spotify Song or Youtube Song type and they derive from the abstract base class Song
>		* Therefore we have implemented the creation of them separately in the event that we would like to support another streaming service
>		* We want users in a discord server to have the ability to queue up songs with Simon
>			* This is implemented by creating another derived class that stores a Playlist which is a vector of Songs which has functions that can perform operations on the songs so that the order of the songs in the queue are manipulated to the user’s desire(i.e., shuffle randomly, by genre, by user, by last added, deque)

>*Strategy Pattern:*

>* Implements the statuses feature of Simon
>	* If a user is planning on stepping away from a discord call they can tell Simon they are stepping away for dinner or using the restroom and this will set their status to their input, additionally, users can input how long they will be away for
>	* The abstraction for the Status class is that the derived class will break up the work into two classes:
>		* TimerStatus - Calculates the time since the user has set their status.
>		* AwayStatus - Calculates the time until the user’s status is up.
 


>*Attached is a link to the SIMON DISCORD OMT PDF
 [ProjectOmtNew.pdf](https://github.com/cs100/final-project-rmani010-driff001-jwalk057/files/5986844/ProjectOmtNew.pdf)

 
 
 > ## Phase III
 > You will need to schedule a check-in with the TA (during lab hours or office hours). Your entire team must be present. 
 > * Before the meeting you should perform a sprint plan like you did in Phase II
 > * In the meeting with your TA you will discuss: 
 >   - How effective your last sprint was (each member should talk about what they did)
 >   - Any tasks that did not get completed last sprint, and how you took them into consideration for this sprint
 >   - Any bugs you've identified and created issues for during the sprint. Do you plan on fixing them in the next sprint or are they lower priority?
 >   - What tasks you are planning for this next sprint.

 > ## Final deliverable
 > All group members will give a demo to the TA during lab time. The TA will check the demo and the project GitHub repository and ask a few questions to all the team members. 
 > Before the demo, you should do the following:
 > * Complete the sections below (i.e. Screenshots, Installation/Usage, Testing)
 > * Plan one more sprint (that you will not necessarily complete before the end of the quarter). Your In-progress and In-testing columns should be empty (you are not doing more work currently) but your TODO column should have a full sprint plan in it as you have done before. This should include any known bugs (there should be some) or new features you would like to add. These should appear as issues/cards on your Kanban board. 
 
 ## Screenshots
 > Screenshots of the input/output after running your application
 ## Installation/Usage
 > Instructions on installing and running your application
 ## Testing
 > How was your project tested/validated? If you used CI, you should have a "build passing" badge in this README.
 
