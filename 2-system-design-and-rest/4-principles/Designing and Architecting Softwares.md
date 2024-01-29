# Designing and Architecting Softwares

1. My approach for designing and architecting software. I thought might help some of you guys.

2. I block 2-3 hours of uninterrupted time slots. No meetings, emails or any notification. I use a note app that is clutter free (I use write-monkey for Windows & Focus for Mac) full screen dark mode. This way its only me and what I type.

3. I first start writing the workflow of how the software will be used in detailed length. I leave nothing out. There is a magical thing of stating the obvious that helps the ideas and creativity freely roam. This step produces many questions to the project's stakeholders

4. I compile the questions raised from the workflow step and meet with the stakeholders to get a final say on the workflow. Part of the workflow would then turn into a min-ship. The final workflow becomes available for non-technical people interested in the project.

5. Next step is I open a new page in write-monkey and start writing down the design overview. The design overview explains how users interact with the software and what really happens. It is a technical representation of the workflow, in this step I can freely use technical terms.

6. The design overview includes write-ups of different components of the software, the UX, UI, frontend, backend, databases etc. It also includes how the components interact with each other, referencing the workflow when applicable.  No diagrams yet.

7. Some items in the overview design won't be linked back to the workflow, such as asynchronous jobs or health checks that doesn't have a direct user input.

8. The design overview also helps me articulate things that I have never thought about. Here is where things started to form, what database would I need, what reverse proxy should I use, how would the backend scale, would eager vs lazy approach be better. Again no diagrams.

9. Next step is to open a new page of write-monkey for each component and write in details what that component is, what does it interface with, what does it compute, what does it output etc. I am allowed to go full technical mode here.

10. Final step after writing all those pieces is to draw the design overview diagram. It is a diagram of how all those components communicate with each other. I don't use a special software here, just blocks and squares and arrows with text. simple. Google slides work perfectly.

11. There would probably be multiple diagrams for each component based on the complexity of the system. Plus I would schedule reviews with team members every now and then.  Hope that helped (L).