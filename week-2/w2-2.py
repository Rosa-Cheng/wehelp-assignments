def avg(data):
    sum = 0
    ttl = data["count"]
    staff = data["employees"]
    for money in staff :
        sum += money["salary"]
    result = sum/ttl
    print(result)
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