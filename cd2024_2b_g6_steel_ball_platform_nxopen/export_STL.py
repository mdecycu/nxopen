# NX 1872
# Journal created by Admin on Fri May 24 14:42:35 2024 台北標準時間

#
import math
import NXOpen
import NXOpen.Assemblies
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: File->Export->STL...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sTLCreator1 = theSession.DexManager.CreateStlCreator()
    
    sTLCreator1.AutoNormalGen = True
    
    sTLCreator1.ChordalTol = 0.080000000000000002
    
    sTLCreator1.AdjacencyTol = 0.080000000000000002
    
    theSession.SetUndoMarkName(markId1, "STL Export Dialog")
    
    # ----------------------------------------------
    #   Menu: Edit->Selection->Select All
    # ----------------------------------------------
    # Refer to the sample NXOpen application, Selection for "Select All" alternatives.
    objects1 = [NXOpen.NXObject.Null] * 17 
    component1 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT s_link 2")
    body1 = component1.FindObject("PROTO#.Bodies|EXTRUDE(2)")
    objects1[0] = body1
    component2 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT platform 1")
    body2 = component2.FindObject("PROTO#.Bodies|EXTRUDE(6)5")
    objects1[1] = body2
    component3 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT base_w 1")
    body3 = component3.FindObject("PROTO#.Bodies|EXTRUDE(8)")
    objects1[2] = body3
    body4 = component2.FindObject("PROTO#.Bodies|EXTRUDE(2)")
    objects1[3] = body4
    body5 = component3.FindObject("PROTO#.Bodies|EXTRUDE(4)1")
    objects1[4] = body5
    body6 = component3.FindObject("PROTO#.Bodies|EXTRUDE(2)")
    objects1[5] = body6
    body7 = component2.FindObject("PROTO#.Bodies|EXTRUDE(6)4")
    objects1[6] = body7
    body8 = component3.FindObject("PROTO#.Bodies|EXTRUDE(4)")
    objects1[7] = body8
    component4 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT y_link 1")
    body9 = component4.FindObject("PROTO#.Bodies|EXTRUDE(2)")
    objects1[8] = body9
    body10 = component2.FindObject("PROTO#.Bodies|EXTRUDE(6)3")
    objects1[9] = body10
    body11 = component2.FindObject("PROTO#.Bodies|EXTRUDE(6)2")
    objects1[10] = body11
    component5 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT y_link 2")
    body12 = component5.FindObject("PROTO#.Bodies|EXTRUDE(2)")
    objects1[11] = body12
    body13 = component2.FindObject("PROTO#.Bodies|EXTRUDE(6)")
    objects1[12] = body13
    component6 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT s_link 1")
    body14 = component6.FindObject("PROTO#.Bodies|EXTRUDE(2)")
    objects1[13] = body14
    body15 = component3.FindObject("PROTO#.Bodies|EXTRUDE(8)1")
    objects1[14] = body15
    body16 = component3.FindObject("PROTO#.Bodies|EXTRUDE(6)")
    objects1[15] = body16
    body17 = component2.FindObject("PROTO#.Bodies|EXTRUDE(6)1")
    objects1[16] = body17
    added1 = sTLCreator1.ExportSelectionBlock.Add(objects1)
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "STL Export")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "STL Export")
    
    sTLCreator1.OutputFile = "C:\\Users\\Admin\\Desktop\\nx\\assembly1.stl"
    
    nXObject1 = sTLCreator1.Commit()
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(markId1, "STL Export")
    
    sTLCreator1.Destroy()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()