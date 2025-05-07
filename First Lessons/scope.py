x = "global"

def f():
    x = "local x"

f()
print(x)

#fonksiyon içindeki x değişkeni global x değişkeni ile aynı isimde olsa da farklı bir değişkendir.
