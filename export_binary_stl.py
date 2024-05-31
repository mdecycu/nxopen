# NX 1872
# Journal created by Admin on Fri May 31 13:48:17 2024 台北標準時間

#
import math
import NXOpen
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
    objects1 = [NXOpen.NXObject.Null] * 1 
    body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
    objects1[0] = body1
    added1 = sTLCreator1.ExportSelectionBlock.Add(objects1)
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "STL Export")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "STL Export")
    
    sTLCreator1.OutputFile = "Y:\\base.stl"
    
    nXObject1 = sTLCreator1.Commit()
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(markId1, "STL Export")
    
    sTLCreator1.Destroy()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()