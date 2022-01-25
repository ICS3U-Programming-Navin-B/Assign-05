# Python
def cube_area(side): 
    
    
    return 6 * side**2 

def cube_volume(side):
    return side**3
 
def get_float(prompt): 
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number!")

def main(): 
    side = get_float("Please enter a side cube number !: ")
    print(
        "For a cube with side length {side:0.2f},\n"
        "The volume of the cube is {volume:0.2f}." 
        .format(
            side   = side,
            area   = cube_area(side),
            volume = cube_volume(side)
        )
    )

if __name__ == "__main__":
    main()