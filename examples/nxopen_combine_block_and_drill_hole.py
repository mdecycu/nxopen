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
# 以下兩個模組導入 for 挖孔
import NXOpen.Annotations  # 導入註釋模組，用於建立尺寸、文字、符號等註釋
import math  # 再次導入數學函數庫，可能是重複導入

# 導入 os 用來查驗是否希望建立的零件檔案是否存在, 若已經存在則事先刪除
import os

# 定義 main 函數，這是程式的進入點，包含了建立長方體的主要邏輯
def main():
    # 取得 NX 使用者介面物件，以便與使用者互動，例如顯示訊息框、取得使用者輸入等
    theUI = NXOpen.UI.GetUI()

    # 取得訊息框物件，用於顯示訊息給使用者
    theMsgBox = theUI.NXMessageBox

    # 顯示訊息框，告知使用者程式將建立長方體
    # "簡要說明" 是訊息框的標題
    # NXOpen.NXMessageBox.DialogType.Information 指定訊息類型為資訊
    # "以下流程將建立一個簡單的長方體" 是訊息框的內容
    theMsgBox.Show("簡要說明", NXOpen.NXMessageBox.DialogType.Information, "以下流程將建立一個簡單的長方體")

    # 取得目前開啟的工作階段物件，以便與 NX 互動，例如建立零件、建立特徵等
    theSession = NXOpen.Session.GetSession()

    # 取得 UF 工作階段物件，UF 是 NX 的底層框架，用於存取 NX 內部資料結構和函數
    theUfSession = NXOpen.UF.UFSession.GetUFSession()

    # 若先前已經執行此程式, 則需手動或採下列方式關閉所有已經開啟的零件才可繼續執行程式
    # 下一行關閉所有開啟的零件
    theUfSession.Part.CloseAll()

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
    fileNew1.NewFileName = "C:\\tmp\\nxopen_record\\model1.prt"
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

    # 接續挖孔程式碼

    # ----------------------------------------------
    #   Menu: Insert->Sketch...  # 插入 -> 草圖，建立一個新的草圖
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")  # 設定復原標記，標記名稱為 "Start"，用於記錄操作步驟，以便復原

    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)  # 建立草圖建構器物件，用於設定和建立草圖

    # 設定草圖平面，草圖將建立在這個平面上
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)  # 設定草圖平面的原點座標為 (0, 0, 0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)  # 設定草圖平面的法線向量為 (0, 0, 1)，即 Z 軸正方向
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)  # 建立草圖平面
    sketchInPlaceBuilder1.PlaneReference = plane1  # 設定草圖建構器的參考平面為剛建立的平面

    # 建立單位和表達式，用於設定草圖尺寸和幾何約束
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")  # 找到毫米單位物件
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)  # 建立表達式 "0 mm"，表示數值 0，單位為毫米
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)  # 建立表達式 "0 mm"，表示數值 0，單位為毫米

    # 建立沿路徑草圖建構器，但未被使用
    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)

    # 設定復原標記名稱為 "Create Sketch Dialog"
    theSession.SetUndoMarkName(markId1, "Create Sketch Dialog")

    # 建立一個標量物件，數值為 1.0，無單位，用於指定點的位置
    scalar1 = workPart.Scalars.CreateScalar(1.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 找到名稱為 "EXTRUDE(2)" 的拉伸特徵
    extrude1 = workPart.Features.FindObject("EXTRUDE(2)")

    # 找到拉伸特徵上的一個邊緣
    edge1 = extrude1.FindObject("EDGE * 130 * 140 {(120,20,25)(60,20,25)(0,20,25) EXTRUDE(2)}")

    # 在邊緣上建立一個點，位置由標量物件指定，使用百分比參數化
    point1 = workPart.Points.CreatePoint(edge1, scalar1, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 找到拉伸特徵上的另一個邊緣
    edge2 = extrude1.FindObject("EDGE * 130 * 170 {(120,0,25)(120,10,25)(120,20,25) EXTRUDE(2)}")

    # 建立一個方向物件，表示邊緣的方向
    direction1 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 找到拉伸特徵上的一個面
    face1 = extrude1.FindObject("FACE 130 {(60,10,25) EXTRUDE(2)}")

    # 建立一個座標系變換物件，由平面、X 方向、點定義
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction1, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)

    # 建立一個笛卡爾坐標系
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 設定草圖建構器的坐標系
    sketchInPlaceBuilder1.Csystem = cartesianCoordinateSystem1

    # 建立一個新的平面，與 face1 重合
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane2 = workPart.Planes.CreatePlane(origin2, normal2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    plane2.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)  # 設定平面建立方法為重合 
    geom1 = [NXOpen.NXObject.Null] * 1 
    geom1[0] = face1  # 設定平面重合的幾何物件為 face1
    plane2.SetGeometry(geom1)
    plane2.SetFlip(False)  # 設定平面不翻轉
    plane2.SetExpression(None)  # 不設定表達式
    plane2.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)  # 設定備選平面類型為 One
    plane2.Evaluate()  # 計算平面

    # 建立另一個新的平面，與 plane2 同步
    origin3 = NXOpen.Point3d(0.0, 0.0, 0.0) 
    normal3 = NXOpen.Vector3d(0.0, 0.0, 1.0) 
    plane3 = workPart.Planes.CreatePlane(origin3, normal3, NXOpen.SmartObject.UpdateOption.WithinModeling) 
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1) 
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1) 
    plane3.SynchronizeToPlane(plane2)  # 將 plane3 與 plane2 同步

    # 在邊緣上建立一個點，位置由標量物件指定，使用百分比參數化
    scalar2 = workPart.Scalars.CreateScalar(100.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling) 
    point2 = workPart.Points.CreatePoint(edge1, scalar2, NXOpen.PointCollection.PointOnCurveLocationOption.PercentParameter, NXOpen.Point.Null, NXOpen.SmartObject.UpdateOption.WithinModeling) 

    # 設定 plane3 與 face1 重合 
    plane3.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident) 
    geom2 = [NXOpen.NXObject.Null] * 1 
    geom2[0] = face1  # 設定平面重合的幾何物件為 face1
    plane3.SetGeometry(geom2) 
    plane3.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)  # 設定備選平面類型為 One 
    plane3.Evaluate()  # 計算平面 

    # 設定復原標記 
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch") 
    theSession.DeleteUndoMark(markId2, None)  # 刪除復原標記
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch") 

    # 設定草圖偏好設定 
    theSession.Preferences.Sketch.CreateInferredConstraints = True  # 自動建立推斷約束 
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True  # 連續自動標註尺寸 
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression  # 使用表達式作為尺寸標籤 
    theSession.Preferences.Sketch.TextSizeFixed = True  # 使用固定文字大小 
    theSession.Preferences.Sketch.FixedTextSize = 3.0  # 設定文字大小為 3.0
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True  # 顯示參考尺寸的括號
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False  # 不顯示參考幾何 
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0  # 設定約束符號大小為 3.0 
    theSession.Preferences.Sketch.DisplayObjectColor = False  # 不顯示物件顏色 
    theSession.Preferences.Sketch.DisplayObjectName = True  # 顯示物件名稱 

    # 提交草圖建構器，建立草圖 
    nXObject1 = sketchInPlaceBuilder1.Commit() 
    sketch1 = nXObject1  # 取得草圖物件 
    feature1 = sketch1.Feature  # 取得草圖特徵 

    # 設定復原標記 
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update") 
    nErrs1 = theSession.UpdateManager.DoUpdate(markId4)  # 執行更新操作 

    # 啟用草圖並重新定向視圖 
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue) 

    # 刪除復原標記 
    theSession.DeleteUndoMark(markId3, None) 

    # 設定復原標記名稱 
    theSession.SetUndoMarkName(markId1, "Create Sketch") 

    # 銷毀草圖建構器 
    sketchInPlaceBuilder1.Destroy() 

    # 銷毀沿路徑草圖建構器 
    sketchAlongPathBuilder1.Destroy() 

    # 嘗試刪除表達式 
    try: 
        workPart.Expressions.Delete(expression2) 
    except NXOpen.NXException as ex: 
        ex.AssertErrorCode(1050029) 

    # 刪除點 
    workPart.Points.DeletePoint(point2) 

    # 嘗試刪除表達式 
    try: 
        workPart.Expressions.Delete(expression1) 
    except NXOpen.NXException as ex: 
        ex.AssertErrorCode(1050029) 

    # 刪除平面 
    plane1.DestroyPlane() 

    # 嘗試刪除表達式 
    try: 
        workPart.Expressions.Delete(expression4) 
    except NXOpen.NXException as ex: 
        ex.AssertErrorCode(1050029) 

    # 嘗試刪除表達式 
    try: 
        workPart.Expressions.Delete(expression3) 
    except NXOpen.NXException as ex: 
        ex.AssertErrorCode(1050029) 

    # 刪除平面 
    plane3.DestroyPlane() 

    # ---------------------------------------------- 
    #   Menu: Insert->Sketch Curve->Circle...  # 插入 -> 草圖曲線 -> 圓，在草圖中建立圓弧
    # ----------------------------------------------
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")  # 設定復原標記
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")  # 設定復原標記 
    theSession.SetUndoMarkVisibility(markId6, "Curve", NXOpen.Session.MarkVisibility.Visible)  # 設定復原標記的可見性 

    # 取得目前草圖的方向矩陣 
    nXMatrix1 = theSession.ActiveSketch.Orientation 

    # 設定圓弧的中心點和半徑 
    center1 = NXOpen.Point3d(47.0, 10.0, 25.0) 
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 5.2517510580886286, 0.0, ( 360.0 * math.pi/180.0 ))  # 建立一個 360 度的圓弧，即一個完整的圓

    # 將圓弧添加到草图中，不进行约束推断 
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints) 

    # 建立尺寸約束，標註圓的直徑 
    dimObject1_1 = NXOpen.Sketch.DimensionGeometry() 
    dimObject1_1.Geometry = arc1 
    dimObject1_1.AssocType = NXOpen.Sketch.AssocType.NotSet 
    dimObject1_1.AssocValue = 0 
    dimObject1_1.HelpPoint.X = 0.0 
    dimObject1_1.HelpPoint.Y = 0.0 
    dimObject1_1.HelpPoint.Z = 0.0 
    dimObject1_1.View = NXOpen.NXObject.Null 
    dimOrigin1 = NXOpen.Point3d(43.687730028144621, 10.0, 25.0)  # 設定尺寸標註的原點 
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_1, dimOrigin1, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)  # 建立直徑尺寸约束 

    # 取得尺寸約束的關聯尺寸和關聯表達式 
    dimension1 = sketchDimensionalConstraint1.AssociatedDimension 
    expression5 = sketchDimensionalConstraint1.AssociatedExpression 

    # 更新草圖 
    theSession.ActiveSketch.Update() 

    # ----------------------------------------------
    #   Dialog Begin Circle  # 圓形對話框開始，可能是 NX 介面的操作步驟
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: File->Finish Sketch  # 文件 -> 完成草圖，結束草圖編輯
    # ----------------------------------------------
    sketch2 = theSession.ActiveSketch  # 取得目前的草圖物件，賦值給 sketch2

    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")  # 設定復原標記，標記名稱為 "Deactivate Sketch"

    # 取消啟用草圖並重新定向視圖
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)

    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...  # 插入 -> 設計特徵 -> 拉伸，建立拉伸特徵
    # ----------------------------------------------
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")  # 設定復原標記

    # 建立拉伸建構器物件
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)

    # 建立截面物件，用於指定拉伸的截面形狀
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)

    # 將截面設定為拉伸建構器的截面
    extrudeBuilder1.Section = section1

    # 允許自相交截面
    extrudeBuilder1.AllowSelfIntersectingSection(True)

    # 取得單位物件，用於設定角度單位
    unit2 = extrudeBuilder1.Draft.FrontDraftAngle.Units

    # 建立表達式 "2.00 度"，表示數值 2.00，單位為度
    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)

    # 設定拉伸的距離容差
    extrudeBuilder1.DistanceTolerance = 0.01

    # 設定拉伸的布林運算類型為建立
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

    # 設定拉伸的目標實體為空
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)

    # 設定拉伸的起點延伸距離為 0
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")

    # 設定拉伸的終點延伸距離為 25
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("25")

    # 設定拉伸的起點偏移距離為 0
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")

    # 設定拉伸的終點偏移距離為 5
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")

    # 取得 SmartVolumeProfileBuilder 物件，用於設定智慧型體積輪廓
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile

    # 設定不使用開放輪廓智慧型體積選項
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False

    # 設定關閉輪廓規則為 Fci
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci

    # 設定復原標記名稱
    theSession.SetUndoMarkName(markId8, "Extrude Dialog")

    # 設定拉伸的起點延伸距離為 0
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")

    # 設定拉伸的終點延伸距離為 25
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("25")

    # 設定拉伸的布林運算類型為建立
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

    # 設定拉伸的目標實體為空
    targetBodies2 = [NXOpen.Body.Null] * 1
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies2)

    # 設定拉伸的前導角為 2 度
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")

    # 設定拉伸的後導角為 2 度
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")

    # 設定拉伸的起點偏移距離為 0
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")

    # 設定拉伸的終點偏移距離為 5
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")

    # 設定截面的距離容差
    section1.DistanceTolerance = 0.01

    # 設定截面的鏈接容差
    section1.ChainingTolerance = 0.0094999999999999998

    # 設定截面允許的實體類型為僅限曲線
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)

    # 設定復原標記
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)

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
    helpPoint1 = NXOpen.Point3d(50.845184787956853, 6.4440712063959831, 25.0)
    section1.AddToSection(rules1, arc1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)

    # 刪除復原標記
    theSession.DeleteUndoMark(markId10, None)

    # 取得草圖的方向
    direction2 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 設定拉伸的方向
    extrudeBuilder1.Direction = direction2

    # 設定拉伸的目標實體為 "EXTRUDE(2)" 實體
    targetBodies3 = [NXOpen.Body.Null] * 1
    body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
    targetBodies3[0] = body1
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies3)

    # 設定拉伸的布林運算類型為聯合
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite

    # 設定拉伸的目標實體為 "EXTRUDE(2)" 實體
    targetBodies4 = [NXOpen.Body.Null] * 1
    targetBodies4[0] = body1
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies4)

    # 建立表達式 "0 mm"
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)

    # 刪除復原標記
    theSession.DeleteUndoMark(markId9, None)

    # 設定拉伸的布林運算類型為減去
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract

    # 設定拉伸的目標實體為 "EXTRUDE(2)" 實體
    targetBodies5 = [NXOpen.Body.Null] * 1
    targetBodies5[0] = body1
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies5)

    # 取得拉伸的方向
    direction3 = extrudeBuilder1.Direction

    # 反轉拉伸的方向
    success1 = direction3.ReverseDirection()

    # 設定拉伸的方向
    extrudeBuilder1.Direction = direction3

    # 設定拉伸的終點延伸距離為 44
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("44")

    # 設定復原標記
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")

    # 刪除復原標記
    theSession.DeleteUndoMark(markId11, None)

    # 設定復原標記
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")

    # 設定拉伸的父特徵為內部
    extrudeBuilder1.ParentFeatureInternal = False

    # 提交 ExtrudeBuilder 物件，建立拉伸特徵，並將新建立的物件賦值給 feature2
    feature2 = extrudeBuilder1.CommitFeature()

    # 刪除復原標記
    theSession.DeleteUndoMark(markId12, None)

    # 設定復原標記名稱
    theSession.SetUndoMarkName(markId8, "Extrude")

    # 取得拉伸的起點和終點延伸距離表達式
    expression8 = extrudeBuilder1.Limits.StartExtend.Value
    expression9 = extrudeBuilder1.Limits.EndExtend.Value

    # 銷毀 ExtrudeBuilder 物件
    extrudeBuilder1.Destroy()

    # 刪除表達式
    workPart.Expressions.Delete(expression6)
    workPart.Expressions.Delete(expression7)

    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording  # 工具 -> 日誌 -> 停止錄製，結束日誌錄製
    # ----------------------------------------------

# 檢查是否是直接執行此程式，如果是則執行 main 函數
if __name__ == "__main__":
    main()