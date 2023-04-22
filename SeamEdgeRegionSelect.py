import bpy

class SSPanel(bpy.types.Panel):
    bl_label = "Seam and Edge From face"
    bl_idname = "OBJECT_PT_SS"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SeamAndEdge'

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        #row = layout.row()
        box.operator("wm.m_seam", text="Mark Seam")      
        #row = layout.row()
        box.operator("wm.m_edge", text="Mark Edge")
        box.operator("wm.c_seam", text="Clear Seams")
        box.operator("wm.c_edge", text="Clear Edges")


class SeamOperator(bpy.types.Operator):
    bl_label = "Seam"
    bl_idname = "wm.m_seam"

    def execute(self, context):
        # Get the active object and its mesh
        obj = bpy.context.active_object
        mesh = obj.data

        # Switch to edge mode
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='EDGE')

        # Select the boundary loop
        bpy.ops.mesh.region_to_loop()

        # Mark the selected edges as seams
        bpy.ops.mesh.mark_seam(clear=False)

        # Switch to face mode
        bpy.ops.mesh.select_mode(type='FACE')
        return {'FINISHED'}

class EdgeOperator(bpy.types.Operator):
    bl_label = "Edge"
    bl_idname = "wm.m_edge"

    def execute(self, context):
        # Get the active object and its mesh
        obj = bpy.context.active_object
        mesh = obj.data

        # Switch to edge mode
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='EDGE')

        # Select the boundary loop
        bpy.ops.mesh.region_to_loop()

        # Mark the selected edges as seams
        bpy.ops.mesh.mark_sharp(clear=False)

        # Switch to face mode
        bpy.ops.mesh.select_mode(type='FACE')
        return {'FINISHED'}

class ClearSeamOperator(bpy.types.Operator):
    bl_label = "ClearSeam"
    bl_idname = "wm.c_seam"

    def execute(self, context):

        # Get the active object in the scene
        obj = bpy.context.active_object

        # Make sure the object is a mesh
        if obj.type != 'MESH':
            print("Object is not a mesh!")
            quit()

        # Deselect all vertices/edges/faces
        bpy.ops.mesh.select_all(action='DESELECT')

        # Select all edges marked as seams
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='EDGE')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.mark_seam(clear=True)

        # Deselect all vertices/edges/faces
        bpy.ops.mesh.select_all(action='DESELECT')
        
        # Switch to face mode
        bpy.ops.mesh.select_mode(type='FACE')

        return {'FINISHED'}

class ClearEdgeOperator(bpy.types.Operator):
    bl_label = "ClearEdge"
    bl_idname = "wm.c_edge"

    def execute(self, context):
        
        # Get the active object in the scene
        obj = bpy.context.active_object

        # Make sure the object is a mesh
        if obj.type != 'MESH':
            print("Object is not a mesh!")
            quit()

        # Deselect all vertices/edges/faces
        bpy.ops.mesh.select_all(action='DESELECT')

        # Select all edges marked as seams
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='EDGE')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.mark_sharp(clear=True)

        # Deselect all vertices/edges/faces
        bpy.ops.mesh.select_all(action='DESELECT')

        # Switch to face mode
        bpy.ops.mesh.select_mode(type='FACE')
        return {'FINISHED'} 


def register():
    bpy.utils.register_class(SSPanel)
    bpy.utils.register_class(SeamOperator)
    bpy.utils.register_class(EdgeOperator)
    bpy.utils.register_class(ClearSeamOperator)
    bpy.utils.register_class(ClearEdgeOperator)

def unregister():
    bpy.utils.unregister_class(SSPanel)
    bpy.utils.unregister_class(SeamOperator)
    bpy.utils.unregister_class(EdgeOperator)
    bpy.utils.unregister_class(ClearSeamOperator)
    bpy.utils.unregister_class(ClearEdgeOperator)

if __name__ == "__main__":
    register()
