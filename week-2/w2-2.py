def avg(data):
    print((data["employees"][0]["salary"]+data["employees"][1]["salary"]+data["employees"][2]["salary"])/data["count"])
avg({
    "count":3,
    "employees":[
            {
            "name":"John",
            "salary":30000
            },
            {
                "name":"Bob",
                "salary":60000
            },
            {
                "name":"Jenny",
                "salary":50000
            }
        ]
})# 呼叫 avg 函式