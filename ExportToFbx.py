bl_info = {
    "name": "Blender Batch Export",
    "author": "Zorn",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "Select",
    "description": "Exports Selected assets from 0.0.0 to individual .fbx files",
    "category": "Select",
}

import bpy
import os

##-------------------------------------------------------------------
# Get the path of the current Blender file

def Export_Files():

    global path
    path = bpy.data.filepath
    print("Current Path:", path)

    # Get the directory of the current Blender file
    global dir
    dir = os.path.dirname(path)

    # Print the directory of the current Blender file
    print("Directory:", dir)

    # Get the list of selected objects
    selected_objects = bpy.context.selected_objects

    # Loop through the selected objects and export each one
    for obj in selected_objects:
        
        # Deselect all objects and select the current object
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        
        # Set the active object to the current selected object
        bpy.context.view_layer.objects.active = obj
        
        start_loc = obj.location.copy()

        # Move the object to the origin
        obj.location = (0, 0, 0)
        
        # Set the output filename
        output_filename = os.path.join(dir, obj.name + ".fbx")
        
        # Export the selected object as an FBX file
        bpy.ops.export_scene.fbx(filepath=output_filename, use_selection=True)
        
        ##-------------------------------------------------------------------
        # Wait for one second
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        # Move the object back to its original location
        obj.location = start_loc

def show_popup_message(message):
    def draw(self, context):
        self.layout.label(text=message)

    bpy.context.window_manager.popup_menu(draw, title="Message", icon='INFO')



class OBJECT_OT_Export_geometry(bpy.types.Operator):
   
    bl_idname = "object.export_to_fbx"
    bl_label = "Export Selected .FBX"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        if bpy.data.is_saved:
            print("The file has been saved.")
            Export_Files()
            show_popup_message("Assets Exported")
        else:
            print("The file has not been saved.")
            show_popup_message("The file has not been saved.")

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_Export_geometry.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_Export_geometry)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_Export_geometry)
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_func)

if __name__ == "__main__":
    register()