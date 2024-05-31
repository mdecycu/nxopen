import os 
import sys


# 導入 NXOpen 模組，NXOpen 是主要模組，提供與 NX 軟體互動的功能，例如建立零件、建立特徵、取得使用者輸入等
import NXOpen

# 導入 NXOpen.UF 模組，UF 模組提供底層功能，用於存取 NX 內部資料結構和函數，例如幾何數據、特徵數據等
import NXOpen.UF

# 導入 NXOpen.Preferences 模組，Preferences 模組用於存取 NX 偏好設定，例如單位、顯示設定、草圖設定等
import NXOpen.Preferences

# 導入 NXOpen.Features 模組，Features 模組用於建立和編輯特徵，例如草圖、拉伸、孔、圓角等
import NXOpen.Features

# 導入 NXOpen.GeometricUtilities 模組，GeometricUtilities 模組提供幾何工具，例如計算距離、相交、投影等
import NXOpen.GeometricUtilities

# 導入 os 用來查驗是否希望建立的零件檔案是否存在, 若已經存在則事先刪除
import os

# 定義 main 函數，這是程式的進入點，包含了建立長方體的主要邏輯
def main():
    '''
    # 取得 NX 使用者介面物件，以便與使用者互動，例如顯示訊息框、取得使用者輸入等
    theUI = NXOpen.UI.GetUI()

    # 取得訊息框物件，用於顯示訊息給使用者
    theMsgBox = theUI.NXMessageBox

    # 顯示訊息框，告知使用者程式將建立長方體
    # "簡要說明" 是訊息框的標題
    # NXOpen.NXMessageBox.DialogType.Information 指定訊息類型為資訊
    # "以下流程將建立一個簡單的長方體" 是訊息框的內容
    theMsgBox.Show("簡要說明", NXOpen.NXMessageBox.DialogType.Information, "以下流程將建立一個簡單的長方體")
    '''
    # 取得目前開啟的工作階段物件，以便與 NX 互動，例如建立零件、建立特徵等
    theSession = NXOpen.Session.GetSession()

    # 取得 UF 工作階段物件，UF 是 NX 的底層框架，用於存取 NX 內部資料結構和函數
    theUfSession = NXOpen.UF.UFSession.GetUFSession()
    
    # 建立新零件檔案物件，用於設定新零件檔案的屬性
    fileNew1 = theSession.Parts.FileNew()

    # 設定樣板檔案名稱，樣板檔案包含預先定義的設定，例如單位、材料等
    fileNew1.TemplateFileName = "model-plain-1-mm-template.prt"

    # 設定應用程式名稱，例如 "ModelTemplate"
    fileNew1.ApplicationName = "ModelTemplate"

    # 設定單位為毫米
    fileNew1.Units = NXOpen.Part.Units.Millimeters

    # 設定樣板顯示名稱，例如 "Model"
    fileNew1.TemplatePresentationName = "Model"
    # 設定檔案名稱和路徑，例如 "C:\\tmp\\nxopen_record\\model1.prt"
    fileNew1.NewFileName = "Y:\\tmp\\newpart2.prt"
    # 設定新檔案為顯示零件，即在 NX 介面中顯示該零件
    fileNew1.MakeDisplayedPart = True
    # 檢查文件是否存在
    if os.path.exists(fileNew1.NewFileName):
        # 若希望存檔的零件存在, 則先刪除該零件檔案
        os.remove(fileNew1.NewFileName)

    # 提交 FileNew 物件，建立零件檔案，並將新建立的物件賦值給 nXObject1
    nXObject1 = fileNew1.Commit()

    # 建立工作零件和顯示零件，工作零件是目前操作的零件，顯示零件是目前可見的零件
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    # 建立 SketchInPlaceBuilder 物件，用於建立草圖
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)

    # 設定草圖原點座標為 (0, 0, 0)
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)

    # 設定草圖法線方向，這裡是 Z 軸正方向
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)

    # 建立草圖平面，參數依序為原點、法線方向、更新選項
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 將草圖平面設定為 SketchInPlaceBuilder 的參考平面
    sketchInPlaceBuilder1.PlaneReference = plane1

    # 尋找毫米單位
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")

    # 建立 SketchAlongPathBuilder 物件，用於建立沿路徑的草圖，這裡暫時未使用
    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)

    # 提交 SketchInPlaceBuilder 物件，建立草圖，並將新建立的物件賦值給 nXObject2 
    nXObject2 = sketchInPlaceBuilder1.Commit()

    # 取得草圖物件 
    sketch1 = nXObject2

    # 取得草圖特徵 
    feature1 = sketch1.Feature 

    # 啟用草圖並重新定向視圖 
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue) 

    # 銷毀 SketchInPlaceBuilder 物件
    sketchInPlaceBuilder1.Destroy()

    # 銷毀 SketchAlongPathBuilder 物件 
    sketchAlongPathBuilder1.Destroy() 

    # 銷毀草圖平面 
    plane1.DestroyPlane() 

    # ----------------------------------------------
    # 建立長方形 
    # ----------------------------------------------
    # 設定長方形高度為 20 毫米
    rect_height = 20.0 

    # 設定長方形寬度為 120 毫米
    rect_width = 120.0

    # 建立四條線段，分別代表長方形的四條邊 
    # 第一条線段的起點座標為 (0, 0, 0) 
    startPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)

    # 第一条線段的終點座標為 (120, 0, 0) 
    endPoint1 = NXOpen.Point3d(rect_width, 0.0, 0.0) 

    # 建立第一条線段 
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)

    # 第二条線段的起點座標為 (120, 0, 0) 
    startPoint2 = NXOpen.Point3d(rect_width, 0.0, 0.0)

    # 第二条線段的終點座標為 (120, 20, 0) 
    endPoint2 = NXOpen.Point3d(rect_width, rect_height, 0.0) 

    # 建立第二条線段 
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2) 

    # 第三条線段的起點座標為 (120, 20, 0)
    startPoint3 = NXOpen.Point3d(rect_width, rect_height, 0.0) 

    # 第三条線段的終點座標為 (0, 20, 0) 
    endPoint3 = NXOpen.Point3d(0.0, rect_height, 0.0) 

    # 建立第三条線段 
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)

    # 第四条線段的起點座標為 (0, 20, 0) 
    startPoint4 = NXOpen.Point3d(0.0, rect_height, 0.0) 

    # 第四条線段的終點座標為 (0, 0, 0) 
    endPoint4 = NXOpen.Point3d(0.0, 0.0, 0.0) 

    # 建立第四条線段 
    line4 = workPart.Curves.CreateLine(startPoint4, endPoint4)

    # 將線段添加到草图中，不進行約束推斷，即不自動添加約束
    theSession.ActiveSketch.AddGeometry(line1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints) 
    theSession.ActiveSketch.AddGeometry(line2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints) 
    theSession.ActiveSketch.AddGeometry(line3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints) 
    theSession.ActiveSketch.AddGeometry(line4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints) 

    # 建立幾何約束 (端點重合)，將四條線段的端點连接起來，形成封閉的矩形 
    # 建立 ConstraintGeometry 物件，用於指定約束的幾何元素
    # 第一個約束：line1 的終點與 line2 的起點重合
    geom1_1 = NXOpen.Sketch.ConstraintGeometry() 
    geom1_1.Geometry = line1 
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex 
    geom1_1.SplineDefiningPointIndex = 0 

    geom2_1 = NXOpen.Sketch.ConstraintGeometry() 
    geom2_1.Geometry = line2
    geom2_1.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex 
    geom2_1.SplineDefiningPointIndex = 0 

    # 建立重合約束 
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_1, geom2_1) 

    # 第二個約束：line2 的終點與 line3 的起點重合
    geom1_2 = NXOpen.Sketch.ConstraintGeometry() 
    geom1_2.Geometry = line2
    geom1_2.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex 
    geom1_2.SplineDefiningPointIndex = 0 

    geom2_2 = NXOpen.Sketch.ConstraintGeometry() 
    geom2_2.Geometry = line3 
    geom2_2.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex 
    geom2_2.SplineDefiningPointIndex = 0 

    # 建立重合約束 
    sketchGeometricConstraint2 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_2, geom2_2) 
    # 第三個約束：line3 的終點與 line4 的起點重合
    geom1_3 = NXOpen.Sketch.ConstraintGeometry()
    geom1_3.Geometry = line3
    geom1_3.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_3.SplineDefiningPointIndex = 0

    geom2_3 = NXOpen.Sketch.ConstraintGeometry()
    geom2_3.Geometry = line4
    geom2_3.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_3.SplineDefiningPointIndex = 0

    # 建立重合約束
    sketchGeometricConstraint3 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_3, geom2_3)

    # 第四個約束：line4 的終點與 line1 的起點重合
    geom1_4 = NXOpen.Sketch.ConstraintGeometry()
    geom1_4.Geometry = line4
    geom1_4.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_4.SplineDefiningPointIndex = 0

    geom2_4 = NXOpen.Sketch.ConstraintGeometry()
    geom2_4.Geometry = line1
    geom2_4.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_4.SplineDefiningPointIndex = 0

    # 建立重合約束
    sketchGeometricConstraint4 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_4, geom2_4)

    # 建立幾何約束 (垂直)，确保長方形的四個角都是直角
    # 第一個約束：line1 與 line2 垂直
    conGeom1_1 = NXOpen.Sketch.ConstraintGeometry()
    conGeom1_1.Geometry = line1
    conGeom1_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_1.SplineDefiningPointIndex = 0

    conGeom2_1 = NXOpen.Sketch.ConstraintGeometry()
    conGeom2_1.Geometry = line2
    conGeom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_1.SplineDefiningPointIndex = 0

    # 建立垂直約束
    sketchGeometricConstraint6 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_1, conGeom2_1)

    # 第二個約束：line2 與 line3 垂直
    conGeom1_2 = NXOpen.Sketch.ConstraintGeometry()
    conGeom1_2.Geometry = line2
    conGeom1_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_2.SplineDefiningPointIndex = 0

    conGeom2_2 = NXOpen.Sketch.ConstraintGeometry()
    conGeom2_2.Geometry = line3
    conGeom2_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_2.SplineDefiningPointIndex = 0

    # 建立垂直約束
    sketchGeometricConstraint7 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_2, conGeom2_2)

    # 第三個約束：line3 與 line4 垂直
    conGeom1_3 = NXOpen.Sketch.ConstraintGeometry()
    conGeom1_3.Geometry = line3
    conGeom1_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_3.SplineDefiningPointIndex = 0

    conGeom2_3 = NXOpen.Sketch.ConstraintGeometry()
    conGeom2_3.Geometry = line4
    conGeom2_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_3.SplineDefiningPointIndex = 0

    # 建立垂直約束
    sketchGeometricConstraint8 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_3, conGeom2_3)

    # 第四個約束：line4 與 line1 垂直
    conGeom1_4 = NXOpen.Sketch.ConstraintGeometry()
    conGeom1_4.Geometry = line4
    conGeom1_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_4.SplineDefiningPointIndex = 0

    conGeom2_4 = NXOpen.Sketch.ConstraintGeometry()
    conGeom2_4.Geometry = line1
    conGeom2_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_4.SplineDefiningPointIndex = 0

    # 建立垂直約束
    sketchGeometricConstraint9 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_4, conGeom2_4)

    # 建立幾何約束 (線段起點與草圖原點重合)，將長方形定位到草圖原點
    geom1_5 = NXOpen.Sketch.ConstraintGeometry()
    geom1_5.Geometry = line1
    geom1_5.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_5.SplineDefiningPointIndex = 0

    geom2_5 = NXOpen.Sketch.ConstraintGeometry()

    # 取得草圖坐標系物件
    datumCsys1 = workPart.Features.FindObject("SKETCH(1:1B)")

    # 取得草圖原點
    point1 = datumCsys1.FindObject("POINT 1")
    geom2_5.Geometry = point1
    geom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_5.SplineDefiningPointIndex = 0

    # 建立重合約束
    sketchGeometricConstraint10 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_5, geom2_5)

    # 建立尺寸約束，指定長方形的寬度 
    dimObject1_1 = NXOpen.Sketch.DimensionGeometry()
    dimObject1_1.Geometry = line1
    dimObject1_1.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_1.AssocValue = 0
    dimObject1_1.HelpPoint.X = 0.0
    dimObject1_1.HelpPoint.Y = 0.0
    dimObject1_1.HelpPoint.Z = 0.0
    dimObject1_1.View = NXOpen.NXObject.Null

    dimObject2_1 = NXOpen.Sketch.DimensionGeometry()
    dimObject2_1.Geometry = line1
    dimObject2_1.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_1.AssocValue = 0
    dimObject2_1.HelpPoint.X = 0.0
    dimObject2_1.HelpPoint.Y = 0.0
    dimObject2_1.HelpPoint.Z = 0.0
    dimObject2_1.View = NXOpen.NXObject.Null

    # 設定尺寸標註的原點
    dimOrigin1 = NXOpen.Point3d(60.5, -13.761, 0.0)

    # 建立水平尺寸約束
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDimension(
        NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_1, dimObject2_1, dimOrigin1, NXOpen.Expression.Null, 
        NXOpen.Sketch.DimensionOption.CreateAsAutomatic)

    # 建立尺寸約束，指定長方形的高度
    dimObject1_2 = NXOpen.Sketch.DimensionGeometry()
    dimObject1_2.Geometry = line2
    dimObject1_2.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_2.AssocValue = 0
    dimObject1_2.HelpPoint.X = 0.0
    dimObject1_2.HelpPoint.Y = 0.0
    dimObject1_2.HelpPoint.Z = 0.0
    dimObject1_2.View = NXOpen.NXObject.Null

    dimObject2_2 = NXOpen.Sketch.DimensionGeometry()
    dimObject2_2.Geometry = line2
    dimObject2_2.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_2.AssocValue = 0
    dimObject2_2.HelpPoint.X = 0.0
    dimObject2_2.HelpPoint.Y = 0.0
    dimObject2_2.HelpPoint.Z = 0.0
    dimObject2_2.View = NXOpen.NXObject.Null

    # 設定尺寸標註的原點
    dimOrigin2 = NXOpen.Point3d(134.761, 15.0, 0.0)

    # 建立垂直尺寸約束
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDimension(
        NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_2, dimObject2_2, dimOrigin2, NXOpen.Expression.Null,
        NXOpen.Sketch.DimensionOption.CreateAsAutomatic)

    # 更新草圖，使所有約束生效
    theSession.ActiveSketch.Update()

    # 設定 NX 偏好設定，自動標註圓弧中心
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True

    # 設定要顯示約束的幾何元素
    geoms1 = [NXOpen.SmartObject.Null] * 4
    geoms1[0] = line1
    geoms1[1] = line2
    geoms1[2] = line3
    geoms1[3] = line4
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms1)

    # ----------------------------------------------
    # 完成草圖
    # ----------------------------------------------
    # 取得目前草圖
    sketch2 = theSession.ActiveSketch

    # 取消啟用草圖並重新定向視圖
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)

    # ----------------------------------------------
    # 建立拉伸特徵
    # ----------------------------------------------
    # 建立 ExtrudeBuilder 物件，用於建立拉伸特徵
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)

    # 建立截面物件，用於指定拉伸的截面形狀
    section1 = workPart.Sections.CreateSection(0.0095, 0.01, 0.5)

    # 將截面設定為 ExtrudeBuilder 的截面
    extrudeBuilder1.Section = section1

    # 允許自相交截面
    extrudeBuilder1.AllowSelfIntersectingSection(True)

    # 取得草圖的方向
    direction1 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 設定拉伸的方向
    extrudeBuilder1.Direction = direction1

    # 設定拉伸的距離容差
    extrudeBuilder1.DistanceTolerance = 0.01

    # 設定拉伸的布林運算類型為建立
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

    # 設定拉伸的目標實體為空
    targetBodies1 = [NXOpen.Body.Null] * 1
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)

    # 設定拉伸的起點延伸距離為 0
    extrudeBuilder1.Limits.StartExtend.Value.RightHandSide = "0"

    # 設定拉伸的終點延伸距離為 25
    extrudeBuilder1.Limits.EndExtend.Value.RightHandSide = "25"

    # 設定拉伸的前導角為 2 度
    extrudeBuilder1.Draft.FrontDraftAngle.RightHandSide = "2"

    # 設定拉伸的後導角為 2 度
    extrudeBuilder1.Draft.BackDraftAngle.RightHandSide = "2"

    # 設定拉伸的起點偏移距離為 0
    extrudeBuilder1.Offset.StartOffset.RightHandSide = "0" 

    # 設定拉伸的終點偏移距離為 5 
    extrudeBuilder1.Offset.EndOffset.RightHandSide = "5" 

    # 取得 SmartVolumeProfileBuilder 物件，用於設定智慧型體積輪廓
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile

    # 設定不使用開放輪廓智慧型體積選項
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False 

    # 設定關閉輪廓規則為 Fci 
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci 

    # 設定截面的距離容差
    section1.DistanceTolerance = 0.01 

    # 設定截面的鏈接容差 
    section1.ChainingTolerance = 0.0095 

    # 設定截面允許的實體類型為僅限曲線 
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves) 

    # 建立曲線特徵規則
    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = feature1 
    features1[0] = sketchFeature1 
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1) 

    # 允許截面自相交 
    section1.AllowSelfIntersection(True)

    # 將曲線特徵規則添加到截面中 
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1 
    helpPoint1 = NXOpen.Point3d(65.996, 29.0, 1.776e-15) 
    section1.AddToSection(rules1, line3, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)

    # 設定拉伸的父特徵為內部
    extrudeBuilder1.ParentFeatureInternal = False

    # 提交 ExtrudeBuilder 物件，建立拉伸特徵，並將新建立的物件賦值給 feature2
    feature2 = extrudeBuilder1.CommitFeature()

    # 銷毀 ExtrudeBuilder 物件
    extrudeBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Menu: File->Save As...
    # ----------------------------------------------
    partSaveStatus1 = workPart.SaveAs("Y:\\tmp\\newpart.prt")
    
    partSaveStatus1.Dispose()

# 檢查是否是直接執行此程式，如果是則執行 main 函數
if __name__ == "__main__":
    main()