# No Shortcuts Manifesto
© 2026 Jeremy Cox. Licensed under CC BY 4.0.
July 4, 2026
Congratulations!
250 Years of Colonial Independence

## Preamble

I am always getting myself into trouble. Not intentionally, not like an irresponsible person—just trying to do the right thing. Until it gets out of control. This time I outdid myself. This is my claim to notoriety.

One day, AI code gen blasted through a five-point ticket in two hours. I found myself with four whole extra days at the end of a three-week sprint. My good friend B.S. was slated to work on two tickets at the end of the sprint, and I messaged him: "It looks like you're in trouble. This is an eight-pointer, you need this three-pointer done first, and you haven't started yet?"

With good intentions, I loaded up the three-month-old branch he had started and the Jira issues. I went back and forth with Claude... Guess what? The team lead had put the wrong ticket in the sprint. This was actually the third ticket in the series. Okay—fine, I would research the first two. Next thing I knew, Claude had this enormous plan to implement 42 story points.

So I said to myself, "What's the worst that could happen?" I hit accept all changes.

Because this was a new feature—so-called "greenfield"—Claude Code (with Claude Opus 4.6) blasted through with alacrity. In six days, I had coded up and demonstrated 42 story points to my product owner.

Here I was left holding the bag. I did nine weeks' work in six days. I had a volume of code bordering on 8,000 lines. B.S. volunteered to review the code. He hated it. It was simply too much. He despaired. What's worse, Claude could keep up with his feedback and proactively rewrite chunks before he had read them. It was... a learning experience. B.S. learned I was a bad friend (just kidding).

In one hand, we had what seemed like relatively stable and bug-free code. In the other, we didn't have the bandwidth to do the code review.

The realization is that those 42 story points weren't about writing code. They were about writing code ***well***, and that includes a time budget for code reviews. Let's call it a 50% split. I had just created a four-and-a-half-week-long code review.

---

We were muddling through when I challenged B.S., "Come on, we tested it. You don't need to read all the code!"

Thankfully, B.S. was a no-nonsense kind of guy. He refused to compromise, take shortcuts, or take AI's seemingly good code on credit. He is the hero of this story.

It was horrible. We barely got the code review completed in six weeks. But there it was: our beautiful new feature.

But we were haunted by a burning question: How can we make the code review faster?

The tempting answer: lean into AI code review and AI software factories; remove the human. Let AI solve the AI problem.

A purist at heart, B.S. refused to compromise again. "How do you know it's good if you don't read it?" He pointed out that he had seen AI do foolish things. Straight-up dumb. You do not trust people like that.

B.S. hit on a core truth. Using AI to proofread AI is not fixing the disease; you're treating the symptom by rubbing the disease into it.
And you're removing the one thing that makes software good—human judgment.

And thus I began my journey to figure out how to take no shortcuts and maintain workflow quality and rigor.

---

The answer to this riddle lies not in generating code faster, but in crafting code with engineering rigor.

Amid the many talks I attended on AI code generation, one point stood out in my mind and has stood the test of time. "AI LLM technology's job is to minimize your pain points." The speaker was introducing RAG. The agent was going to read every technical document the team had written in 20 years and use it as source material for me. Genius. Less pain indeed.

But wait—the wizened words stuck with me. AI isn't here to make me more efficient? It's not here to do my work for me? It's not here to generate code like a firehose? It's here to make my life easier.

Someone paraphrased this to me as "AI gives you time back." What a delicious question to ask: "What do I want to do with all my extra time?" I found most people wanted to reinvest in coding, so they would just do more in the same amount of time. That is not a bad answer. But I went straight to my product owner and said, "I've got free time. Let's work on technical debt. I hate this offline data mode we have..." My thought process went straight to, "I know I skip steps when I do my job. Documentation. Unit tests. Design. My product owner is on my case to add these things to the Jira ticket. I don't have the time. But now I do."

So I set forth on my second experiment. What if I invested this extra time in doing the job right, without *skipping steps*? What will happen?

---

### Focusing on Speed Misses the Opportunity

