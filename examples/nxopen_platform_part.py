# 導入必要的模組
import math
import NXOpen
import NXOpen.Annotations  # 註解相關功能
import NXOpen.Features     # 特徵建立功能
import NXOpen.GeometricUtilities  # 幾何工具
import NXOpen.Preferences  # 偏好設定
import NXOpen.UF            # 底層 UF 函數

def main():
    # 取得 UF 工作階段物件，UF 是 NX 的底層框架，用於存取 NX 內部資料結構和函數
    theUfSession = NXOpen.UF.UFSession.GetUFSession()

    # 關閉所有開啟的零件，避免衝突
    theUfSession.Part.CloseAll()

    # 取得 NX 開放式工作階段物件
    theSession = NXOpen.Session.GetSession()

    # ----------------------------------------------
    #   Menu: 檔案->新建...
    # ----------------------------------------------
    # 建立新的零件檔案物件
    fileNew1 = theSession.Parts.FileNew()

    # 設定模板檔案名稱
    fileNew1.TemplateFileName = "model-plain-1-mm-template.prt"

    # 設定不使用空白模板
    fileNew1.UseBlankTemplate = False

    # 設定應用程式名稱
    fileNew1.ApplicationName = "ModelTemplate"

    # 設定單位為毫米
    fileNew1.Units = NXOpen.Part.Units.Millimeters

    # 設定關係類型 (留空)
    fileNew1.RelationType = ""

    # 設定不使用主模型
    fileNew1.UsesMasterModel = "No"

    # 設定模板類型為項目
    fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item

    # 設定模板顯示名稱為模型
    fileNew1.TemplatePresentationName = "Model"

    # 設定項目類型 (留空)
    fileNew1.ItemType = ""

    # 設定專業化 (留空)
    fileNew1.Specialization = ""

    # 設定不允許建立替代表示
    fileNew1.SetCanCreateAltrep(False)

    # 設定新檔案名稱和路徑
    fileNew1.NewFileName = "C:\\Users\\kmol\\Downloads\\model1.prt"

    # 設定主檔案名稱 (留空)
    fileNew1.MasterFileName = ""

    # 設定為顯示零件
    fileNew1.MakeDisplayedPart = True

    # 設定顯示零件選項
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional

    # 提交新的零件檔案
    nXObject1 = fileNew1.Commit()

    # 取得工作零件和顯示零件物件
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    # 銷毀 fileNew1 物件
    fileNew1.Destroy()

    # 切換到建模應用程式
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")

    # ----------------------------------------------
    #   Menu: 插入->草圖...
    # ----------------------------------------------

    # 建立一個新的草圖建構器物件
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)

    # 定義草圖平面的原點和法向量
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)

    # 建立一個新的平面
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 設定草圖建構器的平面參考
    sketchInPlaceBuilder1.PlaneReference = plane1

    # 尋找毫米單位物件
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")

    # 建立兩個數值為 0 的系統表達式，單位為毫米
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)

    # 設定草圖偏好設定
    theSession.Preferences.Sketch.CreateInferredConstraints = True   # 自動建立推斷約束
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True  # 連續自動標註尺寸
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression  # 使用表達式作為尺寸標籤
    theSession.Preferences.Sketch.TextSizeFixed = True              # 使用固定文字大小
    theSession.Preferences.Sketch.FixedTextSize = 3.0                # 設定文字大小為 3.0
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True  # 顯示參考尺寸的括號
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False   # 不顯示參考幾何
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0         # 設定約束符號大小為 3.0
    theSession.Preferences.Sketch.DisplayObjectColor = False        # 不顯示物件顏色
    theSession.Preferences.Sketch.DisplayObjectName = True          # 顯示物件名稱

    # 提交草圖建構器，建立草圖特徵
    nXObject2 = sketchInPlaceBuilder1.Commit()

    # 取得草圖和特徵物件
    sketch1 = nXObject2
    feature1 = sketch1.Feature

    # 激活草圖
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)

    # 銷毀草圖建構器和沿路徑草圖建構器物件
    sketchInPlaceBuilder1.Destroy()

    # 嘗試刪除表達式 (如果沒有被使用)
    try:
        workPart.Expressions.Delete(expression2)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)

    try:
        workPart.Expressions.Delete(expression1)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)

    # 銷毀平面物件
    plane1.DestroyPlane()

    # ----------------------------------------------
    #   Menu: 插入->草圖曲線->矩形...
    # ----------------------------------------------
    # ----------------------------------------------
    # 使用兩點法建立矩形
    # ----------------------------------------------

    # 定義矩形的四個頂點
    startPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    endPoint1 = NXOpen.Point3d(88.0, 0.0, 0.0)
    startPoint2 = NXOpen.Point3d(88.0, 0.0, 0.0)
    endPoint2 = NXOpen.Point3d(88.0, 78.0, 0.0)
    startPoint3 = NXOpen.Point3d(88.0, 78.0, 0.0)
    endPoint3 = NXOpen.Point3d(0.0, 78.0, 0.0)
    startPoint4 = NXOpen.Point3d(0.0, 78.0, 0.0)
    endPoint4 = NXOpen.Point3d(0.0, 0.0, 0.0)

    # 建立四條線段
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)
    line4 = workPart.Curves.CreateLine(startPoint4, endPoint4)

    # 將線段添加到草圖中，不推斷約束
    theSession.ActiveSketch.AddGeometry(line1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    theSession.ActiveSketch.AddGeometry(line2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    theSession.ActiveSketch.AddGeometry(line3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    theSession.ActiveSketch.AddGeometry(line4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)

    # ----------------------------------------------
    #   建立幾何約束
    # ----------------------------------------------

    # 建立重合約束，將線段的端點連接起來
    geom1_1 = NXOpen.Sketch.ConstraintGeometry()
    geom1_1.Geometry = line1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    geom2_1.Geometry = line2
    geom2_1.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_1, geom2_1)

    # ... (類似地建立其他三個重合約束) ...

    # 建立水平約束，使第一條線段水平
    geom1 = NXOpen.Sketch.ConstraintGeometry()
    geom1.Geometry = line1
    geom1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint5 = theSession.ActiveSketch.CreateHorizontalConstraint(geom1)

    # 建立垂直約束，使相鄰線段垂直
    conGeom1_1 = NXOpen.Sketch.ConstraintGeometry()
    conGeom1_1.Geometry = line1
    conGeom1_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_1.SplineDefiningPointIndex = 0
    conGeom2_1 = NXOpen.Sketch.ConstraintGeometry()
    conGeom2_1.Geometry = line2
    conGeom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint6 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_1, conGeom2_1)

    # ... (類似地建立其他三個垂直約束) ...

    # 建立重合約束，將第一條線段的起點與草圖原點重合
    geom1_5 = NXOpen.Sketch.ConstraintGeometry()
    geom1_5.Geometry = line1
    geom1_5.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_5.SplineDefiningPointIndex = 0
    geom2_5 = NXOpen.Sketch.ConstraintGeometry()
    datumCsys1 = workPart.Features.FindObject("SKETCH(1:1B)")
    point1 = datumCsys1.FindObject("POINT 1") 
    geom2_5.Geometry = point1
    geom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint10 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_5, geom2_5)

    # ----------------------------------------------
    #   建立尺寸約束
    # ----------------------------------------------

    # 建立尺寸幾何物件，用於定義尺寸約束的幾何參考
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

    # 定義尺寸原點
    dimOrigin1 = NXOpen.Point3d(44.0, -9.9368099155661405, 0.0)

    # 建立水平尺寸約束，約束第一條線段的長度
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDimension(
        NXOpen.Sketch.ConstraintType.ParallelDim, 
        dimObject1_1, 
        dimObject2_1, 
        dimOrigin1, 
        NXOpen.Expression.Null, 
        NXOpen.Sketch.DimensionOption.CreateAsAutomatic
    )

    # 取得尺寸約束的相關物件
    sketchHelpedDimensionalConstraint1 = sketchDimensionalConstraint1
    dimension1 = sketchHelpedDimensionalConstraint1.AssociatedDimension
    expression3 = sketchHelpedDimensionalConstraint1.AssociatedExpression

    # ... (類似地建立垂直尺寸約束，約束第二條線段的長度) ...

    # 設定不自動標註尺寸到圓弧中心
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False

    # 更新草圖
    theSession.ActiveSketch.Update()

    # 設定自動標註尺寸到圓弧中心
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True

    # 更新約束和尺寸的顯示
    geoms1 = [NXOpen.SmartObject.Null] * 4 
    geoms1[0] = line1
    geoms1[1] = line2
    geoms1[2] = line3
    geoms1[3] = line4
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms1)
    geoms2 = [NXOpen.SmartObject.Null] * 4 
    geoms2[0] = line1
    geoms2[1] = line2
    geoms2[2] = line3
    geoms2[3] = line4
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms2)

    # ----------------------------------------------
    #   Menu: 檔案->完成草圖
    # ----------------------------------------------

    # 取得草圖物件
    sketch2 = theSession.ActiveSketch

    # 取消激活草圖
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)

    # ----------------------------------------------
    #   Menu: 插入->設計特徵->拉伸...
    # ----------------------------------------------

    # 建立一個拉伸建構器物件
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)

    # 建立一個截面物件，用於定義拉伸的形狀
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)

    # 設定拉伸建構器的截面
    extrudeBuilder1.Section = section1

    # 允許自相交截面
    extrudeBuilder1.AllowSelfIntersectingSection(True)

    # 取得草圖角度的單位
    unit2 = extrudeBuilder1.Draft.FrontDraftAngle.Units

    # 建立一個數值為 2.00 的系統表達式，單位為角度
    expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)

    # 設定距離公差
    extrudeBuilder1.DistanceTolerance = 0.01

    # 設定布林運算類型為建立
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

    # 設定目標實體為空
    targetBodies1 = [NXOpen.Body.Null] * 1
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)

    # 設定拉伸起始延伸距離為 0
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")

    # 設定拉伸結束延伸距離為 44
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("44")

    # 設定前草圖角度為 2 度
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")

    # 設定後草圖角度為 2 度
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")

    # 設定起始偏移距離為 0
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")

    # 設定結束偏移距離為 5
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")

    # 取得智慧體積輪廓建構器
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile

    # 設定不使用開放輪廓智慧體積選項
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False

    # 設定閉合輪廓規則為 Fci
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci

    # 設定截面的距離公差和鏈接公差
    section1.DistanceTolerance = 0.01
    section1.ChainingTolerance = 0.0094999999999999998

    # 設定截面只允許曲線
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)

    # 定義截面曲線
    curves1 = [NXOpen.ICurve.Null] * 4 
    curves1[0] = line4
    curves1[1] = line2
    curves1[2] = line3
    curves1[3] = line1

    # 定義種子點
    seedPoint1 = NXOpen.Point3d(29.333333333333329, 26.0, 0.0)

    # 建立區域邊界規則
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch2, curves1, seedPoint1, 0.01)

    # 允許截面自相交
    section1.AllowSelfIntersection(True)

    # 定義規則列表
    rules1 = [None] * 1 
    rules1[0] = regionBoundaryRule1

    # 定義輔助點
    helpPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)

    # 將規則添加到截面
    section1.AddToSection(rules1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)

    # 建立方向物件
    direction1 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 設定拉伸的方向
    extrudeBuilder1.Direction = direction1

    # 建立一個數值為 0 的系統表達式，單位為毫米
    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)

    # 設定父特徵為內部
    extrudeBuilder1.ParentFeatureInternal = False

    # 提交拉伸建構器，建立拉伸特徵
    feature2 = extrudeBuilder1.CommitFeature()

    # 取得拉伸的起始和結束延伸距離的表達式
    expression7 = extrudeBuilder1.Limits.StartExtend.Value
    expression8 = extrudeBuilder1.Limits.EndExtend.Value

    # 銷毀拉伸建構器
    extrudeBuilder1.Destroy()

    # 刪除表達式
    workPart.Expressions.Delete(expression5)
    workPart.Expressions.Delete(expression6)

    # ----------------------------------------------
    #   Menu: 插入->草圖...
    # ----------------------------------------------

    # 建立第二個草圖建構器
    sketchInPlaceBuilder2 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)

    # ----------------------------------------------
    #   建立坐標系
    # ----------------------------------------------

    # 建立一個標量物件，數值為 1.0
    scalar1 = workPart.Scalars.CreateScalar(1.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 尋找第一個拉伸特徵的邊緣
    extrude1 = feature2
    edge1 = extrude1.FindObject("EDGE * 130 * 150 {(0,0,44)(44,0,44)(88,0,44) EXTRUDE(2)}")

    # 在邊緣上建立一個點
    point2 = workPart.Points.CreatePoint(edge1, scalar1, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 尋找第一個拉伸特徵的另一個邊緣
    edge2 = extrude1.FindObject("EDGE * 130 * 160 {(88,0,44)(88,39,44)(88,78,44) EXTRUDE(2)}")

    # 建立一個方向物件
    direction2 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 尋找第一個拉伸特徵的面
    face1 = extrude1.FindObject("FACE 130 {(44,39,44) EXTRUDE(2)}")

    # 建立一個變換物件
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction2, point2, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)

    # 建立一個笛卡爾坐標系
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 設定草圖建構器的坐標系
    sketchInPlaceBuilder2.Csystem = cartesianCoordinateSystem1

    # 提交草圖建構器，建立草圖特徵
    nXObject3 = sketchInPlaceBuilder2.Commit()
    sketch3 = nXObject3
    feature3 = sketch3.Feature

    # 激活草圖
    sketch3.Activate(NXOpen.Sketch.ViewReorient.TrueValue)

    # 銷毀草圖建構器和沿路徑草圖建構器
    sketchInPlaceBuilder2.Destroy()
    #sketchAlongPathBuilder2.Destroy()

    # ----------------------------------------------
    #   Menu: 插入->草圖曲線->矩形...
    # ----------------------------------------------
    # ----------------------------------------------
    # 使用兩點法建立矩形
    # ----------------------------------------------

    # 定義矩形的四個頂點
    startPoint5 = NXOpen.Point3d(8.0, 10.0, 44.0)
    endPoint5 = NXOpen.Point3d(8.0, 70.0, 44.0)
    startPoint6 = NXOpen.Point3d(8.0, 70.0, 44.0)
    endPoint6 = NXOpen.Point3d(79.0, 70.0, 44.0)
    startPoint7 = NXOpen.Point3d(79.0, 70.0, 44.0)
    endPoint7 = NXOpen.Point3d(79.0, 10.0, 44.0)
    startPoint8 = NXOpen.Point3d(79.0, 10.0, 44.0)
    endPoint8 = NXOpen.Point3d(8.0, 10.0, 44.0)

    # 建立四條線段
    line5 = workPart.Curves.CreateLine(startPoint5, endPoint5)
    line6 = workPart.Curves.CreateLine(startPoint6, endPoint6)
    line7 = workPart.Curves.CreateLine(startPoint7, endPoint7)
    line8 = workPart.Curves.CreateLine(startPoint8, endPoint8)

    # 將線段添加到草圖中，不推斷約束
    theSession.ActiveSketch.AddGeometry(line5, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    theSession.ActiveSketch.AddGeometry(line6, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    theSession.ActiveSketch.AddGeometry(line7, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    theSession.ActiveSketch.AddGeometry(line8, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)

    # ----------------------------------------------
    #   建立幾何約束
    # ----------------------------------------------

    # ... (類似地建立重合約束和垂直約束，將線段連接成矩形) ...

    # 建立水平約束
    geom4 = NXOpen.Sketch.ConstraintGeometry()
    geom4.Geometry = line5
    geom4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint15 = theSession.ActiveSketch.CreateHorizontalConstraint(geom4)

    # ... (類似地建立垂直約束) ...

    # ----------------------------------------------
    #   建立尺寸約束
    # ----------------------------------------------

    # ... (類似地建立水平尺寸約束和垂直尺寸約束，約束矩形的尺寸) ...

    # 更新約束和尺寸的顯示
    geoms3 = [NXOpen.SmartObject.Null] * 4 
    geoms3[0] = line5
    geoms3[1] = line6
    geoms3[2] = line7
    geoms3[3] = line8
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms3)
    geoms4 = [NXOpen.SmartObject.Null] * 4 
    geoms4[0] = line5
    geoms4[1] = line6
    geoms4[2] = line7
    geoms4[3] = line8
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms4)

    # ----------------------------------------------
    #   Menu: 檔案->完成草圖
    # ----------------------------------------------

    # 取得草圖物件
    sketch4 = theSession.ActiveSketch

    # 取消激活草圖
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)

    # ----------------------------------------------
    #   Menu: 插入->設計特徵->拉伸...
    # ----------------------------------------------

    # 建立第二個拉伸建構器
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)

    # 建立截面物件
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    extrudeBuilder2.Section = section2

    # 允許自相交截面
    extrudeBuilder2.AllowSelfIntersectingSection(True)

    # 設定距離公差
    extrudeBuilder2.DistanceTolerance = 0.01

    # 設定拉伸起始延伸距離為 0
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("0")

    # 設定拉伸結束延伸距離為 44
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("44")

    # 設定前草圖角度為 2 度
    extrudeBuilder2.Draft.FrontDraftAngle.SetFormula("2")

    # 設定後草圖角度為 2 度
    extrudeBuilder2.Draft.BackDraftAngle.SetFormula("2")

    # 設定起始偏移距離為 0
    extrudeBuilder2.Offset.StartOffset.SetFormula("0")

    # 設定結束偏移距離為 5
    extrudeBuilder2.Offset.EndOffset.SetFormula("5")

    # 取得智慧體積輪廓建構器
    smartVolumeProfileBuilder2 = extrudeBuilder2.SmartVolumeProfile

    # 設定不使用開放輪廓智慧體積選項
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False

    # 設定閉合輪廓規則為 Fci
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci

    # 設定截面的距離公差和鏈接公差
    section2.DistanceTolerance = 0.01
    section2.ChainingTolerance = 0.0094999999999999998

    # 設定截面只允許曲線
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)

    # 建立曲線特徵規則
    features1 = [NXOpen.Features.Feature.Null] * 1
    sketchFeature1 = feature3
    features1[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1)

    # 允許截面自相交
    section2.AllowSelfIntersection(True)

    # 定義規則列表
    rules2 = [None] * 1
    rules2[0] = curveFeatureRule1

    # 定義輔助點
    helpPoint2 = NXOpen.Point3d(53.571849182720413, 70.0, 44.0)

    # 將規則添加到截面
    section2.AddToSection(rules2, line6, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)

    # 建立方向物件
    direction3 = workPart.Directions.CreateDirection(sketch4, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)

    # 設定拉伸方向
    extrudeBuilder2.Direction = direction3

    # 設定布林運算目標實體為第一個拉伸特徵
    targetBodies4 = [NXOpen.Body.Null] * 1
    body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
    targetBodies4[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies4)

    # 設定布林運算類型為減去
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    targetBodies6 = [NXOpen.Body.Null] * 1
    targetBodies6[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies6)

    # 反轉拉伸方向
    direction4 = extrudeBuilder2.Direction
    success1 = direction4.ReverseDirection()
    extrudeBuilder2.Direction = direction4

    # 設定拉伸結束延伸距離為 21
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("21")

    # 設定父特徵為內部
    extrudeBuilder2.ParentFeatureInternal = False

    # 提交拉伸建構器，建立拉伸特徵 (挖洞)
    feature4 = extrudeBuilder2.CommitFeature()

    # 取得拉伸的起始和結束延伸距離的表達式
    expression17 = extrudeBuilder2.Limits.StartExtend.Value
    expression18 = extrudeBuilder2.Limits.EndExtend.Value

    # 銷毀拉伸建構器
    extrudeBuilder2.Destroy()

    # ----------------------------------------------
    #   Menu: 工具->日誌->停止記錄
    # ----------------------------------------------

if __name__ == '__main__':
    main()