# -*- coding: utf-8 -*-
"""Hand-written question bank for 學而時習.
Every sentence contains a cue that decides the answer.
Fields: (sentence with ＿, answer, also-acceptable, cue_zh, cue_en, English gloss)
"""

L1 = [  # 初級：線索直接寫在句子裡（時間詞、離職、多年、至今）
 # 原
 ('新部長上任後，＿部長回到大學教書。','原',['前'],'有新人上任，原本擔任的人換了位置。正式的人事異動用「原」。','A new minister took office, so the one who held the post before has moved on. Formal reassignments use 原.','After the new minister took office, the former minister went back to teaching at a university.'),
 ('公司改組以後，＿總經理轉任顧問。','原',['前'],'「改組」是職位異動，原本的總經理換了角色。','"Restructuring" is a change of posts; the original general manager took a new role.','After the restructuring, the former general manager became an adviser.'),
 ('他調到總公司了，＿職位由林小姐接任。','原',[],'指他「原本」的那個職位，現在換人做。「前職位」不自然。','His original post, now taken by someone else. 前職位 sounds unnatural.','He has been transferred to headquarters; Ms. Lin has taken over his original post.'),
 ('合併以後，兩家公司的＿員工都被留了下來。','原',['舊'],'合併「之前」本來就在公司的員工。','The staff who were already there before the merger.','After the merger, the original staff of both companies were all kept on.'),
 ('他從業務部調到行銷部，可是＿部門的同事還常找他幫忙。','原',['前'],'「原部門」＝調職前原本所屬的部門，部門本身還在。','原部門 = the department he belonged to before the transfer; it still exists.','He moved from sales to marketing, but colleagues in his original department still often ask for his help.'),
 ('新校長八月才到任，在那之前由＿校長繼續主持校務。','原',[],'原本的校長還在做，所以不能用「前」（已經不在職）。','The existing principal is still in charge, so 前 (no longer in office) is wrong.','The new principal arrives in August; until then the current principal will keep running the school.'),
 ('這次人事異動以後，他又回到＿單位上班。','原',[],'回到「原本」所屬的單位。','Back to the unit he originally belonged to.','After this round of reassignments, he went back to work in his original unit.'),
 ('報導指出，該校＿校長已在上個月退休。','原',['前'],'新聞報導＋職稱，正式語氣常用「原」。','A news report plus a job title: formal register favours 原.','The report says the school’s former principal retired last month.'),
 # 前
 ('他是我們公司的＿員工，三年前就離職了。','前',[],'「三年前就離職」：關係已經結束，最常用「前」。','"Left three years ago": the tie has ended; 前 is the usual choice.','He is a former employee of our company; he left three years ago.'),
 ('＿總統今天出席了開幕典禮。','前',[],'卸任的國家元首固定說「前總統」。','A head of state who has left office is always 前總統.','The former president attended the opening ceremony today.'),
 ('這位是我＿上司，他已經轉到別家公司了。','前',['舊'],'上司已經離開，強調關係結束。','The boss has moved to another company: the tie has ended.','This is my former boss; he has moved to another company.'),
 ('離職以後，她在臉書上封鎖了＿主管。','前',[],'已經不是主管，而且關係疏遠（封鎖），不帶懷念，所以用「前」不用「舊」。','No longer her manager and the relationship is cold (blocked), so not the nostalgic 舊.','After quitting, she blocked her former manager on Facebook.'),
 ('他的＿雇主幫他寫了一封推薦信。','前',['舊'],'推薦信來自已經不再雇用他的人。','The reference comes from someone who no longer employs him.','His former employer wrote him a reference letter.'),
 ('已經卸任的＿董事長很少在公開場合露面。','前',['原'],'「已經卸任」＝職位結束。','"Has stepped down" = the post has ended.','The former chairman, who has stepped down, rarely appears in public.'),
 ('聽說你＿公司倒閉了，現在還好嗎？','前',['舊'],'你已經離開的公司。','A company you have already left.','I heard your former company went bankrupt. Are you okay?'),
 ('兩人已經拆夥，現在只是＿合夥人的關係。','前',[],'「拆夥」＝合作結束。','"Split up" = the partnership has ended.','They have split up; now they are just former partners.'),
 # 舊
 ('換了新工作，他週末還是常跟＿同事吃飯。','舊',['前'],'以前的同事，但感情還在，口語又帶懷念。','Colleagues from before, but the friendship remains: casual and nostalgic.','Even after changing jobs, he still often has dinner with his old colleagues on weekends.'),
 ('將軍退休以後，＿部屬每年都會來拜年。','舊',['老'],'過去帶過的部屬，情誼一直延續。','Subordinates from the past who still visit.','After the general retired, his former subordinates came to pay New Year visits every year.'),
 ('繞了一圈，他最後又回到＿老闆的公司上班。','舊',['前'],'「回去」找以前的老闆，帶懷念。','Going back to a boss from before: a nostalgic tie.','After all that, he went back to work at his old boss’s company.'),
 ('在街上巧遇＿同事，兩人聊起當年一起加班的日子。','舊',['前'],'「聊起當年」：回憶過去的關係。','"Talked about those days": looking back at a past tie.','He ran into an old colleague on the street, and they reminisced about working overtime together back then.'),
 ('同學會上，他碰到好幾位以前一起創業的＿夥伴。','舊',['前'],'「以前一起創業」：過去的夥伴，久別重逢。','"Started a business together back then": partners from the past.','At the reunion he met several old partners he had once started a business with.'),
 ('公司搬家那天，幾個已經離職的＿員工特地回來幫忙。','舊',['前'],'已經離開、但還有感情，特地回來幫忙。','They left, but still care enough to come back and help.','On moving day, a few former employees who had left came back specially to help.'),
 ('她把履歷寄給以前的＿上司，請他幫忙推薦。','舊',['前'],'過去的上司，關係還好到可以拜託。','A boss from before, close enough to ask a favour.','She sent her CV to her old boss and asked him for a recommendation.'),
 ('翻到一張十年前的合照，照片裡都是＿同事。','舊',['前'],'十年前的照片：看向過去，帶懷念。','A photo from ten years ago: looking back with nostalgia.','He came across a group photo from ten years ago, full of old colleagues.'),
 # 老
 ('我們在同一個部門二十年了，是＿同事。','老',[],'共事二十年、現在還在一起：延續。','Twenty years in the same department and still together: continuing.','We have been in the same department for twenty years; we are long-time colleagues.'),
 ('他是公司的＿員工，從開幕做到現在。','老',[],'「從開幕做到現在」＝資深、仍在職。','"From opening day until now" = senior and still here.','He is a long-time employee who has worked here since the company opened.'),
 ('這家店的＿客戶都知道，週二不營業。','老',[],'長期往來、現在仍是客戶。','Long-standing customers who still come.','The shop’s regular customers all know it is closed on Tuesdays.'),
 ('李先生是我們的＿夥伴，合作十幾年了，一直很愉快。','老',[],'合作十幾年、現在仍持續。','Over a decade of partnership, still going.','Mr. Lee is our long-time partner; we have worked together happily for over ten years.'),
 ('王經理是我的＿長官，一路提拔我到今天。','老',[],'「一路……到今天」：關係延續至今，帶敬重。','"All the way to today": the tie continues, with respect.','Manager Wang is my long-time superior; he has supported me all the way to where I am today.'),
 ('幾位持股三十年的＿股東都支持這次的改革。','老',[],'「持股三十年」＝資深、長期。','"Held shares for thirty years" = long-standing.','Several shareholders who have held stock for thirty years support the reform.'),
 ('他和阿明搭檔十年了，是彼此的＿搭檔，一個眼神就懂。','老',[],'默契來自長久合作：延續＋親切。','Their rapport comes from years together: continuing and warm.','He and A-Ming have worked as a pair for ten years; they are old partners who understand each other at a glance.'),
 ('退休那天，一起工作了三十年的＿同事們為他辦了驚喜派對。','老',[],'一起工作三十年，直到今天都還是同事。','Thirty years together and colleagues right up to today.','On the day he retired, the colleagues he had worked with for thirty years threw him a surprise party.'),
]