Everyone loves to race. So the idea of writing code faster is intoxicating—it is fun—and it tugs at our primal instincts to compete. AI Code Gen sucks you into its world, and you do not want to leave. But do you really want to live there?

Software has been stuck in the corporate world too long. Somehow the Agile software movement got twisted and corrupted into justifying "get features out to the customer faster." The Agile software movement was about how to do our job right, making a stand against "the man" to let us do it right. Deadlines. Ship code. Somewhere, the mentality became "customers are paying for features." Not features that work, not code that is good, just a new doodad on the dashboard. We have witnessed that customers no longer expect code to work right the first time they get it. Look at how poorly the video game industry performs. They ship broken products and expect the people who bought the game to report bugs for them. Production is the new beta test.

We stand at a crossroads. We can either use AI Code Gen to make more slop at a faster pace, or we can use AI Code Gen to make better code. The happy accident I discovered is that better-engineered code gets written faster end to end. That much seems obvious in hindsight. We all know about the technical-debt tax that is the consequence of sloppy coding. Yet this insight goes deeper.

> Better-engineered code gets written faster end to end.

Not only do you have less technical debt, saving you time downstream—the task of writing the code from inception to code review to testing takes less total time.

It is time for all of us to pivot. By using the time AI gives developers back, developers can finally write software the correct way.

### Correctness Is Glorious

Better code doesn't just save time downstream. It takes less total time from inception to code review.

Programmers with AI are running around reveling in speed. How quickly we've forgotten the pain of spending two weeks writing a feature, only to realize with two days left that the design would be so much simpler if only we had used five global variables. A mentor once told me that we write the code three times. "You do a proof of concept to convince someone to let you write it. You write the code. Then you come back and write the code again the right way. Wait, just kidding—I'm not going to pay you to write it *again*."

What if we lived in a world where coding was fast enough that, when we make some really smelly code, we are allowed to throw it out?

We all want to do the job right; it's just that our hands are tied. Who cares about working faster? If the only innovation AI brings to the rat race is a bigger wheel, then I'll pass.

Doing things right is invaluable. And you have never gotten to try it. That changes today. You have the freedom to direct your extra time toward what you think matters: the big problems that you cannot squeeze into your schedule. Pursue the winning strategy that your company just couldn't afford the time to implement. I can see it in your eyes: you already have the big fish you are going after in mind.

### Fix Your Thinking

Look at AI code gen as a tool that enables you to do what you always wanted to do. Suddenly, it is not an existential job threat—AI code gen is the secret to your success.

Unleashing AI code gen's potential is about thinking strategically—not tactically—about time savings. What could you do if you no longer had to worry about deadlines? Dare to dream. Now go do it.

> AI code gen is the secret to your success: do what you always wanted to do.

### Mountain In, Mountains Out

I propose a thought experiment. You can spend as much time as you like planning and designing your software, but you only have one week of development time. Is it possible to design something so well that the code flows forth smoothly wihtout inhibitions?

I would have said "not possible" three months ago. But I now believe this is true. Writing code is busy work—it is a lot of ***exhaustive typing***. What I am doing when I write code is not typing out sentences translated into some goofy syntax. I spend my time thinking, planning, seeing ten steps ahead, and visualizing data flows in my head. For me, it is frustrating that I can't type faster. I can see it all in my head, but this keyboard is so slow.

> I think. It types.

By spending time thinking, formulating, and carefully considering design choices, I am making great code. It's just not typed yet! This is the miracle of AI Code Gen. It can take that masterfully crafted plan you created and execute your vision with prejudice.

By actually doing our jobs—engineering software—we make a much better product.

> Mountain In, Mountains Out

By putting a large amount of well-structured input into the AI, we will get an avalanche of high-quality output.

### How You Climb the Mountain

"Hey Jeremy, why didn't I just think to do my job right?" I am frustrated, too. A vision easily described is not so easy to execute.

