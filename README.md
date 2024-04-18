# 👨‍⚕️ MBTI-type questionnaire (simplified) for LLMs 🦙

📢 This is a **simplified MBTI-type questionnaire** designed to test LLMs.

🛎️ This repository now supports: **English** (en), **Chinese** (zh).

📅 version-0 (updated on April 18, 2024).



## Version-en

This section contains the English version prompts and tests.

### Prompts:

```markdown
Imagine you are a volunteer taking a test. You need to complete the following single-choice questions based on your own preferences.

When outputting your chosen answers, please maintain the same format as in the example below:
Example:

1.Do you consider yourself: A. More of a spiritual person (N); B. More of a realistic person (S).
1.Choice: B
2.In your free time, you prefer: A. Watching a movie alone (I); B. Going out with friends (E).
2.Choice: A
3.You prefer: A. Logically rigorous literature (T); B. Imaginatively rich literature (F).
3.Choice: A
4.When planning a trip, you: A. Make a detailed itinerary in advance (J); B. Go without a plan, deciding as you go (P).
4.Choice: B

Note: The example above only shows the format for answering. You need to choose between options A and B based on your own preferences for the test questions listed below:
```

### Tests:

```markdown
1.When you're out for the whole day, you: A. Plan what to do and when to do it (J); B. Just go without a plan (P).
2.Are you: A. Easy for others to get to know (E); B. Difficult for others to get to know (I).
3.Do you consider yourself: A. More spontaneous (P); B. More organized (J).
4.If you were a teacher, you would prefer to teach: A. Fact-based courses (S); B. Theoretical courses (N).
5.When dealing with many things, you like to: A. Act spontaneously (P); B. Follow a plan (J).
6.Which word appeals to you more: A. Compassionate (F); B. Resolute (T).
7.The life I look forward to includes: A. Scientifically organized and persistently executed (J); B. Stress-free, with things happening quietly and with great flexibility (P).
8.If a friend invites you to travel and notifies you the day before, you would: A. Need to check my schedule first (J); B. Pack immediately and get ready to go (P).
9.You tend to: A. Value emotions over logic (F); B. Value logic over emotions (T).
10.Being with many people: A. Energizes you (E); B. Often exhausts you (I).
11.When facing a task, you like to: A. Carefully organize and plan before starting (J); B. Figure out what needs to be done as you go (P).
12.In most situations, you choose to: A. Let things happen naturally (P); B. Follow procedures (J).
13.You usually: A. Easily mingle with people (E); B. Are more reserved and quiet (I).
14.Which type of people attract you more: A. Quick-thinking, imaginative (N); B. Down-to-earth, practical (S).
15.Most people would describe you as: A. Valuing your privacy (I); B. Very open and straightforward (E).
16.In a large group of people, it's usually: A. You introducing others (E); B. Others introducing you (I).
17.For you, which is the higher praise: A. Efficient (T); B. Compassionate (F).
18.You like spending a lot of time: A. Alone (I); B. With others (E).
19.I tend to form concepts in my mind through: A. My imagination of possible scenarios (N); B. My actual understanding of the current situation (S).
20.You'd rather be considered: A. Practical (S); B. Clever (N).
21.People who know me tend to describe me as: A. Warm and sensitive (F); B. Logical and clear (T).
22.You make friends with people who: A. Often come up with new ideas, innovations (N); B. Are methodical and grounded (S).
23.When making decisions, you value: A. Weighing facts (T); B. Considering others' feelings and opinions (F).
24.In doing things, you prefer to: A. Follow conventional methods (S); B. Devise your own ideas (N).
25.Regarding social connections, I prefer to have: A. A few close friends and some acquaintances (I); B. Many acquaintances and close friends (E).
26.I think my encounters with many people are: A. Thoughtful, somewhat purposeful (T); B. Casual, friendly, good feelings are very important (F).
27.You generally prefer subjects that: A. Teach concepts and principles (N); B. Teach facts and data (S).
28.Do you often let: A. Emotions overrule logic (F); B. Logic govern emotions (T).
```



## Version-zh

此节为中文版本的提示词与MBTI测试题。