L2 = [  # 中級：線索要從情境推論
 # 原
 ('新政府上台後，＿行政院長轉任總統府資政。','原',['前'],'政府換人、他轉任新職：正式的職位異動。','A new government and a new post for him: a formal reassignment.','After the new government took office, the former premier became a senior adviser to the president.'),
 ('經過內部調動，＿課長的位置由林先生接任，他自己則升為經理。','原',[],'他沒有離開，只是升官，所以是「原本擔任」課長，不是「前」。','He did not leave, he was promoted, so it is the post he originally held (原), not a former one (前).','After an internal reshuffle, Mr. Lin took over his original section-chief post, and he was promoted to manager.'),
 ('這家公司被併購後，＿老闆仍然留任董事。','原',[],'他還留在公司（留任），所以是「原本的」老闆，不是已經離開的「前」老闆。','He is still with the company, so he is the original owner (原), not a departed former one (前).','After the company was acquired, the original owner stayed on as a director.'),
 ('專案改由新團隊負責，＿團隊成員則回到各自的部門。','原',['前'],'「原本」負責這個專案的團隊。','The team that originally ran the project.','The project was handed to a new team, and the members of the original team went back to their own departments.'),
 ('他升任處長後，＿副處長的職缺到現在還沒補上。','原',[],'他自己「原本」擔任的職位空出來了。','The post he himself originally held is now vacant.','Since he was promoted to division director, his original deputy-director post has still not been filled.'),
 ('改制以後，＿職員一律改聘為約聘人員。','原',[],'「改制前」就在的職員，人還在，只是身分改變。','Staff from before the reform; still there, with a new status.','After the reform, all the original staff were rehired on fixed-term contracts.'),
 ('醫院改為公立後，＿院長獲聘繼續主持院務。','原',[],'同一個人繼續當院長，所以不能用「前」。','The same person carries on as director, so 前 does not fit.','After the hospital became public, the original director was hired to keep running it.'),
 ('記者會上，＿發言人宣布即將卸任，由新人接棒。','原',['前'],'他「原本」是發言人，正在交接；正式語氣。','He is the spokesperson handing over; formal register.','At the press conference, the outgoing spokesperson announced he would step down and hand over to a newcomer.'),
 # 前
 ('面試時，人資打電話給他的＿雇主，確認他過去的表現。','前',['舊'],'已經不再雇用他的公司，語氣中性。','The company that no longer employs him; neutral tone.','During the hiring process, HR called his former employer to check his past performance.'),
 ('這位＿立法委員卸任後，轉往大學任教。','前',['原'],'「卸任後」：身分已結束，最通用的說法是「前」。','"After leaving office": the role has ended; 前 is the general term.','After leaving office, the former legislator went to teach at a university.'),
 ('他是蘋果的＿工程師，去年出來自己創業。','前',[],'「去年出來」＝已經離開，常見的履歷寫法。','"Left last year" = no longer there; a typical CV phrasing.','He is a former Apple engineer who left last year to start his own company.'),
 ('法院傳喚公司兩年前就已離職的＿財務長出庭作證。','前',['原'],'「兩年前就已離職」＝職位結束。','"Left two years ago" = the post has ended.','The court summoned the company’s former CFO, who had left two years earlier, to testify.'),
 ('她跟＿老闆鬧上法院，要求補發加班費。','前',[],'關係結束而且有衝突，不帶懷念，不用「舊」。','The tie has ended in conflict, without nostalgia, so not 舊.','She took her former boss to court over unpaid overtime.'),
 ('這位＿國手退役後，在體育班擔任教練。','前',[],'「退役後」：國手身分已經結束。','"After retiring": no longer on the national team.','After retiring, the former national-team athlete became a coach at a sports school.'),
 ('兩年前被資遣的＿員工控告公司積欠資遣費。','前',[],'已經離開而且對立，用中性的「前」。','Gone and now adversaries: neutral 前.','Former employees laid off two years ago are suing the company for unpaid severance.'),
 ('新主管一上任，就推翻了＿主管訂下的所有規定。','前',['原'],'上一任主管已經離開，新的接手。','The previous manager has gone and a new one has taken over.','As soon as the new manager arrived, she overturned all the rules set by the previous manager.'),
 # 舊
 ('退休多年後，每逢過年，＿部屬總會帶著禮物來探望他。','舊',['老'],'過去帶過的部屬，情誼還在。','People he once led, still loyal.','Years after he retired, his former subordinates still visit him with gifts every New Year.'),
 ('他重回業界，靠著＿同事的人脈很快找到新工作。','舊',['前'],'以前的同事關係還能幫忙，帶情誼。','Ties with colleagues from before still help him: a warm bond.','When he returned to the industry, he quickly found a job through his old colleagues’ connections.'),
 ('到了新公司，他常懷念和＿團隊一起熬夜趕案子的日子。','舊',['前'],'「懷念」：看向過去，充滿感情。','"Misses": looking back with feeling.','At his new company, he often misses the late nights spent rushing projects with his old team.'),
 ('這次創業，他找來幾位＿同事一起打拚，彼此早有默契。','舊',['老'],'以前共事過、默契還在的人。','People he worked with before; the rapport is still there.','For this start-up, he brought in several old colleagues; they already work well together.'),
 ('多年沒聯絡的＿上司突然打電話來，邀他回公司幫忙。','舊',['前'],'過去的上司，多年後重新聯繫。','A boss from the past, getting back in touch after years.','His old boss, whom he had not heard from in years, suddenly called and asked him to come back and help.'),
 ('他在＿東家待了十年，離開時大家都捨不得。','舊',['前'],'「舊東家」是常見說法，指以前工作的公司，帶感情。','舊東家 is a common phrase for a former employer, with affection.','He spent ten years at his old company, and everyone was sad when he left.'),
 ('搬家整理時，他找到一疊＿同事寫給他的離職卡片。','舊',['前'],'離職時同事寫的卡片：回憶過去。','Cards colleagues wrote when he left: memories of the past.','While packing to move, he found a stack of farewell cards from his old colleagues.'),
 ('選舉時，他動員了不少當年帶過的＿部屬幫忙站台。','舊',['老'],'「當年帶過的」：過去的部屬。','"People he led back then": past subordinates.','During the election, he mobilised many of the former subordinates he had once led to campaign for him.'),
 # 老
 ('這位＿師傅在工廠做了三十年，徒弟遍布全台。','老',[],'做了三十年，資深而且還在做。','Thirty years on the job, senior and still working.','This veteran master craftsman has worked in the factory for thirty years and has apprentices all over Taiwan.'),
 ('他對往來多年的＿客戶特別照顧，連過年都親自送禮。','老',[],'「往來多年」：長期而且仍持續。','"Dealt with for years": long and ongoing.','He takes special care of his long-standing clients, even delivering New Year gifts in person.'),
 ('公司三十週年慶，特別表揚服務滿二十年的＿員工。','老',[],'服務滿二十年、仍在職：資深。','Twenty years of service and still employed: senior.','At the company’s 30th anniversary, it honoured long-serving employees with twenty years of service.'),
 ('這家小吃店的＿主顧，每天早上都來報到。','老',[],'「老主顧」：長期、天天來的客人。','老主顧: regulars who come every day.','The snack shop’s regular customers show up every morning.'),
 ('遇到難題時，大家都會去請教部門裡的＿前輩。','老',[],'「老前輩」＝資深、受敬重的人；這裡的「前輩」本身就是名詞，不能再加「前」。','老前輩 = a respected senior; 前輩 is already the noun, so adding 前 makes no sense.','When they hit a hard problem, everyone goes to ask the department’s respected seniors.'),
 ('即使彼此都升了官，他們見面時還是互稱＿同事。','老',[],'關係一直延續，帶親切。','The tie has lasted and is warm.','Even though both have been promoted, they still call each other "old colleague" when they meet.'),
 ('會議上，幾位資歷最深的＿主管對新制度意見很多。','老',[],'「資歷最深」＝資深，而且仍在職。','"Most senior" = long-serving and still in post.','At the meeting, several of the most senior managers had many objections to the new system.'),
 ('這家公司靠著一群十幾年不離不棄的＿員工，撐過了金融海嘯。','老',[],'「十幾年不離不棄」：長期而且仍在。','"Stayed loyal for over a decade": long and still there.','The company survived the financial crisis thanks to a group of employees who had stayed loyal for more than ten years.'),
]

