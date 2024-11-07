# NX 2312 Journal
#
import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

import os
import NXOpen.UF

FileName = "block.prt"
length = 200
width = 110
height = 520

# --------------------------------------------------------------------------------------------
current_directory = os.path.dirname(os.path.realpath(__file__))
theUfSession = NXOpen.UF.UFSession.GetUFSession()
theUfSession.Part.CloseAll() 
# --------------------------------------------------------------------------------------------
    
def new_file() : 
    global theSession, workPart
    theSession  = NXOpen.Session.GetSession() 
    fileNew1 = theSession.Parts.FileNew()
    fileNew1.TemplateFileName = "model-plain-1-mm-template.prt"
    fileNew1.Units = NXOpen.Part.Units.Millimeters
    fileNew1.TemplatePresentationName = "Model"
    fileNew1.NewFileName = current_directory + "\\" + FileName
    try:
        os.remove(fileNew1.NewFileName)
    except:
        nXObject1 = fileNew1.Commit()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    fileNew1.Destroy()

def xy_plane():
    theSession  = NXOpen.Session.GetSession() 
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    theSession.BeginTaskEnvironment()
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    sketchInPlaceBuilder1.PlaneReference = plane1

    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    simpleSketchInPlaceBuilder1 = workPart.Sketches.CreateSimpleSketchInPlaceBuilder()
    coordinates1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point1 = workPart.Points.CreatePoint(coordinates1)
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    matrix1 = NXOpen.Matrix3x3()
    matrix1.Xx = 1.0
    matrix1.Xy = 0.0
    matrix1.Xz = 0.0
    matrix1.Yx = 0.0
    matrix1.Yy = 1.0
    matrix1.Yz = 0.0
    matrix1.Zx = 0.0
    matrix1.Zy = 0.0
    matrix1.Zz = 1.0
    plane2 = workPart.Planes.CreateFixedTypePlane(origin2, matrix1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    coordinates2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2 = workPart.Points.CreatePoint(coordinates2)
    origin3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    vector1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction1 = workPart.Directions.CreateDirection(origin3, vector1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    origin4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    vector2 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction2 = workPart.Directions.CreateDirection(origin4, vector2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    origin5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    matrix2 = NXOpen.Matrix3x3()
    matrix2.Xx = 1.0
    matrix2.Xy = 0.0
    matrix2.Xz = 0.0
    matrix2.Yx = 0.0
    matrix2.Yy = 1.0
    matrix2.Yz = 0.0
    matrix2.Zx = 0.0
    matrix2.Zy = 0.0
    matrix2.Zz = 1.0
    plane3 = workPart.Planes.CreateFixedTypePlane(origin5, matrix2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane3, direction2, point2, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    simpleSketchInPlaceBuilder1.CoordinateSystem = cartesianCoordinateSystem1
    datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) X axis")
    simpleSketchInPlaceBuilder1.HorizontalReference.Value = datumAxis1
    point3 = simpleSketchInPlaceBuilder1.SketchOrigin
    simpleSketchInPlaceBuilder1.SketchOrigin = point3
    nXObject1 = simpleSketchInPlaceBuilder1.Commit()
    sketch1 = nXObject1
    feature1 = sketch1.Feature
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    sketchFindMovableObjectsBuilder1 = workPart.Sketches.CreateFindMovableObjectsBuilder()
    nXObject2 = sketchFindMovableObjectsBuilder1.Commit()
    sketchFindMovableObjectsBuilder1.Destroy()
    sketchInPlaceBuilder1.Destroy()
    sketchAlongPathBuilder1.Destroy()
    simpleSketchInPlaceBuilder1.Destroy()
    plane1.DestroyPlane()

def sketch_rect():
    global theSession
    # left upper point
    lux = -length/2
    luy = width/2
    # right upper point
    rux = length/2
    ruy = width/2
    startPoint1 = NXOpen.Point3d(lux, luy, 0.0)
    endPoint1 = NXOpen.Point3d(rux, ruy, 0.0)
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)
    
    # right lower point
    rlx = length/2
    rly = -width/2
    startPoint2 = NXOpen.Point3d(rux, ruy, 0.0)
    endPoint2 = NXOpen.Point3d(rlx, rly, 0.0)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)
    
    # left lower point
    llx = -length/2
    lly = -width/2
    startPoint3 = NXOpen.Point3d(rlx, rly, 0.0)
    endPoint3 = NXOpen.Point3d(llx, lly, 0.0)
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)
    
    startPoint4 = NXOpen.Point3d(llx, lly, 0.0)
    endPoint4 = NXOpen.Point3d(lux, luy, 0.0)
    line4 = workPart.Curves.CreateLine(startPoint4, endPoint4)
    
    theSession.ActiveSketch.AddGeometry(line1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    theSession.ActiveSketch.AddGeometry(line2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    theSession.ActiveSketch.AddGeometry(line3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    theSession.ActiveSketch.AddGeometry(line4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    # 選擇繪製 Rectangle 的正中心點
    coordinates3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point4 = workPart.Points.CreatePoint(coordinates3)
    
    # Rectangle 左上點為 startPoint5, 右下為 endPoint5
    startPoint5 = NXOpen.Point3d(lux, luy, 0.0)
    endPoint5 = NXOpen.Point3d(rlx, rly, 0.0)
    line5 = workPart.Curves.CreateLine(startPoint5, endPoint5)
    
    theSession.ActiveSketch.AddGeometry(point4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    theSession.ActiveSketch.AddGeometry(line5, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    convertToFromReferenceBuilder1 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    selectNXObjectList1 = convertToFromReferenceBuilder1.InputObjects
    added1 = selectNXObjectList1.Add(point4)
    added2 = selectNXObjectList1.Add(line5)
    convertToFromReferenceBuilder1.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Reference
    
    nXObject3 = convertToFromReferenceBuilder1.Commit()
    convertToFromReferenceBuilder1.Destroy()
    conGeom1_1 = NXOpen.Sketch.ConstraintGeometry()
    conGeom1_1.Geometry = line1
    conGeom1_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_1.SplineDefiningPointIndex = 0
    conGeom2_1 = NXOpen.Sketch.ConstraintGeometry()
    conGeom2_1.Geometry = line2
    conGeom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_1, conGeom2_1)
    
    conGeom1_2 = NXOpen.Sketch.ConstraintGeometry()
    conGeom1_2.Geometry = line2
    conGeom1_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_2.SplineDefiningPointIndex = 0
    conGeom2_2 = NXOpen.Sketch.ConstraintGeometry()
    conGeom2_2.Geometry = line3
    conGeom2_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint2 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_2, conGeom2_2)
    
    conGeom1_3 = NXOpen.Sketch.ConstraintGeometry()
    conGeom1_3.Geometry = line3
    conGeom1_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_3.SplineDefiningPointIndex = 0
    conGeom2_3 = NXOpen.Sketch.ConstraintGeometry()
    conGeom2_3.Geometry = line4
    conGeom2_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint3 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_3, conGeom2_3)
    
    conGeom1_4 = NXOpen.Sketch.ConstraintGeometry()
    conGeom1_4.Geometry = line4
    conGeom1_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_4.SplineDefiningPointIndex = 0
    conGeom2_4 = NXOpen.Sketch.ConstraintGeometry()
    conGeom2_4.Geometry = line1
    conGeom2_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint4 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_4, conGeom2_4)
    
    theSession.ActiveSketch.Update()
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
    
    objects1 = [NXOpen.NXObject.Null] * 4 
    objects1[0] = sketchGeometricConstraint1
    objects1[1] = sketchGeometricConstraint2
    objects1[2] = sketchGeometricConstraint3
    objects1[3] = sketchGeometricConstraint4

    sketchFindMovableObjectsBuilder2 = workPart.Sketches.CreateFindMovableObjectsBuilder()
    
    nXObject4 = sketchFindMovableObjectsBuilder2.Commit()
    sketchFindMovableObjectsBuilder2.Destroy()
    sketchWorkRegionBuilder1 = workPart.Sketches.CreateWorkRegionBuilder()
    sketchWorkRegionBuilder1.Scope = NXOpen.SketchWorkRegionBuilder.ScopeType.EntireSketch
    
    nXObject5 = sketchWorkRegionBuilder1.Commit()
    sketchWorkRegionBuilder1.Destroy()
    theSession.ActiveSketch.CalculateStatus()
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    theSession.EndTaskEnvironment()
    
def extrude():
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    extrudeBuilder1.Section = section1
    unit1 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    extrudeBuilder1.DistanceTolerance = 0.01
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula(str(height))
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    selectionIntentRuleOptions1 = workPart.ScRuleFactory.CreateRuleOptions()
    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = workPart.Features.FindObject("SKETCH(1)")
    features1[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1, NXOpen.DisplayableObject.Null, selectionIntentRuleOptions1)
    selectionIntentRuleOptions1.Dispose()
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    helpPoint1 = NXOpen.Point3d(-477.58594465840537, 360.5615238491884, 0.0)
    section1.AddToSection(rules1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    sketch1 = sketchFeature1.FindObject("SKETCH_000")
    direction1 = workPart.Directions.CreateDirection(sketch1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    extrudeBuilder1.Direction = direction1
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies2)
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    targetBodies3 = []
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies3)
    extrudeBuilder1.ParentFeatureInternal = False
    feature1 = extrudeBuilder1.CommitFeature()
    expression2 = extrudeBuilder1.Limits.StartExtend.Value
    expression3 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    workPart.Expressions.Delete(expression1)

def save_file():
    partSaveStatus1 = workPart.Save(NXOpen.BasePart.SaveComponents.TrueValue, NXOpen.BasePart.CloseAfterSave.FalseValue)
    partSaveStatus1.Dispose()
    
def main() : 
    new_file()
    xy_plane()
    sketch_rect()
    extrude()
    try:
        os.remove(current_directory + "\\" + FileName)
    except:
        save_file()
    
if __name__ == '__main__':
    main()
