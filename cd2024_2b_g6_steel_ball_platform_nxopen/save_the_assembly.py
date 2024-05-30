# NX 1872
# Journal created by Admin on Fri May 24 14:22:23 2024 台北標準時間

#
import math
import NXOpen
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: File->Save As...
    # ----------------------------------------------
    partSaveStatus1 = workPart.SaveAs("C:\\Users\\Admin\\Desktop\\nx\\platform_assembly.prt")
    
    partSaveStatus1.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()