The core idea is to spend time on engineering activities before ever going to code generation. We flip it upside down. Currently, I estimate that 80% of the time is spent coding and debugging. Now we're going to focus on design first: 80% on design instead of 80% on coding. I feel a bit flippant saying that; in reality, your coding time will be split about 50% planning and 50% code gen.

> Time well spent: 80% on design first instead of 80% on coding.

#### Same Workflow. Completely Different Inside

The workflow still revolves around a programmer taking a ticket, writing code, testing, and then a merge request. The fundamentals stay the same. How we work must completely change.

> Don't take shortcuts. Do it right.

We make really detailed tickets with clear program behavior and goals.
We talk back and forth with the AI, using pair programming to plan and explore design decisions.
We document designs and implementation plans.
We supervise the AI code gen process and steer it when it gets off course.
We follow good programming practice—stop and write unit tests frequently.
We use AI to help us review our code. It can summarize the code and point us to areas we think are critical.
We are willing to throw away code that's bad. If it's flawed, we can afford to replace it.

When I started doing all these things, something equally amazing and unexpected happened. The code review process began to go faster. Reviewers can come in and read the design before they look at the code. They can evaluate at a high level where this is headed. The code is cleaner and neater, well-commented, and has an easy flow. There are legitimately fewer bugs to create swirl.

The code review didn't get faster because we reviewed less carefully. It got faster because there was less to worry about.

## The No Shortcuts Framework

The story is personal. The standard is not.

The lesson is not that AI code gen should be slowed down. The lesson is that engineering must evolve to catch up with it.

> Forget about working faster. Focus now on doing a better job.  A complete job.

AI can generate code at a pace that would have seemed absurd a year ago. That does not make the hard parts of software development easier. Requirements can still be unclear. Designs can still be wrong. Systems can still be fragile. Tests can still miss what matters. Reviewers can still be overwhelmed. And a confident-looking answer can still be foolish.

The purpose of **No Shortcuts** is not to generate more code. It is to use the time AI gives us back to do the job correctly.

> AI gave us time back. Use it like engineers.

No Shortcuts is built on six pillars. Together, they preserve the workflow we already know—ticket, code, test, code review—while changing the discipline inside every step.

The process does not need to be replaced. How we work does.

---

### The Thesis: Do the Job Right

For years, developers have been forced to make tradeoffs we did not want to make.

We skip the design document because the sprint is moving. We defer the unit tests because the feature is almost done. We leave the ticket vague because everyone has a rough idea. We accept awkward code because rewriting it would take too long. We tell ourselves we will document it later.

Later rarely comes.

AI changes the economics of that work. It reduces the cost of turning a good plan into code. That is not permission to lower the bar. It is the opportunity to finally meet it.

**Do the Job Right** is not one task in the workflow. It is the governing idea behind all of them.

A completed feature is not merely code that compiles. It is understood, designed, tested, documented, reviewable, and maintainable.

> AI writes the code. You write the software.

---

### Pillar I — Define the Work Before You Build It

A weak ticket does not become a strong feature because an AI touched it.

Before code generation begins, the team needs a shared understanding of the problem, the intended behavior, the constraints, and the definition of done. AI can help expose ambiguity, find missing cases, and challenge assumptions. It cannot decide what the business actually needs.

This pillar contains four principles.

#### Principle 1 — Complete Expectations

Write the ticket right.

A ticket is not merely a request to begin coding. It is the first engineering artifact. It should explain the problem being solved, the desired behavior, success criteria, affected components, constraints, known risks, and open questions.

A good ticket gives the developer and the reviewer something concrete to agree on before implementation begins.

Where behavior matters, state it plainly. Where uncertainty exists, write it down. Where a decision is still needed, surface it instead of quietly guessing. A common mistake is to start talking about how. You need to define what you want; defer how to build it until work starts.

> Do not focus on how to implement the ticket; rather what it will accomplish.

Decompose the goal into verifiable slices of functionality. Each slice should carry a definition of done you can actually check—concrete results someone can confirm. It must be verifiable. Slicing the work this way is what keeps a ticket bounded and reviewable.

The goal is not bureaucratic perfection. The goal is an unambiguous definition of done.

