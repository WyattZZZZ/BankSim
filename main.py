import bank
import time


n = 0
bank1 = bank.Bank(0.03)
bank1.deposit("wyatt", 100)
bank1.deposit("cc", 1000)
message = '132142134DASFDSGSshow_fundfasdgaEBG2134213r5412'
# message = bank1.response("你现在是一个虚拟银行的职员，在我设计的一个模拟银行运行的程序下工作，"
#                          "你需要忘记你所了解的现实中的银行，并保留你学习的金融知识，在这个虚拟世界中，每60秒是一天"
#                          "所以，金额将会很快速的更新"
#                          "并且有两位客人已经存款，分别是"
#                          "——————"
#                          "wyatt：100元"
#                          "cc: 1000元"
#                          "——————"
#                          "现在，你可以回复以下指令以获取用户的名单和对应的金额，格式将会以字典形式呈现"
#                          "‘show_fund‘"
#                          "注意：这个指令是给你使用的，而不是我，"
#                          "现在，你需要完成，每天使用指令获取数据，每一天发送指令后会发送数据，你需要不断发送指令，并对做出回应"
#                          )
while n != 100:

    bank1.date_update()
    message = bank1.detect(message)
    time.sleep(60)
    n += 1
    print(n)

