import turtle

def draw_golden_spiral(n):
    a, b = 0, 1
    
    # 設置畫布
    turtle.speed(10)
    turtle.pensize(2)
    
    # 繪製斐波那契正方形和弧線
    for _ in range(n):
        # 繪製正方形
        for _ in range(4):
            turtle.forward(b * 10) # 放大倍數，方便觀看
            turtle.left(90)
        
        # 繪製弧線 (1/4圓)
        turtle.circle(b * 10, 90)
        
        # 更新斐波那契數列
        a, b = b, a + b

# 繪製 10 次的黃金螺旋線
if __name__ == "__main__":
    turtle.setup(800, 600)
    draw_golden_spiral(10)
    turtle.done()
