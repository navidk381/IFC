import ifcopenshell as ios

from pathlib import Path, PureWindowsPath #for neatly handling the paths
#shift + right lick then copy as path. Finally, replace \\ with \.


def filepath(copied_pasted_path):
    # I've explicitly declared my path as being in Windows format, so I can use forward slashes in it.
    filename = PureWindowsPath(copied_pasted_path)

    # Convert path to the right format for the current operating system sdf sdfs 
    correct_path = Path(filename)
    return correct_path

def path_sanity(correct_path):
    if not correct_path.exists():
        print("Oops, {} doesn't exist at {}!".format(correct_path.name,correct_path))
    else:
        print("Yay, {} exists at {}!".format(correct_path.name,correct_path))

def main():
    wall_path = "C:\\Users\\nkayf\\OneDrive\\Documents\\IFC\\2. IFC\\wall.ifc"  #a single wall
    unit_path = "C:\\Users\\nkayf\\OneDrive\\Documents\\IFC\\2. IFC\\sample1.ifc"  #a unit
    correct_Wpath = filepath(wall_path) 
    path_sanity(correct_Wpath)  
    correct_Upath = filepath(unit_path) 
    path_sanity(correct_Upath)

    ifc_file = ios.open(correct_Wpath)
    wall = ifc_file.by_type('IfcWall')[0]
    print(wall.GlobalId)
    
    
if __name__ == "__main__":
   
    main()
