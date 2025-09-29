def total_overs(balls):
    ans = "{}.{}".format(balls // 6, balls % 6)
    return float(ans)


print(total_overs(164))