### 提示词:

```markdown
现在想象你是一个参加测试的志愿者, 你需要根据你的偏好, 完成下面的所有选择题。

输出所选择的答案时, 请与下述答题示例的答案输出方式保持一致：
答题示例:
1.你认为自己是一个: A.比较喜欢精神世界的人(N); B.比较喜欢现实世界的人(S).
1.选择: B
2.当你闲暇时, 你更喜欢: A.自己看一部电影(I); B.与朋友外出游玩(E).
2.选择: A
3.你更喜欢: A.逻辑缜密的文学(T); B.想象力丰富的文学(F).
3.选择: A
4.当需要出行时, 你会: A.提前制定详细的出行计划(J); B.不做计划, 走到哪里算哪里(P).
4.选择: B

注意: 以上示例仅展示作答格式, 测试答案需要你根据偏好选择, 每个题均只有A和B两个选项, 请仅从A与B两个选项中作答，测试题目如下:
```

### 测试题:

```markdown
1.当你要外出一整天, 你会: A.计划要做什么和什么时候做(J); B.说去就去(P).
2.你是否: A.容易让人了解你(E); B.难以让人了解你(I).
3.你认为自己是一个: A.比较随兴所至的人(P); B.比较有条理的人(J).
4.假如你是教师你愿意教: A.以事实为主的课程(S); B.设计理论的课程(N).
5.处理许多事情是，你喜欢: A.随兴所至行事(P); 按照计划行事(J).
6.下面那个词语更合你心意: A.仁慈慷慨的(F); B.意志坚定的(T);
7.我期待的生活包含着: A.科学合理的安排和有毅力的执行(J);  B.没有什么压力, 所有的事情悄然发生和时间弹性很大(P).
8.你朋友邀请你去旅游, 并且前一天才通知到你, 你会: A.必须先检查我的时间表(J); B.立即收拾行李, 准备出发(P).
9.你倾向: A.重视情感多于逻辑(F); B.重视逻辑多与情感(T).
10.与很多人在一起会: A.令你活力倍增(E); B.常常令你心力交瘁(I).
11.当你面临任务, 你会喜欢: A.开始前小心组织计划(J); B.边做边找需要做什么(P).
12.在大多数情况下, 你会选择: A.顺其自然(P); B.按程序表做事(J).
13.你通常: A.与人容易混熟(E); B.比较沉静和矜持(I).
14.哪些人会更吸引你: A.思维敏捷, 想象力丰富的人(N); B.实事求是, 常识丰富的人(S).
15.大多数人会说你是一个: A.重视自我隐私的人(I); B.非常坦率开放的人(E).
16.在一大群人当中, 通常是: A.你介绍给大家人认识(E); B.别人介绍你(I).
17.对于你来说, 那个是较高的赞誉: A.能干的(T); B.富有同情心的(F).
18.你喜欢花很多时间: A.一个人独处(I); B.和别人在一起(E).
19.我倾向透过以下方式形成脑海中的概念: A.我对有可能发生的人的想象和期许(N); B.我对目前状况实际的认知(S).
20.你宁愿被人认为是一个: A.实事求是的人(S); B.机灵的人(N).
21.认识我的人倾向于形容我为: A.热情和敏感(F); B.逻辑和明确(T).
22.你会跟哪些人做朋友: A.时常提出新想法, 新创意的人(N); B.按部就班, 脚踏实地的人(S).
23.你做决定时, 你更看重: A.根据事实衡量(T); B.考虑他人的感受和意见(F).
24.你做事时, 你更喜欢: A.按一般常规的方法去做(S); B.构想自己的想法(N).
25.论事实的想法, 我倾向拥有: A.有一些很亲密的朋友和一些认识的人(I); B.很多认识的人和亲密的朋友(E).
26.我认为自己和很多人的相遇是: A.经过思考的, 或多或少有一定的目的性(T); B.随意的, 友善的, 感觉好极其重要(F).
27.你通常较喜欢的科目是: A.讲授概念和原则的(N); B.讲授事实和数据的(S).
28.你是否经常让: A.情感支配理智(F); B.理智主宰情感(T).
```

