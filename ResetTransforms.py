bl_info = {
    "name": "Set Origin to Geometry",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "Object > Set Origin",
    "description": "Sets the origin of the selected object to its geometry",
    "category": "Object",
}

import bpy

class OBJECT_OT_set_origin_to_geometry(bpy.types.Operator):
    """Set the origin of the selected object to its geometry"""
    bl_idname = "object.set_origin_to_geometry"
    bl_label = "Set Origin to Geometry"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Get the active object
        obj = context.active_object

        # Set the origin to the center of the object's geometry
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
        # Apply location, rotation, and scale of the object
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_set_origin_to_geometry.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_set_origin_to_geometry)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_set_origin_to_geometry)
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_func)

if __name__ == "__main__":
    register()