> If it surprises your reviewer, you were not done planning.

#### Principle 2 — Design It Out Fully

When you start to code, don't write a single line. Do the hard thinking before asking the AI to type.

AI code generation is strongest when it executes a well-considered solution. It is weakest when it is asked to discover the problem, choose the architecture, invent missing requirements, and generate production code all at once. This is the failure of vibe coding.

Develop the solution with the model before generating large amounts of implementation code. Explore the data flow. Identify integration points. Consider failure modes. Challenge tradeoffs. Determine what belongs in scope and what does not. Write down the plan.

After all that hard work, save the plan in the repository. A useful implementation plan is not a disposable chat transcript. It is part of the engineering record. It helps future developers understand the decision, gives reviewers a high-level artifact to evaluate, and can be retrieved later through repository search or RAG.

#### Principle 3 — Just-In-Time Planning

The ticket says WHAT you want to accomplish. It defers the HOW until planning time.

A ticket that dictates the implementation is a ticket that will be wrong. The early work changes the later interfaces, so a HOW written too soon gets invalidated by what you learn while building. State the goal, the behavior, and the definition of done.  Choices regarding how to implement are made with the starting code state in mind.  

> The ticket can't predict the future code state, so don't try.

The same holds across a multi-issue feature: do not pre-plan the whole thing into a pile of tickets up front. Plan deeply, but create the next unit of work just in time—once the work ahead of it is stable. This keeps the "mountain in" without building a mountain you will have to demolish.

Where WHAT ends and HOW begins is not a clean line. It is an art form. But the discipline of drawing it is what keeps a ticket bounded, reviewable, and cheap to change.

#### Principle 4 — Preserve the Record

AI code gen creates an implementation plan. This serves as a landmark of intention and design before work begins. Annotate plans at the end with how they changed and evolved. The plan is a digest, a readable summary for each ticket. This is important for the reviewer to consider and also proves that the human did the engineering work. It is a cohesive document reflecting the thought process, not a diff scattered across code and design files.

The plan is not a description of the system as it stands today. It is a moment frozen in time. It will diverge from the documents over time. It preserves the engineering decisions.

> The ticket is the design. The design is the ticket.

Documentation as code is the innovation. Enable documentation to reach critical mass and guide AI code gen. The AI writes up what you ask of it. Garbage in, garbage out. Documents full of constraints have quality baked into every request.
 
> I can say anecdotally that the LLM has surprised me in a good way when I am planning and coding. "This is out of scope for this ticket; that upgrade is planned for ticket 12345." I was floored. How did it know that? Because I keep documenting the work I do, and it read it somewhere. Claude keeps sticking ticket-number references in comments in my code. Marginally useful to a human, but apparently a cross-reference gold mine to Claude. You will reach a critical mass where Claude knows your well-documented project very well.

---

### Pillar II — Engineer the Whole Product

Code is not the product. Code is one part of the product.

The feature also includes tests, documentation, observability, integration behavior, failure handling, maintainability, and the reasoning that makes non-obvious decisions understandable. AI gives us a chance to stop treating those things as optional work that happens only when the schedule allows.

#### Principle 5 — Do the Job Right

Use the time AI gives back to do what you never had time to do.

Write the unit tests. Clarify the ticket. Document the design. Clean up the abstraction. Investigate the edge case. Improve the logging. Fix the technical debt that makes every future change slower.

These are not indulgences. They are the work.

For too long, “faster” has meant ***taking a shortcut*** and making someone else pay for it later. The poor product "pays" for it. AI lets us break that bargain.

> Faster code is not better code. Better code is faster end to end.

#### Principle 6 — Simultaneous Outputs

Generate complete engineering outputs together.

A well-developed plan allows AI to help produce code, unit tests, integration tests, documentation, logging, and related configuration in the same working session. These should not be treated as a long sequence of tasks where quality is postponed until after the feature is “done.”

The code, tests, and supporting artifacts should reinforce one another.

That does not mean accepting them all blindly. It means using AI's speed to build a complete slice of the feature while the design is fresh in your mind.

