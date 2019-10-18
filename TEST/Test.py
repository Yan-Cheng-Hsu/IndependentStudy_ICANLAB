global G_VARIABLE = None

def change_g_variable():
    return G_VARIABLE + 20

def test_func():
    for i in range(6):
        print(i,change_g_variable())



def main():
    test_func()
    
