# 導入 NXOpen
import NXOpen
import NXOpen.UF
import NXOpen.Preferences
import NXOpen.Features
import NXOpen.GeometricUtilities

def main():
    theUI = NXOpen.UI.GetUI()
    theMsgBox = theUI.NXMessageBox
    theMsgBox.Show("簡要說明", NXOpen.NXMessageBox.DialogType.Information,"以下流程將建立一個簡單的長方體")
    # 取得目前開啟的工作階段
    theSession = NXOpen.Session.GetSession()
    theUfSession = NXOpen.UF.UFSession.GetUFSession()
    # 建立新零件檔案
    fileNew1 = theSession.Parts.FileNew()
    fileNew1.TemplateFileName = "model-plain-1-mm-template.prt"
    fileNew1.ApplicationName = "ModelTemplate"
    fileNew1.Units = NXOpen.Part.Units.Millimeters
    fileNew1.TemplatePresentationName = "Model"
    fileNew1.NewFileName = "C:\\tmp\\nxopen_record\\model1.prt"
    fileNew1.MakeDisplayedPart = True
    nXObject1 = fileNew1.Commit()
    # 建立工作零件
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # 建立輪廓草圖
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    sketchInPlaceBuilder1.PlaneReference = plane1
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    nXObject2 = sketchInPlaceBuilder1.Commit()
    sketch1 = nXObject2
    feature1 = sketch1.Feature
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    sketchInPlaceBuilder1.Destroy()
    sketchAlongPathBuilder1.Destroy()
    plane1.DestroyPlane()

    # ----------------------------------------------
    # Creating rectangle using By 2 Points method 
    # ----------------------------------------------
    rect_height = 20.0
    rect_width = 120.0
    startPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    endPoint1 = NXOpen.Point3d(rect_width, 0.0, 0.0)
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)

    startPoint2 = NXOpen.Point3d(rect_width, 0.0, 0.0)
    endPoint2 = NXOpen.Point3d(rect_width, rect_height, 0.0)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)

    startPoint3 = NXOpen.Point3d(rect_width, rect_height, 0.0)
    endPoint3 = NXOpen.Point3d(0.0, rect_height, 0.0)
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)

    startPoint4 = NXOpen.Point3d(0.0, rect_height, 0.0)
    endPoint4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    line4 = workPart.Curves.CreateLine(startPoint4, endPoint4)

    theSession.ActiveSketch.AddGeometry(line1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    theSession.ActiveSketch.AddGeometry(line2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    theSession.ActiveSketch.AddGeometry(line3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    theSession.ActiveSketch.AddGeometry(line4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)

    geom1_1 = NXOpen.Sketch.ConstraintGeometry()
    geom1_1.Geometry = line1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_1.SplineDefiningPointIndex = 0

    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    geom2_1.Geometry = line2
    geom2_1.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_1.SplineDefiningPointIndex = 0

    sketchGeometricConstraint1 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_1, geom2_1)

    geom1_2 = NXOpen.Sketch.ConstraintGeometry()
    geom1_2.Geometry = line2
    geom1_2.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_2.SplineDefiningPointIndex = 0

    geom2_2 = NXOpen.Sketch.ConstraintGeometry()
    geom2_2.Geometry = line3
    geom2_2.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_2.SplineDefiningPointIndex = 0

    sketchGeometricConstraint2 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_2, geom2_2)

    geom1_3 = NXOpen.Sketch.ConstraintGeometry()
    geom1_3.Geometry = line3
    geom1_3.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_3.SplineDefiningPointIndex = 0

    geom2_3 = NXOpen.Sketch.ConstraintGeometry()
    geom2_3.Geometry = line4
    geom2_3.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_3.SplineDefiningPointIndex = 0

    sketchGeometricConstraint3 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_3, geom2_3)

    geom1_4 = NXOpen.Sketch.ConstraintGeometry()
    geom1_4.Geometry = line4
    geom1_4.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_4.SplineDefiningPointIndex = 0

    geom2_4 = NXOpen.Sketch.ConstraintGeometry()
    geom2_4.Geometry = line1
    geom2_4.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_4.SplineDefiningPointIndex = 0

    sketchGeometricConstraint4 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_4, geom2_4)

    geom1 = NXOpen.Sketch.ConstraintGeometry()
    geom1.Geometry = line1
    geom1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint5 = theSession.ActiveSketch.CreateHorizontalConstraint(geom1)

    conGeom1_1 = NXOpen.Sketch.ConstraintGeometry()
    conGeom1_1.Geometry = line1
    conGeom1_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_1.SplineDefiningPointIndex = 0

    conGeom2_1 = NXOpen.Sketch.ConstraintGeometry()
    conGeom2_1.Geometry = line2
    conGeom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_1.SplineDefiningPointIndex = 0

    sketchGeometricConstraint6 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_1, conGeom2_1)

    conGeom1_2 = NXOpen.Sketch.ConstraintGeometry()
    conGeom1_2.Geometry = line2
    conGeom1_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_2.SplineDefiningPointIndex = 0

    conGeom2_2 = NXOpen.Sketch.ConstraintGeometry()
    conGeom2_2.Geometry = line3
    conGeom2_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_2.SplineDefiningPointIndex = 0

    sketchGeometricConstraint7 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_2, conGeom2_2)

    conGeom1_3 = NXOpen.Sketch.ConstraintGeometry()
    conGeom1_3.Geometry = line3
    conGeom1_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_3.SplineDefiningPointIndex = 0

    conGeom2_3 = NXOpen.Sketch.ConstraintGeometry()
    conGeom2_3.Geometry = line4
    conGeom2_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_3.SplineDefiningPointIndex = 0

    sketchGeometricConstraint8 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_3, conGeom2_3)

    conGeom1_4 = NXOpen.Sketch.ConstraintGeometry()
    conGeom1_4.Geometry = line4
    conGeom1_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_4.SplineDefiningPointIndex = 0

    conGeom2_4 = NXOpen.Sketch.ConstraintGeometry()
    conGeom2_4.Geometry = line1
    conGeom2_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_4.SplineDefiningPointIndex = 0

    sketchGeometricConstraint9 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_4, conGeom2_4)

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
    dimOrigin1 = NXOpen.Point3d(60.5, -13.761, 0.0)

    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_1, dimObject2_1, dimOrigin1, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)

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

    dimOrigin2 = NXOpen.Point3d(134.761, 15.0, 0.0)
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_2, dimObject2_2, dimOrigin2, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)

    theSession.ActiveSketch.Update()

    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True

    geoms1 = [NXOpen.SmartObject.Null] * 4 
    geoms1[0] = line1
    geoms1[1] = line2
    geoms1[2] = line3
    geoms1[3] = line4
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms1)

    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketch2 = theSession.ActiveSketch

    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)

    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------

    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)

    section1 = workPart.Sections.CreateSection(0.0095, 0.01, 0.5)

    extrudeBuilder1.Section = section1

    extrudeBuilder1.AllowSelfIntersectingSection(True)

    unit2 = extrudeBuilder1.Draft.FrontDraftAngle.Units

    extrudeBuilder1.DistanceTolerance = 0.01

    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)

    extrudeBuilder1.Limits.StartExtend.Value.RightHandSide = "0"

    extrudeBuilder1.Limits.EndExtend.Value.RightHandSide = "25"

    extrudeBuilder1.Draft.FrontDraftAngle.RightHandSide = "2"

    extrudeBuilder1.Draft.BackDraftAngle.RightHandSide = "2"

    extrudeBuilder1.Offset.StartOffset.RightHandSide = "0"

    extrudeBuilder1.Offset.EndOffset.RightHandSide = "5"

    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile

    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False

    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci

    section1.DistanceTolerance = 0.01

    section1.ChainingTolerance = 0.0095

    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)

    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = feature1
    features1[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1)

    section1.AllowSelfIntersection(True)

    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    helpPoint1 = NXOpen.Point3d(65.996, 29.0, 1.776e-15)
    section1.AddToSection(rules1, line3, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)

    direction1 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)

    extrudeBuilder1.Direction = direction1
    extrudeBuilder1.ParentFeatureInternal = False
    feature2 = extrudeBuilder1.CommitFeature()
    extrudeBuilder1.Destroy()

if __name__ == "__main__":
    main()