#### Principle 7 — Documentation Is the Source of Truth

Creating documentation in the repository serves two purposes: to help humans understand the code and to help the AI code gen agent understand the code. The docs describe the current state of the system and how the parts relate to one another. That imposes an obligation a plan does not carry: when the code changes, the document must change with it. A document that describes a system that no longer exists is not neutral—it actively misleads, and a stale source of truth is worse than none at all. Fixing it is part of the definition of done.

> The feature is not done when the code exists. It is done when the engineering exists.

In principle, the docs are always accurate. Drift is caught and corrected at code review. However, drift does happen and requires correction. Keeping documentation true is ongoing work that demands vigilance and rigor, whether corrected with each change or swept up on a regular cadence.

Now do something radical: commit it to the repository. Commit the coding standards and plans to the repository.

> Join the documentation-as-code revolution.

Documentation creates the critical mass for AI code gen to create a consistent, engineered product.

---

### Pillar III — Direct the AI; Do Not Follow It

The model is a powerful collaborator. It is not the engineer in charge.

AI can identify risks you had not considered, propose alternatives, summarize unfamiliar code, and help explore a design more quickly than any individual can alone. It can also over-design, expand scope, misread a constraint, invent an abstraction, or confidently pursue a solution to the wrong problem.

> The AI is the most well-educated, hardest-working intern you will ever have. Supervise it.

The human remains accountable.

> The human in the loop is doing the engineering.

#### Principle 8 — AI as Thought Partner

Use AI to help you think, not merely to type.

The best AI-assisted work is a conversation. Bring the model the ticket, the source context, the architecture, the constraints, and the concerns you already have. Ask it what you may be missing. Ask it to distinguish facts from assumptions. Ask it to challenge the plan before it implements the plan.

A good developer does not simply prompt for output. A good developer directs the discussion.

> An AI LLM provides a collaborator who brings massive experience. From now on, you work with two heads instead of one.

That includes a new skill: learning the tendencies of the model you are working with. Different models are eager in different ways. Some push toward action. Some over-question. Some over-design. Some are too willing to make a plausible assumption and keep moving.

You must learn to hear the difference between a legitimate concern, a useful alternative, a speculative complication, and a foolish divergence.

Sometimes the correct response is, “That is a real issue; let us investigate it.” Sometimes it is, “Stop. That is not the problem we are solving.”

> AI fluency is not prompt writing. It is engineering judgment applied through a new interface.

Repository instructions, such as `CLAUDE.md`, can establish helpful defaults: plan first, ask questions early, respect explicit constraints, do not expand scope, and investigate before acting. They are valuable because they keep the model from repeatedly relearning the team's working style.

> AI cannot make judgments.

But instructions are not judgment. They cannot replace understanding the system well enough to know when the model is wrong.

#### Principle 9 — Human in the Loop — Always

The human is not optional.

Do not take AI's code on credit. Do not outsource responsibility to a model because its answer is polished, thorough, or fast.

Watch generated work carefully. Stop it when it goes off course. Read the code. Test the behavior. Verify claims against the actual system. Require human judgment where it matters.

Use AI to summarize changes, identify areas of risk, explain unfamiliar code, and help a reviewer navigate a large merge request. Do not use AI as an excuse to remove the one part of the process that makes software trustworthy. Do not compromise good work for speed.

> Trust but verify. Mostly verify.

This connects all the way back to the ticket. The goal and the goalposts *should* already be defined.

> Using AI to proofread AI is not fixing the disease. You are treating the symptom by rubbing the disease into it.

---

### Pillar IV — Fail Cheap, Learn Early

AI speed is most useful when it shortens the distance between an idea and meaningful feedback.

The purpose is not to hide the work from other people until a massive branch is ready. The purpose is to make it easier to show a real thing, learn what is wrong, and adjust before weak assumptions become expensive.

#### Principle 10 — Compress the Feedback Loop

Get feedback while the work is still cheap to change.

> AI-generated code is always cheap to change.

