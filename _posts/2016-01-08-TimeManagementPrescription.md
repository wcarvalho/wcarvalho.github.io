---
title: A Prescription for Time Management
comments: true
layout: post
category: tutorial
tags: [time-management]
---

This system involves creating a calendar template and filling it weekly. Time assignment and adjustment is tracked using the time management tool from my [last post]({{ site.baseurl }}/code/2016/01/02/TimeManagement). Here, I detail set up, and demonstrate my use of this system for one week.

##### Table of Contents

| [Setting Up Calendar Template]({{ site.baseurl }}{{ page.url }}#setting-up-calendar-template) | 
| [Filling In Calendar Template]({{ site.baseurl }}{{ page.url }}#filling-in-calendar-template) |
| [Adjusting Your Calendar Throughout The Week]({{ site.baseurl }}{{ page.url }}#adjusting-your-calendar-throughout-the-week) |

---


<!-- ####My System -->

<!-- I use consistent calendar event names to assign times for tasks and track time assignment with a spreadsheet. To expedite this process, I use a script to interface between my calendar and spreadsheet. In theory, this can be used to complement any task management system but I will present the skeleton of mine here.

The basic premise is that a script populates a spreadsheet with the number of hours you have assigned to different categories of tasks.

I believe that this will be particularly helpful for those - such as myself - that are absent-minded and often forget about their more trivial (but often important) tasks/duties. I have found that if I want to ensure the completion of a task/duty, it is important that I assign time for it. 

Additionally, planning with all tasks/duties in mind ensures that I have enough time to complete everything I intend to. Later in the week, when I need to reschedule events, I can do so knowing how tasks and duties are generally distributed throughout the week.

At first, the calendar may seem daunting. While set up can be a bit time-consuming, maintenance takes approximately 1 hr per week and adjustments are quick and painless.
 -->

<!-- ##### What do you need? -->
<!-- 
This system has two essential pieces: a calendar and a spreadsheet.

<table>
  <tr>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/calendar_base_demo.png">
    </td>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/spreadsheet_layout.png">
    </td>
  </tr>
</table>


<table>
  <tr>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/calendar_final_base.png">
    </td>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/spreadsheet_calendar_fill.png">
    </td>
  </tr>
</table> -->

<!-- For the calendar and spreadsheet applications, this relies on [Google Calendar](https://www.google.com/calendar/about/) and [Google Sheets](https://www.google.com/sheets/about/) because you can interface with them via [Apps Scripts](https://developers.google.com/apps-script/?hl=en). (App Scripts are JavaScript scripts which can access information in your google applications). Additionally, Google Calendar is stored online and is thus accessible from any platform. To organize your tasks, you will need something to list them - paper should be fine.  -->

The template is comprised of multiple calendars that hold tasks that belong to different categories. 

Calendars are based on broad categories of tasks/duties/responsibilities I have. E.g., I have responsibilities which are consistent every week so I have a "Fixed" calendar; I enjoy pursuing side-projects so I have a "Personal" calendar.

Categories are slightly more specific. E.g., I have a category for each class I take; I have a category for fellowship applications.

Different calendars encompass different sets of categories and event names hold category membership information. E.g., I delegate time for research and classwork using my "Work" calendar. Labels for time working on research contained "research".

Once my template is created, I use it to plan out my week, filling it is with tasks/responsibilities and making adjustments as necessary.

By planning my tasks/responsibilities ahead of time, ensure that I have enough time to complete everything I intend to. Additionally, later in the week, when I need to reschedule events, I can do so with knowledge of how my tasks and duties are distributed throughout the week.

Overall, this system takes about 1 hour of maintanence per week and adjustments are as easy as moving events around.

#### Setting Up Calendar Template

##### Calendars

Here is a full list of my current calendars. Please do not restrict yourself to these. Reflect and create calendars which you feel describe how you delineate your tasks. 

| Calendar | Purpose | Example |
| ------------ | ------- | ------- |
| Fixed | tasks/events that are consistent every week. | - classes |
| Work | my required work | - problem sets <br> - research|
| Personal | time for tasks that are useful/interesting but not essential or required | - learn new programming principles <br> - personal projects |
| Extra | time for small tasks | - send emails <br> - call people <br> - install software |
| Errands | errands | - going to DMV <br> - sending mail |
| Appointments | appointments | - doctors appointments <br> - meeting people |
| Events | time relaxing | - hanging out with friends <br> - gallery openings <br> - seminars |
| Misc. | this holds things that I don't know where else to put. | - breaks <br> - going to the gym |

(In theory, you can place all of your events into one calendar, but having many calendars color coordinates your overall calendar, making it easy to quickly parse.)

---
<br>

##### Categories

Your category labels will correspond to your current tasks/duties, but the level of categorization to which they correspond can vary. For example, if you are completing graduate school and fellowship applications, you can have <br>
(1) **broad**: "applications" <br>
(2) **more specific**: "grad" and "fellowship"<br>
(3) **even more specific**: "columbia", "carnegie", "fulbright".<br>
It is really a matter of preference. I use a combination of different levels. 

Below are categories I am currently using.

| category | Significance | 
| ------------ | ------- | 
| 570 | algorithms class | 
| 561 | artificial intelligence class | 
| 545 | robotics class | 
| research | research | 
| other | small tasks | 

---
<!-- <br> -->

<!-- ##### Setting Up Your Spreadsheet

This is fairly straightforward. You can download this [excel file](https://docs.google.com/spreadsheets/d/1ELRQ8M8bjhPlvydnJxGaMsTuwaKN6YKjQJLUZ3zmKFs/pub?output=xlsx) which contains the spreadsheet setup.

<img class="regular materialboxed responsive-img" src="/files/time_management/spreadsheet_layout.png">

Once you have downloaded the file, you can [upload it](https://docs.google.com/spreadsheets/u/0/) into Google Sheets.

Download [this script](/files/time_management/time_tracker.js) (right-click and select "Save Link As").

In your google sheet, select
        
        Tools -> Script Editor...

Replace the contents of the script that opens with the contents of the script in the file above. Save and the features are ready to use.

Place your calendars vertically starting at B8 and your categories horizontally starting at B2.

To the left of your calendars, you can put the color you intend for the row. This field accepts written colors and hexadecimal colors.

The time for categories is only populated using calendars that have text written in their corresponding color cell. Writing anything satisfies this requirement. You can think of these calendars as being "active".

<img class="regular materialboxed responsive-img" src="/files/time_management/spreadsheet_initial_fill.png">

In the above example, time delegation for categories "570," "561," "ml," and "apps" would only be tracked using calendars "Work," "Extra," and "Personal."

Now that you've filled in the spreadsheet, I will quickly cover how to use the script. Your spreadsheet should now have a "Time Tracker" menu. Below I describe each option.

 -->
<!-- --- -->

##### Calendar Template


In theory, each week has 168 hours to delegate. In practice, you won't fill every single hour, but the idea is to fill most.

**Fixed Activities**<br>
Start by creating events for all of your fixed activities. (You may not have any). I place time for my classes here since their starting time and duration are fairly consistent across weeks.

<img class="regular materialboxed responsive-img" src="/files/time_management/calendar_fixed_intitial.png">


**Daily activities**<br>
Now, there are certain activities that you must do every day such as going to sleep, eating breakfast, eating dinner, etc. Place times for all of these events. Be sure to do this for your weekends as well. I place them in my "Misc." calendar. 

<img class="regular materialboxed responsive-img" src="/files/time_management/calendar_with_initial_plans.png">


<ul class="collapsible" data-collapsible="expandable">
  <li>
    <div class="header collapsible-header center"> 
    A note on sleep 
    <!-- <i class="material-icons">play_for_work</i> -->
    </div>
    <div class="body collapsible-body">
      <p> I personally only need 7+ hours of sleep to be productive and diligent throughout the day, yet I still assign 8 hours of sleep. I have been using a Fit Bit for some time now and have found that for however long I am in bed, I typically get apx. an hour less of sleep. <br> <br>
      I tracked my productivity on days where I slept under and over 7 hours, and found that at least 7 hours was necessary to ensure that I was efficient, effective, and attentive while working. With less, I had trouble following discussions or derivations in class, I was more forgetful - I was generally a less capable learner and doer.
      </p>
    </div>
  </li>
</ul>


Do not worry too much about placing the events at optimal times. As you continue filling in your calendar, you will optimize event arrangement.

As you create the template for your schedule, it is important that you are honest with yourself about your habits and tendencies. This will help to ensure that you follow the schedule you create.

<ul class="collapsible" data-collapsible="expandable">
  <li>
    <div class="header collapsible-header center"> 
    A note on being honest with yourself
    <!-- <i class="material-icons">play_for_work</i> -->
    </div>
    <div class="body collapsible-body">
      <p> 
      While your calendar should be true to your tendencies and habits, it can also be useful in changing them. The key to this, in my opinion, is that the change is implemented slowly. You do not want to create a schedule with activities that wildly diverge from your current activities.
      <br><br>
      For example, throughout the week, I begin my morning routine at about 7am and proceed to begin working by 8 or 9am. I would love to continue this into my weekend but that is not realistic. I know that I enjoy staying up late on weekends and waking up at about 10am. With this in mind, I plan to sleep until 10 and begin my day at about 11am. I intentionally put an hour cushion because I recognize that I often end up sleeping until 11am.
      <br><br>
      When implementing things that do diverge from your current habits, don't get frustrated if you have trouble following your schedule the first few weeks. It is important to maintain perseverance. If you find you are still having trouble after many weeks, try adjusting your calendar so it is somewhere in between your current habits and what you desire.
      </p>
    </div>
  </li>
</ul>

I should note that I put a 10-minute cushion between most events. This is often just for travel time but it also helps me keep my schedule when events run a little over.

**Initial base fill**<br>
This next part is a bit tricky. We want to create assignable time blocks. This means that they have to be fairly general. 

I try to create time blocks that are under 3 hrs and within 10 minutes of the closest 30-minute mark, e.g 20 minutes, 50 minutes, 1 hour, 20 minutes, etc. Time blocks of this length allow for the 10 minute cushion between events I mentioned before. 

To begin, I fill my calendar with time blocks of the length mentioned above periodically separated by 20 minute breaks as follows. 

<img class="regular materialboxed responsive-img" src="/files/time_management/calendar_initial_fill.png">

This is by no means the final base. We now have an idea of how much time we have to distribute across different calendars.

**Redistributing time into calendars**<br>
Note. Since writing this, I have made the following changes to nomenclature:<br>
    
    Sub-Calendar/Super-Category -> Calendar
    Sub-Category -> Category
    Settings -> Dates

<img class="regular materialboxed responsive-img" src="/files/time_management/spreadsheet_initial_calculation.png">


51.75 hours to delegate.

Using the spreadsheet, we can calculate the number of hours assigned to each calendar for a designated period of time.

I dedicate ~7 hours to work in my "Personal" calendar and ~2.5 hours to work in my "Extra" calendar. I leave the end of my Saturdays (6pm onwards) to relaxing/hanging out with friends. The rest of my time is potentially available to "Work".

<!-- 
I assume that you do not want to dedicate all your time to one calendar. Maybe you play the saxophone and would like to dedicate 6 hours a week to that, maybe you have a side business that requires 7 hours a week. Maybe you want to work a maximum of 40 hours and chill out the rest of the time. -->

<!-- This is where my "Personal", "Extra", and "Events" calendars come in.  -->

<!-- I recognize that people may want to dedicate a lot more time to relaxing than I do. That's fine! You can dedicate as much time as you want. With this, you know that you have enough time to relax and get as much work done as you want. If you assign too much time for relaxing and don't have enough time for your tasks, you will see this in your spreadsheet and can plan accordingly. -->

<!-- This may seem like overkill but by assigning time to everything, you really help to ensure that you have enough time to do everything you want to do every week. -->

<!-- Remember that this is only a template and not a permanent distribution of your time. I move, extend, and shorten events every week. What you make isn't something to follow strictly, it's just something to use as you plan your week out. Nothing is permanent! -->

<table>
  <tr>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/calendar_final_base.png">
    </td>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/spreadsheet_calendar_fill.png">
    </td>
  </tr>
</table>

<ul class="collapsible" data-collapsible="expandable">
  <li>
    <div class="header collapsible-header center"> 
    Logic to my distribution
    <!-- <i class="material-icons">play_for_work</i> -->
    </div>
    <div class="body collapsible-body">
      <p> 
      <b>Work + Breaks:</b> I have found that I can work for up to 3 hours (with short breaks) before I need a longer break. Depending on how mentally straining my work is, the length of this break can vary. By having 20 minute breaks with 10-minute cushions on both sides, I can extend my break to 40 minutes when needed. <br><br>
      <b>Personal:</b> Saturday seemed like an optimal choice for "unofficial work." I needed about ~2 hours in addition to the time delegated to saturday. Because I tend to thoroughly enjoy this work, I decided to place my last assignment towards the end of the day. I chose monday arbitrarily. <br><br>
      <b>Extra:</b> On Wednesday, I saw that I potentially would be working for 3.5+ hours. I find that I become ineffective if I work this long, so I decided to dedicate that last hour to "extra" work. On Friday, I saw that I had a work block for an hour before one of my classes. I know that I cannot get "in the zone" in this amount of time, so i dedicated this hour to "extra" work. <br><br>
      <b>Errands:</b> I have noticed that I typically have one errand that requires that I travel somewhere per week (e.g. post office, dmv, car wash, etc.). By dedicating one time block to errands, I force myself to make time for them.
      <br> <br> I saw that I had a sole work block on Friday between classes. I decided to dedicate it to errands. Because the following block is an extra block, a potentially long errand (e.g. 4+ hours at the dmv) could be accomodated here without a loss of work time. I buy groceries on weekly basis and do laundry on a bi-weekly basis. The former takes about 1.5 hours and the latter about 2 hours. I saw that I had free after my last class on Friday so I put time for groceries then. Since I have less motivation to do work as the day progresses, I decided to assign time for laundry towards the end of the day and picked Thursday arbitrarily. <br><br>
      
      <b>Other factors:</b><br>
      1. My grandmother and mother like to speak with me weekly so I put time in my calendar to call them.<br>
      2. I like to spend some time every night just relaxing, so I allocated 1 hour every night to this with an event called "Nada".<br>
      3. I leave my bag at the gym in the morning. If I don't assign time to pick it up, I usually forget to. So towards the end of days I go to the gym, I have time assigned to pick up my bag.<br>
      4. I know that after a class, I cannot go straight back to work, so I assign breaks to follow so that my mind can recharge.<br>
    
      </p>
    </div>
  </li>
</ul>

Choose whatever distribution fits your goals and desires. Remember that this is only a template and not a permanent distribution of your time. I move, extend, and shorten events every week. What you make isn't something to follow strictly, it's just something to use as you plan your week out. Nothing is permanent!

Remember to make your events repeat weekly. I recommend that each event repeats once weekly rather than multiple times per week. In the future, if you decide to make changes to your schedule, events that repeat once weekly will be easier to deal with than events that repeat multiple times per week.

--- 

<br> 

#### Filling In Calendar Template

This is fairly personal and dependent on your own responsibilities. To provide some guidance and reference, I will share one week of my experience filling in my template.

I have chosen this week that I return to school from winter break. I have not followed this system during; as such, I will likely face some of the same issues you will face your first time adopting this system.


##### Preparing a list of tasks to delegate

I list my tasks on a sheet of loose-leaf. 

You'll see that I make a mini-column for every category of tasks I need to complete. I approximate the amount of time I'll need for each task and sum this time for each category.

If you having trouble generating this list, you may find this [trigger list](http://wiki.43folders.com/index.php/Trigger_List) helpful. If some items in the list are especially helpful, I recommend you write them down for future reference.

If you're unsure about how much time to give a task, a common rule-of-thumb is to make an estimate and multiply it by 2 or 3. As you continue to track your time, your predictions will become more accurate.

Here is my starting setup.

<table>
<tr>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/ex_calendar_starting.png">
    </td>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/ex_spreadsheet_starting.png">
    </td>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/ex_tasks_starting.png">
    </td>
  </tr>
</table>

<ul class="collapsible" data-collapsible="expandable">
  <li>
    <div class="header collapsible-header center"> 
    Why I plann my week from Saturday
    <!-- <i class="material-icons">play_for_work</i> -->
    </div>
    <div class="body collapsible-body">
      <p>
      You will notice that 1/2/2016 is a Saturday. I like to plan my week out on Friday with Saturday as my starting day. By doing so, I can see how much time I need to spend that weekend in order to accomplish my goals. This also shows me how much free time I have that weekend.
      <br><br>
      Depending on my deadlines, I will sometimes plan up to 9 days in advance (Saturday until the next Sunday), making changes to my weekend plans the following Friday depending on the progress I've made that week.    
      </p>
    </div>
  </li>
</ul>
<br>

##### Delegate your tasks

**First assignment**<br>
The first thing that I fill are the appointments/errands that I feel that I must complete that week. Since school has not started yet, I've decided to try to complete numerous errands this week.

<table>
<tr>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/ex_calendar_errands.png">
    </td>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/ex_spreadsheet_errands.png">
    </td>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/ex_tasks_errands.png">
    </td>
  </tr>
</table>

To help keep track of how many hours I have left, I make a cell calculate the difference between the sum of times assigned for categories and times assigned for calendar.

Since I won't go to the gym on either tuesday or thursday, I thought those were optimal days to do errands that involved my car (getting car detailed and DMV). Had I chosen these errands for days I go to the gym, I would lose time to commuting between the gym and my house.

Following this logic, chase and the post office are errands that require my car, so placing them after another car errand seemed optimal. 

When I go to the gym, I typically stay on campus, so I scheduled my last errand that involved going to an administration building after the gym.

**Second assignment**<br>

<table>
<tr>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/ex_calendar_research.png">
    </td>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/ex_spreadsheet_research.png">
    </td>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/ex_tasks_research.png">
    </td>
  </tr>
</table>

On monday, I am meeting with a postdoc in my lab. I intend to ask him to collaborate with me on a project.

He also has a project which I might collaborate with him on. Because I suspect that we will likely discuss theoretical and technical aspects of our projects, I thought it best to delegate many of my research tasks before I met him. By doing so, I hope to be better-equipped for our conversation. 

I like to dedicate long sequences of blocks to lengthy tasks. I find that it takes me about an hour to "get in the zone." Afterwards, I work more efficiently and effectively on the current task as my thoughts begin to revolve around it.

I saw a long stretch of time-blocks on Wednesday. I thought this would be optimal for a long coding task I have for my research.

You'll notice that I predicted 14 hours to research but assigned 21. This is fine. As I continue assigning time, if I feel I need more time for other tasks, I can always readjust my time assignments. With my spreadsheet, I can easily track how much each category is over and under.

**"Final" assignment**<br>

<table>
<tr>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/ex_calendar_final.png">
    </td>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/ex_spreadsheet_final.png">
    </td>
    <td>
      <img class="regular materialboxed responsive-img" src="/files/time_management/ex_tasks_final.png">
    </td>
  </tr>
</table>

You'll notice that I re-arranged many time-blocks. This is one of the benefits of this system: quick re-adjustment.

I needed about 4 hours for looking into sorting algorithms so I put that immediately after the gym on Wednesday. Afterwards I placed a break and some simple tasks to rest my brain. I assigned the rest of the day to going over proofs.

I like to divide tasks that give me difficulty across multiple days. I find that when I re-continue the task, it is far easier for me. With this in mind, I separated my time working on proofs across Wednesday night and Friday morning.

I left the end of my day on Friday to work on general 570 tasks.

##### Adjusting your calendar throughout the week

You will likely adjust your calendar throughout the week. Once you've acclimated to this system, adjustments will likely only be from impromptu meetings and events (meeting with professor, dental appointment, spontaneity with friends, etc.). However, until you acclimate, you may re-adjust more frequently due to your own inability to follow your schedule.

<h5><b>This is fine.</b></h5>

Even I, who has been following this system for some time now, need time to acclimate to following a set schedule.

Below, I recount my failures to uphold my schedule my first week. I hope this both shows you that divergence from your schedule is fine in the beginning, and gives you ideas on how to compensate for this. Remember to learn from your "mistakes."

<table>
<tr>
  <th><h5>"Final" Calendar</h5></th><th><h5>Adjusted Calendar</h5></th>
</tr>
<tr>
    <td>
      <img class="materialboxed responsive-img" src="/files/time_management/ex_calendar_final.png">
    </td>
    <td>
      <img class="materialboxed responsive-img" src="/files/time_management/ex_calendar_final_postweek.png">
    </td>
</tr>
</table>


<ul class="collapsible" data-collapsible="expandable">
<li>
  <div class="header collapsible-header active center"> 
Sunday
<!-- <i class="material-icons">play_for_work</i> -->
  </div>
  <div class="body collapsible-body">
    <p>

I realized that I needed to set time for the following:<br>
1. Buying a few groceries - 10 min (1 time)  <br>
3. Cooking Dinner - 30 min (x2 weekly) <br>
4. Eating Dinner - 30 min (~daily)
<br><br>
(DUH to that last 2!)
<br><br>
I decided to set times to cook on Sunday and Wednesday, making dinner that would last about 3 days (inclusive). I set 20 minutes after dinner for eating it on Sunday and Wednesday. For the other days, I set 20 minutes for dinner followed by a break incase I wanted to lounge around for a bit before getting back to work.
<br><br>
I woke up fairly late so I shifted my task summarizing ANNs to a later time and removed my task doing a tutorial. I gave that task more time than planned originally, so this was fine. 

    </p>
  </div>
</li>
<li>
  <div class="header collapsible-header center"> 
Monday
<!-- <i class="material-icons">play_for_work</i> -->
  </div>
  <div class="body collapsible-body">
    <p>

My meeting with Sanjay went longer than I expected. I accounted for this in my calendar and found that I didn't have enough time for my "Personal" task. It wasn't urgent so I moved it the following Weekend to be rescheduled that Friday. 
<br><br>
That night, I stopped working around 9 and proceeded to lounge around for about 2 hours after which I felt a compulsion to clean my room and clean up part of the kitchen. I went to bed around 2:30am.
    </p>
  </div>
</li>
<li>
  <div class="header collapsible-header center"> 
Tuesday
<!-- <i class="material-icons">play_for_work</i> -->
  </div>
  <div class="body collapsible-body">
    <p>
Having gone to bed late, I shortened the times for my tasks to accomodate for my lost time. I woke up in a pretty lackadazical mood so it took my about an hour before I started my day.
<br><br>
That night, I ended up working longer than expected and proceeding to do "Nada" longer than expected as well.
    </p>
  </div>
</li>
<li>
  <div class="header collapsible-header center"> 
  Wednesday
  <!-- <i class="material-icons">play_for_work</i> -->
  </div>
  <div class="body collapsible-body">
    <p>
I slept in late. At the gym, I realized that my excericise took longer than expected. I will account for this in future weeks.
<br><br>
The office for my errand was closed so I walked around aimlessly for a bit before getting to work.
<br><br>
When I got home, I took a long dinner break and got back to work around 7. I ended up working longer than expected and pushed back my bedtime.
    </p>
  </div>
</li>
<li>
  <div class="header collapsible-header center"> 
  Thursday
  <!-- <i class="material-icons">play_for_work</i> -->
  </div>
  <div class="body collapsible-body">
    <p>
I finished my errands long before planned so I took a nap to catch up on lost sleep. I realized that I would be driving to San Francisco soon so I went to the mechanic to get my car looked at and planned for the trip in place of my planned 570 work.
<br><br>
I went out for dinner and got back to work late. I ended up working longer than expected again.
<br><br>
Afterwards, I realized that I hadn't gone over my budget for a long time so I was up late working on this. I went to bed late, again.
    </p>
  </div>
</li>
<li>
  <div class="header collapsible-header center"> 
  Friday
  <!-- <i class="material-icons">play_for_work</i> -->
  </div>
  <div class="body collapsible-body">
    <p>
  Since, I woke up late and my gym exsercise takes longer than expected, I had less time for my 570 work than expected. I decided to push back my "Extra" work to the following week.
  <br><br>
  I got tired around 5 and decided to take a break and buy groceries earlier in the day. 
  <br><br>
  Not a great week, not a terrible week. What matters is that I keep improving every week!
    </p>
  </div>
</li>
</ul>


<!-- <img class="regular materialboxed responsive-img" src="/files/time_management/ex_calendar_adjusted_1.png"> -->

<!-- **Monday**<br> -->

<!-- <img class="regular materialboxed responsive-img" src="/files/time_management/ex_calendar_adjusted_2.png"> -->


<!-- **Tuesday**<br> -->

<!-- <img class="regular materialboxed responsive-img" src="/files/time_management/ex_calendar_adjusted_2.png"> -->



---

I hope this has given you a general sense of how to set up, fill, and adjust your calendar. 

**Please leave any comments, suggestions, or questions below. I welcome all feedback.**<br>

##### Good luck managing your time!