# -*- coding: utf-8 -*-
"""Hand-written question bank for 學而時習.
Every sentence contains a cue that decides the answer.
Fields: (sentence with ＿, answer, also-acceptable, cue_zh, cue_en, English gloss)
"""

L1 = [  # 初級（CEFR A1–A2）：常用詞，線索直接寫在句子裡（以前、現在、已經、二十年）
 # 原
 ('新校長來了以後，＿校長去別的學校工作。','原',['前'],'有新的人來，原來的人換了工作。正式的說法用「原」。','A new person came, so the one who was there before moved on. 原 is the formal choice.','After the new principal came, the former principal went to work at another school.'),
 ('他換到別的部門了，＿部門的同事還常找他吃飯。','原',['前'],'「原部門」＝他原來的部門，那個部門還在。','原部門 = the department he was in before; it still exists.','He moved to another department, but colleagues from his original department still often ask him to dinner.'),
 ('新經理還沒來，現在還是＿經理在做。','原',[],'原來的經理現在還在做，所以不能用「前」。','The original manager is still doing the job, so 前 (no longer there) is wrong.','The new manager has not come yet, so the original manager is still doing the job.'),
 ('兩家公司變成一家以後，＿員工都還在。','原',['舊'],'變成一家「以前」就在的員工，現在還在。','Staff who were there before the two companies became one, still there now.','After the two companies became one, the original staff are all still there.'),
 ('他去新公司工作了一年，又回到＿公司。','原',['舊','前'],'回到「原來」的公司。','Back to the company he was at originally.','He worked at a new company for a year and then went back to his original company.'),
 ('新老闆來了，可是＿員工都沒有換。','原',['舊'],'員工是原來就在的，而且還在，所以不能用「前」。','The staff were already there and still are, so not 前.','A new boss came, but none of the original staff changed.'),
 ('新主任下個月才來，這個月還是＿主任上班。','原',[],'原來的主任現在還在上班。','The original director is still at work this month.','The new director only comes next month; this month the original director is still at work.'),
 ('新聞說，這個學校的＿校長已經不做了。','原',['前'],'新聞的正式說法常用「原」。','News reports often use the formal 原.','The news says this school’s former principal has stopped working there.'),
 # 前
 ('他是我們公司的＿員工，三年前就離開了。','前',[],'「三年前就離開了」：現在已經不是員工。','"Left three years ago": no longer an employee.','He is a former employee of our company; he left three years ago.'),
 ('＿總統今天也來了。','前',[],'已經不做總統的人，一定說「前總統」。','Someone who is no longer president is always 前總統.','The former president came today too.'),
 ('這是我＿老闆，他已經去別的公司了。','前',['舊'],'他已經不是我的老闆了。','He is no longer my boss.','This is my former boss; he has gone to another company.'),
 ('他三年前就不是經理了，大家還叫他＿經理。','前',['原'],'「已經不是」：用「前」。','"No longer": use 前.','He stopped being manager three years ago, but everyone still calls him the former manager.'),
 ('我已經不在那家公司工作了，那是我的＿公司。','前',['舊'],'已經離開的公司。','A company I have already left.','I no longer work at that company; it is my former company.'),
 ('離開公司以後，她跟＿老闆不說話了。','前',[],'已經不是老闆，而且關係不好，所以不用帶感情的「舊」。','No longer her boss, and on bad terms, so not the warm 舊.','After leaving the company, she stopped speaking to her former boss.'),
 ('他是我們學校的＿校長，去年已經不做了。','前',['原'],'「去年已經不做了」：現在不是校長。','"Stopped last year": no longer principal.','He is our school’s former principal; he stopped last year.'),
 ('我們已經不一起工作了，現在他是我的＿同事。','前',['舊'],'「已經不一起工作」：同事關係結束了。','"No longer work together": the tie has ended.','We no longer work together; now he is my former colleague.'),
 # 舊
 ('他換了新工作，週末還常跟＿同事吃飯。','舊',['前'],'以前的同事，可是感情還在。','Colleagues from before, still friends.','He has a new job, but on weekends he still often eats with his old colleagues.'),
 ('他又回到＿老闆的公司工作了。','舊',['前'],'回去找以前的老闆，有感情。','Going back to a boss from before: a warm tie.','He went back to work at his old boss’s company.'),
 ('在路上看到＿同事，兩個人一起說以前的事。','舊',['前'],'「說以前的事」：想起過去。','"Talked about the old days": remembering the past.','He saw an old colleague on the street, and they talked about the old days.'),
 ('這是十年前的照片，裡面都是我的＿同事。','舊',['前'],'十年前的照片：看以前的人，有想念的感覺。','A photo from ten years ago: looking back with fondness.','This is a photo from ten years ago; everyone in it is an old colleague of mine.'),
 ('已經離開公司的＿員工，今天回來看我們。','舊',['前'],'人已經離開，可是還有感情，回來看大家。','They left but still care, so they came back to visit.','Former employees who had left the company came back to see us today.'),
 ('她打電話給以前的＿老闆，請他幫忙。','舊',['前'],'以前的老闆，關係還好，可以請他幫忙。','A boss from before, close enough to ask for help.','She called her old boss and asked him for help.'),
 ('我很想念＿公司的同事和朋友。','舊',['前'],'「想念」：看向過去，有感情。','"Miss": looking back with feeling.','I really miss the colleagues and friends at my old company.'),
 ('過年的時候，他去看以前的＿主管。','舊',['前'],'以前的主管，現在還去看他：有感情。','A manager from before whom he still visits: a warm tie.','At New Year, he went to visit his old manager.'),
 # 老
 ('我們一起工作二十年了，是＿同事。','老',[],'一起工作很久，現在還在一起。','Working together for a long time, and still together.','We have worked together for twenty years; we are long-time colleagues.'),
 ('他從公司開門就在這裡工作，是＿員工。','老',[],'從一開始做到現在：很久，而且還在。','From the very start until now: long and still here.','He has worked here since the company opened; he is a long-time employee.'),
 ('他每天都來這家店，來了十年，是＿客人。','老',[],'來了十年，現在還天天來。','Ten years and still coming every day.','He comes to this shop every day and has for ten years; he is a regular customer.'),
 ('王先生買我們的東西二十年了，是＿客戶。','老',[],'二十年，而且現在還在買。','Twenty years, and still buying.','Mr. Wang has bought from us for twenty years; he is a long-standing customer.'),
 ('李先生教我做事很多年了，到現在還是我的＿師傅。','老',[],'「到現在還是」：很久而且還在。','"Still, until now": long and ongoing.','Mr. Lee has taught me the trade for many years and is still my old master.'),
 ('她在醫院工作四十年了，是醫院的＿醫生。','老',[],'四十年、現在還在工作：資深。','Forty years and still working: senior.','She has worked at the hospital for forty years; she is a veteran doctor there.'),
 ('我們十年前就是同事，現在也還是，是＿同事。','老',[],'以前是，現在還是：很久而且還在。','Then and still now: long and ongoing.','We were colleagues ten years ago and still are; we are old colleagues.'),
 ('他和我一起上班十五年，現在還一起，是我的＿夥伴。','老',[],'十五年，而且現在還一起：用「老」。','Fifteen years and still together: 老.','He and I have gone to work together for fifteen years and still do; he is my long-time partner.'),
]

L2 = [  # 中級（CEFR B1–B2）：線索要從情境推論
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

L3 = [  # 高級（CEFR C1–C2）：語域、評價與陷阱
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