Use prototypes, design walkthroughs, focused demos, and early test runs to give people something real to react to. A conversation about an imagined feature is useful. A conversation about a working version of the feature is better. What is better than a wireframe you discuss for an hour with four other people? Three demos of slightly different flavors of the feature as a conversation starters.

This applies to technical feedback as well as product feedback. The sooner a reviewer sees the plan, the sooner they can question the design. The sooner a teammate sees a prototype, the sooner they can point out a workflow problem. The sooner a test exposes a false assumption, the sooner you can change course.

> Reducing the coding time means you have more time afterward for feedback.

Code review is not a safety net for a feature that has already become too large to understand. It is a finish line for work that has already been made reviewable.

> The code review did not get faster because we reviewed less carefully. It got faster because there was less to worry about.

---

### Pillar V — Preserve the Freedom to Change Course

The cost of code has fallen. The cost of being wrong has not.

AI makes it cheaper to explore, prototype, revise, and restart. That should make us less attached to flawed work—not more willing to ship it because the first version arrived quickly.

This pillar contains two principles.

#### Principle 11 — Reset Without Fear

Be willing to throw away code that is wrong.

A prototype can reveal that the ticket was misunderstood. A design conversation can expose a missing requirement. A review can show that the approach is awkward even though the code technically works. A test can demonstrate that the abstraction was wrong from the beginning.

When that happens, reset.

> Every programmer's dream: start over and do it right.

Do not defend bad code because it took effort to produce. Do not preserve a weak design because it is already half implemented. Do not confuse a working demo with a sound solution.

Low sunk cost is not a reason to be careless. It is a strategic advantage: it gives us permission to make a better decision when we learn something new.

#### Principle 12 — Keep Work Units Small

Echoing the need to decompose, your work units are only disposable so long as the cost of replacement is cheap.
A slice you can throw away in an afternoon is a slice you will throw away when it is wrong. For the developer, this emphasizes the need to break down tasks into subtasks: stop, review, and test frequently.

Even if your tickets aren't small, you can work with the LLM when it creates its implementation plan to keep the SDLC loop tight. Stop after each step, compile, and run your new tests.

> Do not create problems you then have to solve at review.

When you stop between steps, ask Claude or a different Claude session to do a code review. It will catch mistakes. It will make you think. And maybe it will give you reason to change course.

> Sunk cost is cheaper when the code took two hours. Throwing code out has never been easier.

Seek feedback quickly from yourself, Claude, and unit tests.

---

### Pillar VI — Code Review Is Not Optional

AI can help with code review. It can summarize a change, trace data flow, identify risk, explain unfamiliar code, and suggest where a reviewer should look first. It cannot be the reviewer of record.

> The human in the loop supervises the AI. The AI never supervises the human.

#### Principle 13 — Human Review Is the Merge Gate

Every production change requires human review. Tests are evidence, not understanding. A green build does not prove that the design is sound, the implementation is maintainable, or the change does what the ticket intended.

> Finally, a third programmer enters the arena.

A reviewer must understand the purpose of the change, evaluate the design, inspect the implementation, and be willing to share responsibility for what is merged. AI can support that judgment. It cannot replace it.

> Code review time is development time.

#### Principle 14 — Better Engineering, Better Code, Faster Reviews

I started my journey seeking a way to review AI-generated code.

The answer is to make it more palatable. Better engineering and better AI guardrails mean fewer mistakes and greater consistency. The code is simply cleaner and easier to read.

> If no human understands the change, the change is not ready.

Coding standards are already enforced. Extensive comments exist. Documentation and plans cross-reference the work.

The focus here is on doing more engineering. That extends to the review. Documentation as code enables the reviewer. The reviewer can see what you planned to do, why you planned it, and how you designed it *before* reading a single line of code. Instead of having to assemble it all from the bottom up during the review—which takes time—the reviewer can simply read it. "The gist" is given up front.

> The answer to overwhelming AI output is not less review. It is more reviewable work.

---

Co-authored with Claude Opus 4.8, ChatGPT 5.5, and peer reviewers.