L3 = [  # 高級：語域、評價與陷阱
 # 原
 ('官方公告指出，經濟部＿政務次長即日起調任國發會主任委員。','原',['前'],'公文語氣＋「調任」：正式的職位異動，用「原」。','Official notice plus "transferred": formal reassignment favours 原.','An official notice says the original political deputy minister of economic affairs is transferred, effective today, to head the National Development Council.'),
 ('兩家銀行合併後，＿行員的年資一律合併計算。','原',[],'合併前本來就在的行員，人還在，所以只能用「原」。','Tellers who were there before the merger and are still there: only 原 fits.','After the two banks merged, the original staff’s seniority was carried over in full.'),
 ('他雖然被調離＿職務，薪資仍然照舊支給。','原',[],'「調離原職務」：原本擔任的職務，固定搭配。','調離原職務 is a fixed pattern: the duty he originally held.','Although he was moved out of his original position, his salary stayed the same.'),
 ('董事會改選結果出爐，＿董事長續任，另外增補兩名獨立董事。','原',[],'陷阱題：「續任」表示他還在當董事長，不能用「前」；也沒有說任期很長，不必用「老」。','Trap: "continues in office" means he is still chairman, so not 前; nothing says long tenure, so not 老.','The board election results are in: the incumbent chairman continues in office, and two independent directors have been added.'),
 ('專案經理臨時請辭，由＿副理暫代職務。','原',[],'「原副理」＝原本就在的副理，暫時兼任。','The deputy manager already in post fills in temporarily.','The project manager resigned suddenly, so the existing deputy manager is filling in for now.'),
 ('部門裁撤後，＿員工分別移撥到其他單位。','原',[],'部門裁撤前本來就在的員工，人還在公司。','Staff of the abolished department, still with the company.','After the department was abolished, its original staff were reassigned to other units.'),
 ('據了解，＿總編輯將轉任社長，總編輯一職由副總編輯升任。','原',[],'還沒離開、只是轉任，所以是「原」，不是「前」。','He has not left, only changes post, so 原, not 前.','Reportedly, the current editor-in-chief will become publisher, and the deputy editor will be promoted to editor-in-chief.'),
 ('法院判決公司必須讓她回到＿職位，並補發薪資。','原',[],'回到「原本」的職位，固定說「原職位／原職」。','Back to the post she originally held: 原職位.','The court ruled that the company must reinstate her to her original position and pay her back wages.'),
 # 前
 ('檢方傳喚＿總經理到案說明，他已在去年請辭。','前',['原'],'「去年請辭」：職位已經結束。','"Resigned last year": the post has ended.','Prosecutors summoned the former general manager, who resigned last year, for questioning.'),
 ('這位＿新聞主播轉戰政壇，宣布參選市議員。','前',[],'已經不當主播，最常見的介紹方式是「前」。','No longer an anchor; 前 is the standard way to introduce her.','The former news anchor has moved into politics and announced a run for city council.'),
 ('她受訪時直言，和＿老闆已經沒有任何聯絡。','前',[],'關係完全中斷、沒有情誼，所以不用「舊」。','The tie is completely cut, with no warmth, so not 舊.','In the interview she said bluntly that she no longer has any contact with her former boss.'),
 ('一位＿情報官員出版回憶錄，揭露不少內幕。','前',[],'已經離職才能寫回憶錄，新聞慣用「前」。','Only someone who has left can publish a memoir; news style uses 前.','A former intelligence officer published a memoir revealing many inside stories.'),
 ('他用＿雇主的客戶資料自行開業，被控違反競業條款。','前',[],'已經離開而且產生糾紛，中性偏負面，用「前」。','He has left and there is a dispute: neutral to negative, so 前.','He started his own business using his former employer’s client data and was accused of breaching a non-compete clause.'),
 ('兩人曾是合作無間的夥伴，如今卻成了對簿公堂的＿合夥人。','前',[],'「如今卻……對簿公堂」：合作已經結束，而且翻臉。','"Now facing each other in court": the partnership has ended badly.','The two were once close partners but are now former partners facing each other in court.'),
 ('這名已經離職的＿員工在網路上爆料公司的加班文化，引發熱議。','前',[],'已經離職而且公開批評，沒有懷念的意思。','Has left and is publicly critical: no nostalgia.','The former employee, who has already left, exposed the company’s overtime culture online and sparked debate.'),
 ('一位卸任多年的美國＿國務卿訪台，與總統會面。','前',[],'卸任的官員固定用「前」。','Officials who have left office are referred to with 前.','A former U.S. secretary of state, out of office for years, visited Taiwan and met the president.'),
 # 舊
 ('他當上總經理後，把好幾位＿部屬調到身邊，被批評任人唯親。','舊',['老'],'「舊部屬」：以前帶過、跟他有交情的人。','舊部屬: people he once led and is close to.','After becoming general manager, he brought several of his old subordinates to his side and was criticised for cronyism.'),
 ('這位作家筆下常出現他在報社的＿同事，字裡行間滿是懷念。','舊',['前'],'「滿是懷念」：看向過去、帶感情。','"Full of nostalgia": looking back with feeling.','The writer often writes about his old colleagues at the newspaper, with nostalgia on every line.'),
 ('他婉拒了新公司的高薪挖角，決定回去幫＿老闆的忙。','舊',['前'],'回去幫以前的老闆：有情誼，所以用「舊」。','Going back to help a boss from before: a bond of loyalty.','He turned down a well-paid offer and decided to go back and help his old boss.'),
 ('告別式上，許多＿部屬從各地趕來送他最後一程。','舊',['老'],'過去帶過的部屬，以情誼前來。','People he once led, coming out of loyalty.','At the funeral, many of his former subordinates came from all over to say goodbye.'),
 ('選舉在即，他頻頻拜訪昔日的＿同事和合作對象。','舊',['前'],'「昔日」＝過去，帶人情味。','"Of former days" = from the past, with a personal touch.','With the election near, he kept visiting old colleagues and past collaborators.'),
 ('退出政壇後，他和＿幕僚仍然保持密切往來。','舊',['前'],'過去的幕僚，但關係仍然親近。','Aides from the past who remain close.','After leaving politics, he stayed in close contact with his former aides.'),
 ('這家新公司的骨幹，幾乎都是他在＿東家認識的同事。','舊',['前'],'「舊東家」：以前工作的公司，常見說法。','舊東家: one’s former company, a common phrase.','The core of this new company is almost all people he met at his old company.'),
 ('重回母公司報到那天，看到當年的＿同事都還在，他鬆了一口氣。','舊',['老'],'「當年的」：以重逢的角度看過去的同事。','"From back then": seeing colleagues from the past again.','On the day he returned to the parent company, he was relieved to see his old colleagues were all still there.'),
 # 老
 ('公司裁員時，薪資最高的＿員工首當其衝。','老',[],'資深員工薪水高，最先被裁：「老」在這裡是「資深」。','Senior staff earn the most and are cut first: 老 here means senior.','When the company cut jobs, the long-serving employees with the highest pay were hit first.'),
 ('這位＿主管倚老賣老，常讓新人很難做事。','老',[],'「倚老賣老」：資深而且帶負面評價。','"Pulls rank on seniority": senior, with a negative judgement.','This old-timer manager throws his seniority around and makes life hard for newcomers.'),
 ('他是這家報社的＿記者，跑了二十年的國會新聞。','老',[],'做了二十年、還在做：資深。','Twenty years on the beat and still at it: veteran.','He is a veteran reporter at this paper who has covered parliament for twenty years.'),
 ('雖然兩家公司競爭激烈，兩位交手多年的＿對手私下卻是好朋友。','老',[],'「交手多年」：長期而且仍在競爭。','"Have competed for years": long and still ongoing.','Although the two companies compete fiercely, the two long-time rivals are good friends in private.'),
 ('新官上任，第一件事就是拜訪公司持股多年的＿股東，請他們繼續支持。','老',[],'「持股多年」：長期、仍持有。','"Held shares for years": long and still holding.','The new chief’s first move was to visit the company’s long-standing shareholders and ask for their continued support.'),
 ('這位＿教授在系上教了四十年，至今仍堅持每週上課。','老',[],'「至今仍」：資深而且仍在任。','"Still… to this day": senior and still in post.','This veteran professor has taught in the department for forty years and still insists on teaching every week.'),
 ('她是這家店十幾年的＿顧客了，店員一看到她就知道要點什麼。','老',[],'「十幾年」而且還在光顧。','"For over ten years" and still coming.','She has been a regular customer of this shop for over ten years; the staff know her order on sight.'),
 ('合作了二十年的＿夥伴突然退出，讓計畫陷入停擺。','老',[],'到退出之前一直是合作多年的夥伴：「老」看長度。','A partner of twenty years until the moment he left: 老 is about length.','A partner of twenty years suddenly pulled out, bringing the project to a halt.'),
]
