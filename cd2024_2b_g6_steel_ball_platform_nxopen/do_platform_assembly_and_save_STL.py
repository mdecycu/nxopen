# NX 1872
import math
import NXOpen
import NXOpen.Assemblies
import NXOpen.Assemblies.ProductInterface
import NXOpen.PDM
import NXOpen.Positioning
import NXOpen.Preferences
import NXOpen.UF
import os

def main() : 
    # 處理 session 同名新增檔案
    # 取得 UF 工作階段物件，UF 是 NX 的底層框架，用於存取 NX 內部資料結構和函數
    theUfSession = NXOpen.UF.UFSession.GetUFSession()

    # 關閉所有開啟的零件，避免衝突
    theUfSession.Part.CloseAll() 

    current_directory = os.path.dirname(os.path.realpath(__file__))

    theSession  = NXOpen.Session.GetSession()
    # ----------------------------------------------
    #   Menu: File->New...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    fileNew1 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId1, "New Dialog")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    fileNew1.TemplateFileName = "assembly-mm-template.prt"
    
    fileNew1.UseBlankTemplate = False
    
    fileNew1.ApplicationName = "AssemblyTemplate"
    
    fileNew1.Units = NXOpen.Part.Units.Millimeters
    
    fileNew1.RelationType = ""
    
    fileNew1.UsesMasterModel = "No"
    
    fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew1.TemplatePresentationName = "Assembly"
    
    fileNew1.ItemType = ""
    
    fileNew1.Specialization = ""
    
    fileNew1.SetCanCreateAltrep(False)
    
    fileNew1.NewFileName = current_directory + "\\assembly1.prt"
    
    fileNew1.MasterFileName = ""
    
    fileNew1.MakeDisplayedPart = True
    
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    nXObject1 = fileNew1.Commit()
    
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    theSession.DeleteUndoMark(markId3, None)
    
    fileNew1.Destroy()
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder1 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner1 = workPart.ComponentAssembly.Positioner
    
    componentPositioner1.ClearNetwork()
    
    componentPositioner1.BeginAssemblyConstraints()
    
    allowInterpartPositioning1 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    unit2 = workPart.UnitCollection.FindObject("Degrees")
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression8 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network1 = componentPositioner1.EstablishNetwork()
    
    componentNetwork1 = network1
    componentNetwork1.MoveObjectsState = True
    
    componentNetwork1.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId4, "Add Component Dialog")
    
    componentNetwork1.MoveObjectsState = True
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder1.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder1.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder1.SetCount(1)
    
    addComponentBuilder1.SetScatterOption(True)
    
    addComponentBuilder1.ReferenceSet = "Unknown"
    
    addComponentBuilder1.Layer = -1
    
    # ----------------------------------------------
    #   Dialog Begin Add Component
    # ----------------------------------------------
    basePart1, partLoadStatus1 = theSession.Parts.OpenBase(current_directory + "\\base_w.prt")
    
    partLoadStatus1.Dispose()
    addComponentBuilder1.ReferenceSet = "Use Model"
    
    addComponentBuilder1.Layer = -1
    
    partstouse1 = [NXOpen.BasePart.Null] * 1 
    part1 = basePart1
    partstouse1[0] = part1
    addComponentBuilder1.SetPartsToAdd(partstouse1)
    
    productinterfaceobjects1 = addComponentBuilder1.GetAllProductInterfaceObjects()
    
    arrangement1 = workPart.ComponentAssembly.Arrangements.FindObject("Arrangement 1")
    componentPositioner1.PrimaryArrangement = arrangement1
    
    coordinates1 = NXOpen.Point3d(5.3932425322388635, -3.6075096622376726, 0.0)
    point1 = workPart.Points.CreatePoint(coordinates1)
    
    coordinates2 = NXOpen.Point3d(5.3932425322388635, -3.6075096622376726, 0.0)
    point2 = workPart.Points.CreatePoint(coordinates2)
    
    origin1 = NXOpen.Point3d(5.3932425322388635, -3.6075096622376726, 0.0)
    vector1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction1 = workPart.Directions.CreateDirection(origin1, vector1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin2 = NXOpen.Point3d(5.3932425322388635, -3.6075096622376726, 0.0)
    vector2 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction2 = workPart.Directions.CreateDirection(origin2, vector2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin3 = NXOpen.Point3d(5.3932425322388635, -3.6075096622376726, 0.0)
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
    plane1 = workPart.Planes.CreateFixedTypePlane(origin3, matrix1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane1, direction2, point2, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point3 = NXOpen.Point3d(5.3932425322388635, -3.6075096622376726, 0.0)
    orientation1 = NXOpen.Matrix3x3()
    
    orientation1.Xx = 1.0
    orientation1.Xy = 0.0
    orientation1.Xz = 0.0
    orientation1.Yx = 0.0
    orientation1.Yy = 1.0
    orientation1.Yz = 0.0
    orientation1.Zx = 0.0
    orientation1.Zy = 0.0
    orientation1.Zz = 1.0
    addComponentBuilder1.SetInitialLocationAndOrientation(point3, orientation1)
    
    movableObjects1 = [NXOpen.NXObject.Null] * 1 
    component1 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT base_w 1")
    movableObjects1[0] = component1
    componentNetwork1.SetMovingGroup(movableObjects1)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    theSession.DeleteUndoMark(markId6, None)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork1.Solve()
    
    componentPositioner1.ClearNetwork()
    
    nErrs1 = theSession.UpdateManager.AddToDeleteList(componentNetwork1)
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId5)
    
    componentPositioner1.EndAssemblyConstraints()
    
    logicalobjects1 = addComponentBuilder1.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder1.ComponentName = "BASE_W"
    
    nXObject2 = addComponentBuilder1.Commit()
    
    errorList1 = addComponentBuilder1.GetOperationFailures()
    
    errorList1.Dispose()
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "ComponentOperationUtilities CreateFixConstraint")
    
    componentPositioner2 = workPart.ComponentAssembly.Positioner
    
    componentPositioner2.ClearNetwork()
    
    network2 = componentPositioner2.EstablishNetwork()
    
    componentNetwork2 = network2
    componentNetwork2.MoveObjectsState = True
    
    componentNetwork2.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork2.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    constraint1 = componentPositioner2.CreateConstraint(True)
    
    componentConstraint1 = constraint1
    componentConstraint1.ConstraintType = NXOpen.Positioning.Constraint.Type.Fix
    
    component2 = nXObject2
    constraintReference1 = componentConstraint1.CreateConstraintReference(component2, component2, False, False, False)
    
    componentNetwork2.Solve()
    
    componentPositioner2.ClearNetwork()
    
    nErrs3 = theSession.UpdateManager.AddToDeleteList(componentNetwork2)
    
    nErrs4 = theSession.UpdateManager.DoUpdate(markId4)
    
    theSession.DeleteUndoMark(markId7, None)
    
    theSession.SetUndoMarkName(markId4, "Add Component")
    
    addComponentBuilder1.Destroy()
    
    workPart.Points.DeletePoint(point1)
    
    componentPositioner2.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId5, None)
    
    scaleAboutPoint1 = NXOpen.Point3d(43.654779022514141, 4.5473728148452235, 0.0)
    viewCenter1 = NXOpen.Point3d(-43.654779022514141, -4.5473728148452235, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(34.92382321801135, 3.6378982518761784, 0.0)
    viewCenter2 = NXOpen.Point3d(-34.923823218011272, -3.6378982518761784, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Components->Add Component...
    # ----------------------------------------------
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder2 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner3 = workPart.ComponentAssembly.Positioner
    
    componentPositioner3.ClearNetwork()
    
    componentPositioner3.PrimaryArrangement = arrangement1
    
    componentPositioner3.BeginAssemblyConstraints()
    
    allowInterpartPositioning2 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression9 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression13 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression14 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression16 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network3 = componentPositioner3.EstablishNetwork()
    
    componentNetwork3 = network3
    componentNetwork3.MoveObjectsState = True
    
    componentNetwork3.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId10, "Add Component Dialog")
    
    componentNetwork3.MoveObjectsState = True
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder2.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder2.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder2.SetCount(1)
    
    addComponentBuilder2.SetScatterOption(True)
    
    addComponentBuilder2.ReferenceSet = "Unknown"
    
    addComponentBuilder2.Layer = -1
    
    basePart2, partLoadStatus2 = theSession.Parts.OpenBase(current_directory + "\\s_link.prt")
    
    partLoadStatus2.Dispose()
    addComponentBuilder2.ReferenceSet = "Use Model"
    
    addComponentBuilder2.Layer = -1
    
    partstouse2 = [NXOpen.BasePart.Null] * 1 
    part2 = basePart2
    partstouse2[0] = part2
    addComponentBuilder2.SetPartsToAdd(partstouse2)
    
    productinterfaceobjects2 = addComponentBuilder2.GetAllProductInterfaceObjects()
    
    scaleAboutPoint3 = NXOpen.Point3d(29.68524973530965, -2.7162973614008914, 0.0)
    viewCenter3 = NXOpen.Point3d(-29.685249735309586, 2.7162973614008914, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(23.74819978824771, -2.1730378891206996, 0.0)
    viewCenter4 = NXOpen.Point3d(-23.748199788247682, 2.1730378891207129, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(18.998559830598168, -1.73843031129656, 0.0)
    viewCenter5 = NXOpen.Point3d(-18.99855983059815, 1.7384303112965813, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(15.198847864478545, -1.4900831239684746, 0.0)
    viewCenter6 = NXOpen.Point3d(-15.198847864478511, 1.4900831239684915, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint6, viewCenter6)
    
    coordinates3 = NXOpen.Point3d(66.993242532238867, 3.392490337762307, 21.0)
    point4 = workPart.Points.CreatePoint(coordinates3)
    
    origin4 = NXOpen.Point3d(66.993242532238867, 3.392490337762307, 21.0)
    vector3 = NXOpen.Vector3d(1.0, -0.0, -0.0)
    direction3 = workPart.Directions.CreateDirection(origin4, vector3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin5 = NXOpen.Point3d(66.993242532238867, 3.392490337762307, 21.0)
    vector4 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    direction4 = workPart.Directions.CreateDirection(origin5, vector4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin6 = NXOpen.Point3d(66.993242532238867, 3.392490337762307, 21.0)
    matrix2 = NXOpen.Matrix3x3()
    
    matrix2.Xx = 0.0
    matrix2.Xy = 1.0
    matrix2.Xz = 0.0
    matrix2.Yx = 0.0
    matrix2.Yy = -0.0
    matrix2.Yz = 1.0
    matrix2.Zx = 1.0
    matrix2.Zy = 0.0
    matrix2.Zz = -0.0
    plane2 = workPart.Planes.CreateFixedTypePlane(origin6, matrix2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane2, direction4, point4, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point5 = NXOpen.Point3d(66.993242532238867, 3.392490337762307, 21.0)
    orientation2 = NXOpen.Matrix3x3()
    
    orientation2.Xx = 0.0
    orientation2.Xy = 1.0
    orientation2.Xz = 0.0
    orientation2.Yx = 0.0
    orientation2.Yy = 0.0
    orientation2.Yz = 1.0
    orientation2.Zx = 1.0
    orientation2.Zy = 0.0
    orientation2.Zz = 0.0
    addComponentBuilder2.SetInitialLocationAndOrientation(point5, orientation2)
    
    movableObjects2 = [NXOpen.NXObject.Null] * 1 
    component3 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT s_link 1")
    movableObjects2[0] = component3
    componentNetwork3.SetMovingGroup(movableObjects2)
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    theSession.DeleteUndoMark(markId12, None)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork3.Solve()
    
    componentPositioner3.ClearNetwork()
    
    nErrs5 = theSession.UpdateManager.AddToDeleteList(componentNetwork3)
    
    nErrs6 = theSession.UpdateManager.DoUpdate(markId11)
    
    componentPositioner3.EndAssemblyConstraints()
    
    logicalobjects2 = addComponentBuilder2.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder2.ComponentName = "S_LINK"
    
    nXObject3 = addComponentBuilder2.Commit()
    
    errorList2 = addComponentBuilder2.GetOperationFailures()
    
    errorList2.Dispose()
    theSession.DeleteUndoMark(markId13, None)
    
    theSession.SetUndoMarkName(markId10, "Add Component")
    
    addComponentBuilder2.Destroy()
    
    componentPositioner3.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId11, None)
    
    scaleAboutPoint7 = NXOpen.Point3d(16.450517688612077, 1.4304797990097506, 0.0)
    viewCenter7 = NXOpen.Point3d(-16.450517688612042, -1.4304797990097371, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(13.160414150889654, 1.1443838392078058, 0.0)
    viewCenter8 = NXOpen.Point3d(-13.160414150889622, -1.1443838392077843, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner4 = workPart.ComponentAssembly.Positioner
    
    componentPositioner4.ClearNetwork()
    
    componentPositioner4.PrimaryArrangement = arrangement1
    
    componentPositioner4.BeginAssemblyConstraints()
    
    allowInterpartPositioning3 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression17 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression18 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression19 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression20 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression23 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression24 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network4 = componentPositioner4.EstablishNetwork()
    
    componentNetwork4 = network4
    componentNetwork4.MoveObjectsState = True
    
    componentNetwork4.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork4.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId16, "Assembly Constraints Dialog")
    
    componentNetwork4.MoveObjectsState = True
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint2 = componentPositioner4.CreateConstraint(True)
    
    componentConstraint2 = constraint2
    componentConstraint2.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    component4 = nXObject3
    edge1 = component4.FindObject("PROTO#.Features|EXTRUDE(2)|EDGE * 130 EXTRUDE(4) 160 {(2.25,1.7009618943233,2.8)(4.5,3,2.8)(2.25,4.2990381056767,2.8) EXTRUDE(2)}")
    constraintReference2 = componentConstraint2.CreateConstraintReference(component4, edge1, False, False, False)
    
    helpPoint1 = NXOpen.Point3d(69.793242532238864, 7.694478632689921, 24.744866753098499)
    constraintReference2.HelpPoint = helpPoint1
    
    edge2 = component2.FindObject("PROTO#.Features|EXTRUDE(8)|EDGE * 220 SIMPLE HOLE(18:1A) 3 {(61.6,8.2990381056766,20.25)(61.6,7,22.5)(61.6,5.7009618943233,20.25) EXTRUDE(8)}")
    constraintReference3 = componentConstraint2.CreateConstraintReference(component2, edge2, False, False, False)
    
    helpPoint2 = NXOpen.Point3d(66.993242532238867, 2.568248301073786, 22.25324581186436)
    constraintReference3.HelpPoint = helpPoint2
    
    constraintReference3.SetFixHint(True)
    
    componentNetwork4.Solve()
    
    componentPositioner4.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner4.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId17, None)
    
    theSession.UndoToMark(markId16, None)
    
    theSession.DeleteUndoMark(markId16, None)
    
    theSession.DeleteUndoMark(markId15, None)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Move Component...
    # ----------------------------------------------
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner5 = workPart.ComponentAssembly.Positioner
    
    componentPositioner5.ClearNetwork()
    
    componentPositioner5.PrimaryArrangement = arrangement1
    
    componentPositioner5.BeginMoveComponent()
    
    allowInterpartPositioning4 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression25 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression26 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression28 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression31 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression32 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network5 = componentPositioner5.EstablishNetwork()
    
    componentNetwork5 = network5
    componentNetwork5.MoveObjectsState = True
    
    componentNetwork5.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork5.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    expression33 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression34 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression35 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression36 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression37 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    componentNetwork5.RemoveAllConstraints()
    
    movableObjects3 = []
    componentNetwork5.SetMovingGroup(movableObjects3)
    
    componentNetwork5.Solve()
    
    theSession.SetUndoMarkName(markId19, "Move Component Dialog")
    
    componentNetwork5.MoveObjectsState = True
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component Update")
    
    componentNetwork5.RemoveAllConstraints()
    
    movableObjects4 = [NXOpen.NXObject.Null] * 1 
    movableObjects4[0] = component4
    componentNetwork5.SetMovingGroup(movableObjects4)
    
    componentNetwork5.Solve()
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Transform Origin")
    
    loaded1 = componentNetwork5.IsReferencedGeometryLoaded()
    
    componentNetwork5.BeginDrag()
    
    point6 = NXOpen.Point3d(68.393242532238872, 10.892490337762309, 24.0)
    direction5 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point6, direction5)
    
    point7 = NXOpen.Point3d(68.393242532238872, 6.0472530091624606, 24.845327496052292)
    direction6 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point7, direction6)
    
    point8 = NXOpen.Point3d(68.393242532238872, 4.9980275914422307, 24.89408462118686)
    direction7 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point8, direction7)
    
    point9 = NXOpen.Point3d(68.393242532238872, 4.2766851167595874, 24.96876166140424)
    direction8 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point9, direction8)
    
    point10 = NXOpen.Point3d(68.393242532238872, 3.6209192306844287, 24.97179718682176)
    direction9 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point10, direction9)
    
    point11 = NXOpen.Point3d(68.393242532238872, 3.0307299332167972, 25.012941908605743)
    direction10 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point11, direction10)
    
    point12 = NXOpen.Point3d(68.393242532238872, 2.2438108699266337, 25.049509752456661)
    direction11 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point12, direction11)
    
    point13 = NXOpen.Point3d(68.393242532238872, 1.7191981610665295, 25.128763670607107)
    direction12 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point13, direction12)
    
    point14 = NXOpen.Point3d(68.393242532238872, 1.0634322749913707, 25.131799196024634)
    direction13 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point14, direction13)
    
    point15 = NXOpen.Point3d(68.393242532238872, 0.47324297752374633, 25.17294391780861)
    direction14 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point15, direction14)
    
    point16 = NXOpen.Point3d(68.393242532238872, -0.51040585158897045, 25.259810239309637)
    direction15 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point16, direction15)
    
    point17 = NXOpen.Point3d(68.393242532238872, -0.96944197184156877, 25.157671931493887)
    direction16 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point17, direction16)
    
    point18 = NXOpen.Point3d(68.393242532238872, -1.2973249148791552, 25.131752016411063)
    direction17 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point18, direction17)
    
    point19 = NXOpen.Point3d(68.393242532238872, -1.4940546807016801, 25.072299782894831)
    direction18 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point19, direction18)
    
    point20 = NXOpen.Point3d(68.393242532238872, -1.6252078579167133, 25.050956745745072)
    direction19 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point20, direction19)
    
    point21 = NXOpen.Point3d(68.393242532238872, -1.7563610351317465, 24.919862997428975)
    direction20 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point21, direction20)
    
    point22 = NXOpen.Point3d(68.393242532238872, -1.9530908009542856, 24.695784697163251)
    direction21 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point22, direction21)
    
    point23 = NXOpen.Point3d(68.393242532238872, -2.2153971553843448, 24.433597200531057)
    direction22 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point23, direction22)
    
    point24 = NXOpen.Point3d(68.393242532238872, -2.5432800984219028, 24.243051218698735)
    direction23 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point24, direction23)
    
    point25 = NXOpen.Point3d(68.393242532238872, -2.7400098642444561, 24.073848274016179)
    direction24 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point25, direction24)
    
    point26 = NXOpen.Point3d(68.393242532238872, -2.8711630414594822, 23.942754525700078)
    direction25 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point26, direction25)
    
    point27 = NXOpen.Point3d(68.393242532238872, -2.9367396300669952, 23.849769973750444)
    direction26 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point27, direction26)
    
    point28 = NXOpen.Point3d(68.393242532238872, -3.0023162186745154, 23.756785421800817)
    direction27 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point28, direction27)
    
    point29 = NXOpen.Point3d(68.393242532238872, -3.0023162186745083, 23.647034710634486)
    direction28 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point29, direction28)
    
    point30 = NXOpen.Point3d(68.393242532238872, -3.0023162186745118, 23.537283999468151)
    direction29 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point30, direction29)
    
    point31 = NXOpen.Point3d(68.393242532238872, -3.0023162186745154, 23.427533288301817)
    direction30 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point31, direction30)
    
    point32 = NXOpen.Point3d(68.393242532238872, -3.0023162186745083, 23.317782577135485)
    direction31 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point32, direction31)
    
    point33 = NXOpen.Point3d(68.393242532238872, -3.0023162186745118, 23.208031865969147)
    direction32 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point33, direction32)
    
    point34 = NXOpen.Point3d(68.393242532238872, -3.0023162186745154, 23.153156510385987)
    direction33 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point34, direction33)
    
    point35 = NXOpen.Point3d(68.393242532238872, -2.9367396300669952, 23.026639640002951)
    direction34 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point35, direction34)
    
    point36 = NXOpen.Point3d(68.393242532238872, -2.8711630414594893, 22.845247414036752)
    direction35 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point36, direction35)
    
    point37 = NXOpen.Point3d(68.393242532238872, -2.8055864528519692, 22.663855188070549)
    direction36 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point37, direction36)
    
    point38 = NXOpen.Point3d(68.393242532238872, -2.6744332756369396, 22.465696802887646)
    direction37 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point38, direction37)
    
    point39 = NXOpen.Point3d(68.393242532238872, -2.6088566870294194, 22.33917993250461)
    direction38 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point39, direction38)
    
    point40 = NXOpen.Point3d(68.393242532238872, -2.5432800984218993, 22.212663062121575)
    direction39 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point40, direction39)
    
    point41 = NXOpen.Point3d(68.393242532238872, -2.5432800984219028, 22.048036995372076)
    direction40 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point41, direction40)
    
    point42 = NXOpen.Point3d(68.393242532238872, -2.5432800984219064, 21.883410928622581)
    direction41 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point42, direction41)
    
    point43 = NXOpen.Point3d(68.393242532238872, -2.5432800984219028, 21.773660217456243)
    direction42 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point43, direction42)
    
    point44 = NXOpen.Point3d(68.393242532238872, -2.5432800984219064, 21.718784861873079)
    direction43 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point44, direction43)
    
    point45 = NXOpen.Point3d(68.393242532238872, -2.5432800984219064, 21.609034150706744)
    direction44 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point45, direction44)
    
    point46 = NXOpen.Point3d(68.393242532238872, -2.5432800984219028, 21.55415879512358)
    direction45 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point46, direction45)
    
    point47 = NXOpen.Point3d(68.393242532238872, -2.5432800984219099, 21.499283439540413)
    direction46 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point47, direction46)
    
    point48 = NXOpen.Point3d(68.393242532238872, -2.5432800984218993, 21.444408083957242)
    direction47 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point48, direction47)
    
    point49 = NXOpen.Point3d(68.393242532238872, -2.6088566870294194, 21.406298887590783)
    direction48 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point49, direction48)
    
    point50 = NXOpen.Point3d(68.393242532238872, -2.6088566870294194, 21.406298887590783)
    direction49 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point50, direction49)
    
    point51 = NXOpen.Point3d(68.393242532238872, -2.6088566870294194, 21.46117424317395)
    direction50 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point51, direction50)
    
    point52 = NXOpen.Point3d(68.393242532238872, -2.608856687029423, 21.516049598757114)
    direction51 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point52, direction51)
    
    point53 = NXOpen.Point3d(68.393242532238872, -2.6088566870294194, 21.680675665506616)
    direction52 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point53, direction52)
    
    point54 = NXOpen.Point3d(68.393242532238872, -2.6088566870294194, 21.73555102108978)
    direction53 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point54, direction53)
    
    point55 = NXOpen.Point3d(68.393242532238872, -2.608856687029423, 21.790426376672947)
    direction54 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point55, direction54)
    
    point56 = NXOpen.Point3d(68.393242532238872, -2.6088566870294194, 21.900177087839282)
    direction55 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point56, direction55)
    
    point57 = NXOpen.Point3d(68.393242532238872, -2.608856687029423, 22.06480315458878)
    direction56 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point57, direction56)
    
    point58 = NXOpen.Point3d(68.393242532238872, -2.5432800984219028, 22.157787706538407)
    direction57 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point58, direction57)
    
    point59 = NXOpen.Point3d(68.393242532238872, -2.5432800984219064, 22.267538417704746)
    direction58 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point59, direction58)
    
    point60 = NXOpen.Point3d(68.393242532238872, -2.5432800984218993, 22.322413773287906)
    direction59 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point60, direction59)
    
    point61 = NXOpen.Point3d(68.393242532238872, -2.5432800984219099, 22.37728912887108)
    direction60 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point61, direction60)
    
    point62 = NXOpen.Point3d(68.393242532238872, -2.5432800984219099, 22.37728912887108)
    direction61 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point62, direction61)
    
    point63 = NXOpen.Point3d(68.393242532238872, -2.5432800984218993, 22.322413773287906)
    direction62 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point63, direction62)
    
    point64 = NXOpen.Point3d(68.393242532238872, -2.5432800984219064, 22.267538417704746)
    direction63 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point64, direction63)
    
    point65 = NXOpen.Point3d(68.393242532238872, -2.5432800984218993, 22.212663062121575)
    direction64 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point65, direction64)
    
    point66 = NXOpen.Point3d(68.393242532238872, -2.5432800984219028, 22.157787706538407)
    direction65 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point66, direction65)
    
    point67 = NXOpen.Point3d(68.393242532238872, -2.6088566870294159, 22.119678510171941)
    direction66 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point67, direction66)
    
    point68 = NXOpen.Point3d(68.393242532238872, -2.6088566870294194, 22.009927799005613)
    direction67 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point68, direction67)
    
    point69 = NXOpen.Point3d(68.393242532238872, -2.6088566870294194, 22.009927799005613)
    direction68 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point69, direction68)
    
    point70 = NXOpen.Point3d(68.393242532238872, -2.608856687029423, 22.06480315458878)
    direction69 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point70, direction69)
    
    point71 = NXOpen.Point3d(68.393242532238872, -2.477703509814404, 22.031270836155379)
    direction70 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point71, direction70)
    
    point72 = NXOpen.Point3d(68.393242532238872, -2.3465503325993708, 22.107489228888305)
    direction71 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point72, direction71)
    
    point73 = NXOpen.Point3d(68.393242532238872, -2.3465503325993637, 22.162364584471472)
    direction72 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point73, direction72)
    
    point74 = NXOpen.Point3d(68.393242532238872, -2.3465503325993637, 22.162364584471472)
    direction73 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point74, direction73)
    
    point75 = NXOpen.Point3d(68.393242532238872, -2.2809737439918507, 22.145598425254772)
    direction74 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point75, direction74)
    
    point76 = NXOpen.Point3d(68.393242532238872, -2.2809737439918507, 22.200473780837939)
    direction75 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point76, direction75)
    
    point77 = NXOpen.Point3d(68.393242532238872, -2.2809737439918507, 22.200473780837939)
    direction76 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point77, direction76)
    
    point78 = NXOpen.Point3d(68.393242532238872, -2.2153971553843377, 22.183707621621235)
    direction77 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point78, direction77)
    
    point79 = NXOpen.Point3d(68.393242532238872, -2.2153971553843377, 22.183707621621235)
    direction78 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point79, direction78)
    
    point80 = NXOpen.Point3d(68.393242532238872, -2.1498205667768246, 22.166941462404534)
    direction79 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point80, direction79)
    
    point81 = NXOpen.Point3d(68.393242532238872, -2.1498205667768246, 22.166941462404534)
    direction80 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point81, direction80)
    
    point82 = NXOpen.Point3d(68.393242532238872, -2.0842439781693045, 22.150175303187829)
    direction81 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point82, direction81)
    
    point83 = NXOpen.Point3d(68.393242532238872, -2.0842439781693045, 22.150175303187829)
    direction82 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point83, direction82)
    
    point84 = NXOpen.Point3d(68.393242532238872, -2.0842439781693116, 22.205050658770997)
    direction83 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point84, direction83)
    
    point85 = NXOpen.Point3d(68.393242532238872, -2.0186673895617844, 22.188284499554296)
    direction84 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point85, direction84)
    
    point86 = NXOpen.Point3d(68.393242532238872, -1.9530908009542856, 22.171518340337595)
    direction85 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point86, direction85)
    
    point87 = NXOpen.Point3d(68.393242532238872, -1.9530908009542856, 22.171518340337595)
    direction86 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point87, direction86)
    
    point88 = NXOpen.Point3d(68.393242532238872, -1.9530908009542784, 22.226393695920759)
    direction87 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point88, direction87)
    
    point89 = NXOpen.Point3d(68.393242532238872, -1.8875142123467654, 22.209627536704058)
    direction88 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point89, direction88)
    
    point90 = NXOpen.Point3d(68.393242532238872, -1.8875142123467654, 22.209627536704058)
    direction89 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point90, direction89)
    
    point91 = NXOpen.Point3d(68.393242532238872, -1.8219376237392524, 22.192861377487361)
    direction90 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point91, direction90)
    
    point92 = NXOpen.Point3d(68.393242532238872, -1.7563610351317465, 22.230970573853821)
    direction91 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point92, direction91)
    
    point93 = NXOpen.Point3d(68.393242532238872, -1.7563610351317465, 22.230970573853821)
    direction92 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point93, direction92)
    
    point94 = NXOpen.Point3d(68.393242532238872, -1.6907844465242334, 22.21420441463712)
    direction93 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point94, direction93)
    
    point95 = NXOpen.Point3d(68.393242532238872, -1.6907844465242334, 22.21420441463712)
    direction94 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point95, direction94)
    
    point96 = NXOpen.Point3d(68.393242532238872, -1.6907844465242334, 22.15932905905396)
    direction95 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point96, direction95)
    
    point97 = NXOpen.Point3d(68.393242532238872, -1.6907844465242334, 22.15932905905396)
    direction96 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point97, direction96)
    
    point98 = NXOpen.Point3d(68.393242532238872, -1.6252078579167062, 22.142562899837252)
    direction97 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point98, direction97)
    
    point99 = NXOpen.Point3d(68.393242532238872, -1.5596312693091932, 22.125796740620551)
    direction98 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point99, direction98)
    
    point100 = NXOpen.Point3d(68.393242532238872, -1.5596312693091861, 22.070921385037384)
    direction99 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point100, direction99)
    
    point101 = NXOpen.Point3d(68.393242532238872, -1.42847809209416, 21.982513711020811)
    direction100 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point101, direction100)
    
    point102 = NXOpen.Point3d(68.393242532238872, -1.362901503486647, 21.96574755180411)
    direction101 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point102, direction101)
    
    point103 = NXOpen.Point3d(68.393242532238872, -1.362901503486647, 21.96574755180411)
    direction102 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point103, direction102)
    
    point104 = NXOpen.Point3d(68.393242532238872, -1.2973249148791481, 21.948981392587413)
    direction103 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point104, direction103)
    
    point105 = NXOpen.Point3d(68.393242532238872, -1.2317483262716209, 21.932215233370712)
    direction104 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point105, direction104)
    
    point106 = NXOpen.Point3d(68.393242532238872, -1.2317483262716209, 21.932215233370712)
    direction105 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point106, direction105)
    
    point107 = NXOpen.Point3d(68.393242532238872, -1.231748326271628, 21.877339877787545)
    direction106 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point107, direction106)
    
    point108 = NXOpen.Point3d(68.393242532238872, -1.231748326271628, 21.877339877787545)
    direction107 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point108, direction107)
    
    point109 = NXOpen.Point3d(68.393242532238872, -1.166171737664115, 21.860573718570844)
    direction108 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point109, direction108)
    
    point110 = NXOpen.Point3d(68.393242532238872, -1.166171737664115, 21.805698362987673)
    direction109 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point110, direction109)
    
    point111 = NXOpen.Point3d(68.393242532238872, -1.1661717376641079, 21.750823007404506)
    direction110 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point111, direction110)
    
    point112 = NXOpen.Point3d(68.393242532238872, -1.1661717376641079, 21.750823007404506)
    direction111 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point112, direction111)
    
    point113 = NXOpen.Point3d(68.393242532238872, -1.166171737664115, 21.695947651821342)
    direction112 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point113, direction112)
    
    point114 = NXOpen.Point3d(68.393242532238872, -1.1005951490566019, 21.679181492604641)
    direction113 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point114, direction113)
    
    point115 = NXOpen.Point3d(68.393242532238872, -1.1005951490566019, 21.679181492604641)
    direction114 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point115, direction114)
    
    point116 = NXOpen.Point3d(68.393242532238872, -1.1005951490565948, 21.734056848187805)
    direction115 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point116, direction115)
    
    point117 = NXOpen.Point3d(68.393242532238872, -1.1005951490565948, 21.734056848187805)
    direction116 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point117, direction116)
    
    point118 = NXOpen.Point3d(68.393242532238872, -1.1005951490566019, 21.788932203770976)
    direction117 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point118, direction117)
    
    point119 = NXOpen.Point3d(68.393242532238872, -1.166171737664115, 21.805698362987673)
    direction118 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point119, direction118)
    
    point120 = NXOpen.Point3d(68.393242532238872, -1.166171737664115, 21.860573718570844)
    direction119 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point120, direction119)
    
    point121 = NXOpen.Point3d(68.393242532238872, -1.166171737664115, 21.860573718570844)
    direction120 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point121, direction120)
    
    point122 = NXOpen.Point3d(68.393242532238872, -1.1661717376641079, 21.915449074154008)
    direction121 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point122, direction121)
    
    point123 = NXOpen.Point3d(68.393242532238872, -1.1661717376641079, 21.970324429737172)
    direction122 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point123, direction122)
    
    point124 = NXOpen.Point3d(68.393242532238872, -1.1661717376641079, 22.025199785320343)
    direction123 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point124, direction123)
    
    point125 = NXOpen.Point3d(68.393242532238872, -1.1661717376641079, 22.025199785320343)
    direction124 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point125, direction124)
    
    point126 = NXOpen.Point3d(68.393242532238872, -1.1661717376641079, 22.025199785320343)
    direction125 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point126, direction125)
    
    point127 = NXOpen.Point3d(68.393242532238872, -1.1661717376641079, 22.025199785320343)
    direction126 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    componentNetwork5.DragByRay(point127, direction126)
    
    componentNetwork5.EndDrag()
    
    componentNetwork5.ResetDisplay()
    
    componentNetwork5.ApplyToModel()
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component")
    
    theSession.DeleteUndoMark(markId22, None)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component")
    
    componentNetwork5.Solve()
    
    componentPositioner5.ClearNetwork()
    
    nErrs7 = theSession.UpdateManager.AddToDeleteList(componentNetwork5)
    
    componentPositioner5.DeleteNonPersistentConstraints()
    
    nErrs8 = theSession.UpdateManager.DoUpdate(markId20)
    
    theSession.DeleteUndoMark(markId23, None)
    
    theSession.SetUndoMarkName(markId19, "Move Component")
    
    componentPositioner5.EndMoveComponent()
    
    componentPositioner5.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMarksUpToMark(markId20, None, False)
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = 0.76266653032894804
    rotMatrix1.Xy = 0.63392699050145063
    rotMatrix1.Xz = -0.12836017384597331
    rotMatrix1.Yx = -0.044870381940236126
    rotMatrix1.Yy = 0.24983520788258581
    rotMatrix1.Yz = 0.96724816760064181
    rotMatrix1.Zx = 0.64523361067177232
    rotMatrix1.Zy = -0.73192823392463113
    rotMatrix1.Zz = 0.21898549733584857
    translation1 = NXOpen.Point3d(-45.34630248601816, -17.481179580836308, 7.8272001559717665)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 5.2020351878798623)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = 0.68404324704923858
    rotMatrix2.Xy = 0.7133192060296385
    rotMatrix2.Xz = -0.15251408615459394
    rotMatrix2.Yx = -0.053194698138484327
    rotMatrix2.Yy = 0.257308155083179
    rotMatrix2.Yz = 0.96486415490349875
    rotMatrix2.Zx = 0.72749925103485868
    rotMatrix2.Zy = -0.65189586870674909
    rotMatrix2.Zz = 0.21395470573647765
    translation2 = NXOpen.Point3d(-48.285463739272231, -17.742969344573648, 2.265183988056048)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 5.2020351878798623)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner6 = workPart.ComponentAssembly.Positioner
    
    componentPositioner6.ClearNetwork()
    
    componentPositioner6.PrimaryArrangement = arrangement1
    
    componentPositioner6.BeginAssemblyConstraints()
    
    allowInterpartPositioning5 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression38 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression39 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression40 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression41 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression42 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression43 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression44 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression45 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network6 = componentPositioner6.EstablishNetwork()
    
    componentNetwork6 = network6
    componentNetwork6.MoveObjectsState = True
    
    componentNetwork6.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork6.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId25, "Assembly Constraints Dialog")
    
    componentNetwork6.MoveObjectsState = True
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    face1 = component2.FindObject("PROTO#.Features|SIMPLE HOLE(16:1A)|FACE 3 {(65.25,7,19.5) EXTRUDE(8)1}")
    line1 = workPart.Lines.CreateFaceAxis(face1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects1 = [NXOpen.TaggedObject.Null] * 1 
    objects1[0] = line1
    nErrs9 = theSession.UpdateManager.AddObjectsToDeleteList(objects1)
    
    line2 = workPart.Lines.CreateFaceAxis(face1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint3 = componentPositioner6.CreateConstraint(True)
    
    componentConstraint3 = constraint3
    componentConstraint3.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge3 = component4.FindObject("PROTO#.Features|EXTRUDE(2)|EDGE * 130 EXTRUDE(4) 170 {(11.25,1.7009618943233,2.8)(13.5,3,2.8)(11.25,4.2990381056767,2.8) EXTRUDE(2)}")
    constraintReference4 = componentConstraint3.CreateConstraintReference(component4, edge3, False, False, False)
    
    helpPoint3 = NXOpen.Point3d(69.793242532238864, 4.1478558247693336, 20.765295373232394)
    constraintReference4.HelpPoint = helpPoint3
    
    edge4 = component2.FindObject("PROTO#.Features|EXTRUDE(8)|EDGE * 160 SIMPLE HOLE(16:1A) 3 {(64.5,8.2990381056766,21.75)(64.5,7,19.5)(64.5,5.7009618943233,21.75) EXTRUDE(8)1}")
    constraintReference5 = componentConstraint3.CreateConstraintReference(component2, edge4, False, False, False)
    
    helpPoint4 = NXOpen.Point3d(69.893242532238858, 4.482597742745269, 19.969628297359971)
    constraintReference5.HelpPoint = helpPoint4
    
    constraintReference5.SetFixHint(True)
    
    objects2 = [NXOpen.TaggedObject.Null] * 1 
    objects2[0] = line2
    nErrs10 = theSession.UpdateManager.AddObjectsToDeleteList(objects2)
    
    componentNetwork6.Solve()
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    theSession.DeleteUndoMark(markId28, None)
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs11 = theSession.UpdateManager.DoUpdate(markId26)
    
    componentNetwork6.Solve()
    
    componentPositioner6.ClearNetwork()
    
    nErrs12 = theSession.UpdateManager.AddToDeleteList(componentNetwork6)
    
    componentPositioner6.DeleteNonPersistentConstraints()
    
    nErrs13 = theSession.UpdateManager.DoUpdate(markId26)
    
    theSession.DeleteUndoMark(markId29, None)
    
    theSession.SetUndoMarkName(markId25, "Assembly Constraints")
    
    componentPositioner6.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner6.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId26, None)
    
    theSession.DeleteUndoMark(markId27, None)
    
    theSession.DeleteUndoMark(markId24, None)
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = 0.20961768117123905
    rotMatrix3.Xy = 0.94696565780994579
    rotMatrix3.Xz = -0.24354972935515451
    rotMatrix3.Yx = -0.086022540661236796
    rotMatrix3.Yy = 0.26597800288385454
    rotMatrix3.Yz = 0.96013323267143613
    rotMatrix3.Zx = 0.97399206887868361
    rotMatrix3.Zy = -0.18031013535154519
    rotMatrix3.Zz = 0.13721408401082161
    translation3 = NXOpen.Point3d(-53.092049815378097, -17.679150500325907, -26.590520607096195)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 5.2020351878798623)
    
    scaleAboutPoint9 = NXOpen.Point3d(-14.698974645824554, 1.3732606070493669, 0.0)
    viewCenter9 = NXOpen.Point3d(14.698974645824581, -1.3732606070493454, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(-18.373718307280694, 1.7165757588117034, 0.0)
    viewCenter10 = NXOpen.Point3d(18.373718307280729, -1.7165757588116763, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(-24.794983182835534, 2.0662485985696342, 0.0)
    viewCenter11 = NXOpen.Point3d(24.794983182835569, -2.0662485985696204, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(-36.258689349899747, 2.3841329983495725, 0.0)
    viewCenter12 = NXOpen.Point3d(36.258689349899761, -2.3841329983495725, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint12, viewCenter12)
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = 0.75145994059320087
    rotMatrix4.Xy = 0.65385040304895214
    rotMatrix4.Xz = -0.088247425551018749
    rotMatrix4.Yx = -0.1965427600504443
    rotMatrix4.Yy = 0.34952308244584396
    rotMatrix4.Yz = 0.91608108719114423
    rotMatrix4.Zx = 0.62982450028195391
    rotMatrix4.Zy = -0.67105384677406876
    rotMatrix4.Zz = 0.39116215764604301
    translation4 = NXOpen.Point3d(-101.30707731001168, -11.637578163348758, 14.109801010891982)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 2.130753612955592)
    
    scaleAboutPoint13 = NXOpen.Point3d(-50.166131840272243, 12.914053741060185, 0.0)
    viewCenter13 = NXOpen.Point3d(50.166131840272264, -12.914053741060185, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(-40.1329054722178, 10.331242992848148, 0.0)
    viewCenter14 = NXOpen.Point3d(40.132905472217814, -10.331242992848141, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(-50.16613184027225, 12.914053741060187, 0.0)
    viewCenter15 = NXOpen.Point3d(50.166131840272271, -12.914053741060187, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(-62.707664800340297, 16.142567176325237, 0.0)
    viewCenter16 = NXOpen.Point3d(62.707664800340375, -16.142567176325223, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(-77.220453559825003, 19.984187730306488, 0.0)
    viewCenter17 = NXOpen.Point3d(77.22045355982506, -19.984187730306473, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint17, viewCenter17)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Components->Add Component...
    # ----------------------------------------------
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder3 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner7 = workPart.ComponentAssembly.Positioner
    
    componentPositioner7.ClearNetwork()
    
    componentPositioner7.PrimaryArrangement = arrangement1
    
    componentPositioner7.BeginAssemblyConstraints()
    
    allowInterpartPositioning6 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression46 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression47 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression48 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression49 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression50 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression51 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression52 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression53 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network7 = componentPositioner7.EstablishNetwork()
    
    componentNetwork7 = network7
    componentNetwork7.MoveObjectsState = True
    
    componentNetwork7.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId30, "Add Component Dialog")
    
    componentNetwork7.MoveObjectsState = True
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder3.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder3.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder3.SetCount(1)
    
    addComponentBuilder3.SetScatterOption(True)
    
    addComponentBuilder3.ReferenceSet = "Unknown"
    
    addComponentBuilder3.Layer = -1
    
    basePart3, partLoadStatus3 = theSession.Parts.OpenBase(current_directory + "\\platform.prt")
    
    partLoadStatus3.Dispose()
    addComponentBuilder3.ReferenceSet = "Use Model"
    
    addComponentBuilder3.Layer = -1
    
    partstouse3 = [NXOpen.BasePart.Null] * 1 
    part3 = basePart3
    partstouse3[0] = part3
    addComponentBuilder3.SetPartsToAdd(partstouse3)
    
    productinterfaceobjects3 = addComponentBuilder3.GetAllProductInterfaceObjects()
    
    scaleAboutPoint18 = NXOpen.Point3d(7.0332699536272925, 82.459027042526728, 0.0)
    viewCenter18 = NXOpen.Point3d(-7.0332699536272099, -82.459027042526728, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(8.7915874420340892, 103.07378380315839, 0.0)
    viewCenter19 = NXOpen.Point3d(-8.7915874420340643, -103.07378380315839, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint19, viewCenter19)
    
    coordinates4 = NXOpen.Point3d(-155.12412864966279, 193.52836660147298, 0.0)
    point128 = workPart.Points.CreatePoint(coordinates4)
    
    coordinates5 = NXOpen.Point3d(-155.12412864966279, 193.52836660147298, 0.0)
    point129 = workPart.Points.CreatePoint(coordinates5)
    
    origin7 = NXOpen.Point3d(-155.12412864966279, 193.52836660147298, 0.0)
    vector5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction127 = workPart.Directions.CreateDirection(origin7, vector5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin8 = NXOpen.Point3d(-155.12412864966279, 193.52836660147298, 0.0)
    vector6 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction128 = workPart.Directions.CreateDirection(origin8, vector6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin9 = NXOpen.Point3d(-155.12412864966279, 193.52836660147298, 0.0)
    matrix3 = NXOpen.Matrix3x3()
    
    matrix3.Xx = 1.0
    matrix3.Xy = 0.0
    matrix3.Xz = 0.0
    matrix3.Yx = 0.0
    matrix3.Yy = 1.0
    matrix3.Yz = 0.0
    matrix3.Zx = 0.0
    matrix3.Zy = 0.0
    matrix3.Zz = 1.0
    plane3 = workPart.Planes.CreateFixedTypePlane(origin9, matrix3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform3 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane3, direction128, point129, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem3 = workPart.CoordinateSystems.CreateCoordinateSystem(xform3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point130 = NXOpen.Point3d(-155.12412864966279, 193.52836660147298, 0.0)
    orientation3 = NXOpen.Matrix3x3()
    
    orientation3.Xx = 1.0
    orientation3.Xy = 0.0
    orientation3.Xz = 0.0
    orientation3.Yx = 0.0
    orientation3.Yy = 1.0
    orientation3.Yz = 0.0
    orientation3.Zx = 0.0
    orientation3.Zy = 0.0
    orientation3.Zz = 1.0
    addComponentBuilder3.SetInitialLocationAndOrientation(point130, orientation3)
    
    movableObjects5 = [NXOpen.NXObject.Null] * 1 
    component5 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT platform 1")
    movableObjects5[0] = component5
    componentNetwork7.SetMovingGroup(movableObjects5)
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Transform Origin")
    
    loaded2 = componentNetwork7.IsReferencedGeometryLoaded()
    
    componentNetwork7.BeginDrag()
    
    point131 = NXOpen.Point3d(-95.124128649662794, 193.52836660147298, 0.0)
    direction129 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point131, direction129)
    
    point132 = NXOpen.Point3d(-72.894649678108863, 193.52836660147298, 0.26832111923038582)
    direction130 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point132, direction130)
    
    point133 = NXOpen.Point3d(-71.860017794713116, 193.52836660147298, 0.49029863720568301)
    direction131 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point133, direction131)
    
    point134 = NXOpen.Point3d(-70.825385911317397, 193.52836660147298, 0.71227615518095888)
    direction132 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point134, direction132)
    
    point135 = NXOpen.Point3d(-69.840587826140649, 193.52836660147298, 0.50990018278112359)
    direction133 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point135, direction133)
    
    point136 = NXOpen.Point3d(-68.288640001047071, 193.52836660147298, 0.8428664597440445)
    direction134 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point136, direction134)
    
    point137 = NXOpen.Point3d(-66.736692175953465, 193.52836660147298, 1.1758327367069725)
    direction135 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point137, direction135)
    
    point138 = NXOpen.Point3d(-65.751894090776744, 193.52836660147295, 0.97345676430710171)
    direction136 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point138, direction136)
    
    point139 = NXOpen.Point3d(-65.234578149078828, 193.52836660147295, 1.0844455232947681)
    direction137 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point139, direction137)
    
    point140 = NXOpen.Point3d(-63.732464122204256, 193.52836660147295, 0.9930583098825565)
    direction138 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point140, direction138)
    
    point141 = NXOpen.Point3d(-61.24555201015297, 193.52836660147295, 0.69929512407052385)
    direction139 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point141, direction139)
    
    point142 = NXOpen.Point3d(-59.226122041580489, 193.52836660147295, 0.71889666964597865)
    direction140 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point142, direction140)
    
    point143 = NXOpen.Point3d(-57.206692073007986, 193.52836660147295, 0.73849821522143344)
    direction141 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point143, direction141)
    
    point144 = NXOpen.Point3d(-56.689376131310155, 193.52836660147295, 0.84948697420906427)
    direction142 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point144, direction142)
    
    point145 = NXOpen.Point3d(-56.689376131310155, 193.52836660147295, 0.84948697420906427)
    direction143 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point145, direction143)
    
    point146 = NXOpen.Point3d(-56.739209929529181, 193.52836660147295, 0.42513348383393179)
    direction144 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point146, direction144)
    
    point147 = NXOpen.Point3d(-56.838877525967213, 193.52836660147295, -0.42357349691630475)
    direction145 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point147, direction145)
    
    point148 = NXOpen.Point3d(-56.520896777145367, 193.52836660147295, -2.0099986994291399)
    direction146 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point148, direction146)
    
    point149 = NXOpen.Point3d(-56.720231970021445, 193.52836660147295, -3.7074126609296201)
    direction147 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point149, direction147)
    
    point150 = NXOpen.Point3d(-56.819899566459448, 193.52836660147295, -4.5561196416798566)
    direction148 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point150, direction148)
    
    point151 = NXOpen.Point3d(-56.969400961116513, 193.52836660147295, -5.8291801128052327)
    direction149 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point151, direction149)
    
    point152 = NXOpen.Point3d(-58.103700440950256, 193.52836660147295, -6.8998646115307452)
    direction150 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point152, direction150)
    
    point153 = NXOpen.Point3d(-58.670850180867149, 193.52836660147295, -7.4352068608935227)
    direction151 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point153, direction151)
    
    point154 = NXOpen.Point3d(-59.188166122565022, 193.52836660147295, -7.5461956198811606)
    direction152 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point154, direction152)
    
    point155 = NXOpen.Point3d(-59.188166122565022, 193.52836660147295, -7.5461956198811606)
    direction153 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point155, direction153)
    
    point156 = NXOpen.Point3d(-59.138332324346017, 193.52836660147295, -7.1218421295060281)
    direction154 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point156, direction154)
    
    point157 = NXOpen.Point3d(-59.038664727907978, 193.52836660147295, -6.2731351487557916)
    direction155 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point157, direction155)
    
    point158 = NXOpen.Point3d(-58.689828140374892, 193.52836660147295, -3.3026607161299353)
    direction156 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point158, direction156)
    
    point159 = NXOpen.Point3d(-58.808473696320618, 193.52836660147295, -0.018821552116619955)
    direction157 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point159, direction157)
    
    point160 = NXOpen.Point3d(-58.976953050485427, 193.52836660147295, 2.8406641215215913)
    direction158 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point160, direction158)
    
    point161 = NXOpen.Point3d(-59.762415942786077, 193.52836660147295, 4.7404540554218926)
    direction159 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point161, direction159)
    
    point162 = NXOpen.Point3d(-60.080396691607902, 193.52836660147295, 6.3268792579347419)
    direction160 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point162, direction160)
    
    point163 = NXOpen.Point3d(-60.865859583908566, 193.52836660147295, 8.2266691918350361)
    direction161 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point163, direction161)
    
    point164 = NXOpen.Point3d(-61.13400653451135, 193.52836660147295, 10.237447884723018)
    direction162 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point164, direction162)
    
    point165 = NXOpen.Point3d(-61.501821081552201, 193.52836660147295, 11.399519596860713)
    direction163 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point165, direction163)
    
    point166 = NXOpen.Point3d(-61.919469426812007, 193.52836660147295, 12.137237818623348)
    direction164 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point166, direction164)
    
    point167 = NXOpen.Point3d(-62.386951570290883, 193.52836660147295, 12.450602550010814)
    direction165 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point167, direction165)
    
    point168 = NXOpen.Point3d(-62.337117772071871, 193.52836660147295, 12.874956040385932)
    direction166 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point168, direction166)
    
    point169 = NXOpen.Point3d(-62.337117772071871, 193.52836660147295, 12.874956040385932)
    direction167 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point169, direction167)
    
    point170 = NXOpen.Point3d(-62.337117772071871, 193.52836660147295, 12.874956040385932)
    direction168 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point170, direction168)
    
    point171 = NXOpen.Point3d(-62.337117772071871, 193.52836660147295, 12.874956040385932)
    direction169 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork7.DragByRay(point171, direction169)
    
    componentNetwork7.EndDrag()
    
    componentNetwork7.ResetDisplay()
    
    componentNetwork7.ApplyToModel()
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    theSession.DeleteUndoMark(markId33, None)
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork7.Solve()
    
    componentPositioner7.ClearNetwork()
    
    nErrs14 = theSession.UpdateManager.AddToDeleteList(componentNetwork7)
    
    nErrs15 = theSession.UpdateManager.DoUpdate(markId31)
    
    componentPositioner7.EndAssemblyConstraints()
    
    logicalobjects3 = addComponentBuilder3.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder3.ComponentName = "PLATFORM"
    
    nXObject4 = addComponentBuilder3.Commit()
    
    errorList3 = addComponentBuilder3.GetOperationFailures()
    
    errorList3.Dispose()
    theSession.DeleteUndoMark(markId34, None)
    
    theSession.SetUndoMarkName(markId30, "Add Component")
    
    addComponentBuilder3.Destroy()
    
    workPart.Points.DeletePoint(point128)
    
    componentPositioner7.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId31, None)
    
    theSession.DeleteUndoMark(markId32, None)
    
    scaleAboutPoint20 = NXOpen.Point3d(-115.20011130941229, 76.926390117798334, 0.0)
    viewCenter20 = NXOpen.Point3d(115.20011130941229, -76.926390117798334, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(-137.84223844999573, 105.15799634329574, 0.0)
    viewCenter21 = NXOpen.Point3d(137.84223844999573, -105.15799634329578, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint21, viewCenter21)
    
    scaleAboutPoint22 = NXOpen.Point3d(-110.27379075999657, 84.126397074636557, 0.0)
    viewCenter22 = NXOpen.Point3d(110.27379075999664, -84.126397074636614, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(-88.219032607997264, 67.301117659709277, 0.0)
    viewCenter23 = NXOpen.Point3d(88.21903260799732, -67.301117659709305, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint23, viewCenter23)
    
    scaleAboutPoint24 = NXOpen.Point3d(-68.39248713527212, 55.053526878392788, 0.0)
    viewCenter24 = NXOpen.Point3d(68.39248713527212, -55.053526878392809, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint24, viewCenter24)
    
    origin10 = NXOpen.Point3d(79.441539182360046, 107.84544449121864, 21.02982482851554)
    workPart.ModelingViews.WorkView.SetOrigin(origin10)
    
    origin11 = NXOpen.Point3d(79.441539182360046, 107.84544449121864, 21.02982482851554)
    workPart.ModelingViews.WorkView.SetOrigin(origin11)
    
    origin12 = NXOpen.Point3d(83.076135545325982, 101.38183665389991, 4.0890584180293441)
    workPart.ModelingViews.WorkView.SetOrigin(origin12)
    
    origin13 = NXOpen.Point3d(83.076135545325982, 101.38183665389991, 4.0890584180293441)
    workPart.ModelingViews.WorkView.SetOrigin(origin13)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = 0.67193044055185858
    rotMatrix5.Xy = 0.73610904243417385
    rotMatrix5.Xz = -0.081565683387220658
    rotMatrix5.Yx = 0.046942254218583938
    rotMatrix5.Yy = 0.067581227237912989
    rotMatrix5.Yz = 0.99660885130220012
    rotMatrix5.Zx = 0.73912509619729205
    rotMatrix5.Zy = -0.67348070155844442
    rotMatrix5.Zz = 0.010855265988461654
    translation5 = NXOpen.Point3d(-138.52515256892582, 8.6843196101887941, 26.599950537752633)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 0.8727566798666111)
    
    rotMatrix6 = NXOpen.Matrix3x3()
    
    rotMatrix6.Xx = -0.28122589824866945
    rotMatrix6.Xy = 0.95852755628885855
    rotMatrix6.Xz = -0.046226810285134042
    rotMatrix6.Yx = 0.15768890929891785
    rotMatrix6.Yy = 0.093673693035266334
    rotMatrix6.Yz = 0.98303583206170575
    rotMatrix6.Zx = 0.94659716988714093
    rotMatrix6.Zy = 0.26916567958795068
    rotMatrix6.Zz = -0.17749263335025997
    translation6 = NXOpen.Point3d(-165.45465010730476, 5.7609203967837885, -83.032652734984268)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation6, 0.8727566798666111)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner8 = workPart.ComponentAssembly.Positioner
    
    componentPositioner8.ClearNetwork()
    
    componentPositioner8.PrimaryArrangement = arrangement1
    
    componentPositioner8.BeginAssemblyConstraints()
    
    allowInterpartPositioning7 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression54 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression55 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression56 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression57 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression58 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression59 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression60 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression61 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network8 = componentPositioner8.EstablishNetwork()
    
    componentNetwork8 = network8
    componentNetwork8.MoveObjectsState = True
    
    componentNetwork8.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork8.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId37, "Assembly Constraints Dialog")
    
    componentNetwork8.MoveObjectsState = True
    
    componentNetwork8.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    scaleAboutPoint25 = NXOpen.Point3d(-119.74748412425748, 86.400083482059173, 0.0)
    viewCenter25 = NXOpen.Point3d(119.74748412425748, -86.400083482059202, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint25, viewCenter25)
    
    scaleAboutPoint26 = NXOpen.Point3d(-96.283040399656144, 68.635013685397183, 0.0)
    viewCenter26 = NXOpen.Point3d(96.283040399656144, -68.635013685397197, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint26, viewCenter26)
    
    scaleAboutPoint27 = NXOpen.Point3d(-77.220453559824961, 54.519968468117639, 0.0)
    viewCenter27 = NXOpen.Point3d(77.220453559825017, -54.519968468117639, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint27, viewCenter27)
    
    scaleAboutPoint28 = NXOpen.Point3d(-62.086796832020056, 43.150323798253979, 0.0)
    viewCenter28 = NXOpen.Point3d(62.086796832020106, -43.150323798253929, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint28, viewCenter28)
    
    face2 = component2.FindObject("PROTO#.Features|SIMPLE HOLE(14:1A)|FACE 3 {(62.95,62.9,59.5) EXTRUDE(6)}")
    line3 = workPart.Lines.CreateFaceAxis(face2, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects3 = [NXOpen.TaggedObject.Null] * 1 
    objects3[0] = line3
    nErrs16 = theSession.UpdateManager.AddObjectsToDeleteList(objects3)
    
    scaleAboutPoint29 = NXOpen.Point3d(2.4834718732808105, 18.750212643270086, 0.0)
    viewCenter29 = NXOpen.Point3d(-2.483471873280747, -18.750212643270043, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint29, viewCenter29)
    
    scaleAboutPoint30 = NXOpen.Point3d(3.1043398416010124, 23.282548812007555, 0.0)
    viewCenter30 = NXOpen.Point3d(-3.1043398416009333, -23.282548812007501, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint30, viewCenter30)
    
    scaleAboutPoint31 = NXOpen.Point3d(3.8804248020012664, 28.715143534809318, 0.0)
    viewCenter31 = NXOpen.Point3d(-3.8804248020011998, -28.715143534809268, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(110.83463340716085, -16.006752308255134, 0.0)
    viewCenter32 = NXOpen.Point3d(-110.83463340716081, 16.006752308255198, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(88.667706725728706, -12.805401846604092, 0.0)
    viewCenter33 = NXOpen.Point3d(-88.667706725728635, 12.805401846604191, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint33, viewCenter33)
    
    scaleAboutPoint34 = NXOpen.Point3d(71.399816356823138, -10.399538469363316, 0.0)
    viewCenter34 = NXOpen.Point3d(-71.399816356823052, 10.399538469363408, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint34, viewCenter34)
    
    rotMatrix7 = NXOpen.Matrix3x3()
    
    rotMatrix7.Xx = 0.24465851170683048
    rotMatrix7.Xy = 0.96222243286098197
    rotMatrix7.Xz = -0.11945795221955165
    rotMatrix7.Yx = 0.079026428877862306
    rotMatrix7.Yy = 0.10300368613925097
    rotMatrix7.Yz = 0.99153671852359382
    rotMatrix7.Zx = 0.96638348298602783
    rotMatrix7.Zy = -0.25202823322163143
    rotMatrix7.Zz = -0.050840274104025036
    translation7 = NXOpen.Point3d(-145.07651553129605, -20.549475303704071, -23.353459252755922)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix7, translation7, 2.1307536129555937)
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint4 = componentPositioner8.CreateConstraint(True)
    
    componentConstraint4 = constraint4
    componentConstraint4.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge5 = component2.FindObject("PROTO#.Features|EXTRUDE(6)|EDGE * 170 SIMPLE HOLE(14:1A) 3 {(64.2490381056767,65.9,61.75)(62.95,65.9,59.5)(61.6509618943233,65.9,61.75) EXTRUDE(6)}")
    constraintReference6 = componentConstraint4.CreateConstraintReference(component2, edge5, False, False, False)
    
    helpPoint5 = NXOpen.Point3d(67.286719826397075, 62.292490337762324, 62.064781560715964)
    constraintReference6.HelpPoint = helpPoint5
    
    component6 = nXObject4
    edge6 = component6.FindObject("PROTO#.Features|EXTRUDE(6)|EDGE * 430 SIMPLE HOLE(14:1A) 3 {(60.75,3,-4.7009618943233)(58.5,3,-6)(60.75,3,-7.2990381056767) EXTRUDE(6)4}")
    constraintReference7 = componentConstraint4.CreateConstraintReference(component6, edge6, False, False, False)
    
    helpPoint6 = NXOpen.Point3d(-60.879425729548103, 196.52836660147298, 6.5212133243295956)
    constraintReference7.HelpPoint = helpPoint6
    
    constraintReference7.SetFixHint(True)
    
    componentNetwork8.Solve()
    
    scaleAboutPoint35 = NXOpen.Point3d(-44.578320125390405, 13.286574522052351, 0.0)
    viewCenter35 = NXOpen.Point3d(44.578320125390469, -13.286574522052257, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint35, viewCenter35)
    
    scaleAboutPoint36 = NXOpen.Point3d(-56.34376812505819, 16.763435144645474, 0.0)
    viewCenter36 = NXOpen.Point3d(56.343768125058247, -16.763435144645367, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint36, viewCenter36)
    
    scaleAboutPoint37 = NXOpen.Point3d(-70.817752636522883, 21.148315170906891, 0.0)
    viewCenter37 = NXOpen.Point3d(70.817752636522982, -21.148315170906791, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint37, viewCenter37)
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    theSession.DeleteUndoMark(markId40, None)
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs17 = theSession.UpdateManager.DoUpdate(markId38)
    
    componentNetwork8.Solve()
    
    componentPositioner8.ClearNetwork()
    
    nErrs18 = theSession.UpdateManager.AddToDeleteList(componentNetwork8)
    
    componentPositioner8.DeleteNonPersistentConstraints()
    
    nErrs19 = theSession.UpdateManager.DoUpdate(markId38)
    
    theSession.DeleteUndoMark(markId41, None)
    
    theSession.SetUndoMarkName(markId37, "Assembly Constraints")
    
    componentPositioner8.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner8.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId38, None)
    
    theSession.DeleteUndoMark(markId39, None)
    
    theSession.DeleteUndoMark(markId36, None)
    
    origin14 = NXOpen.Point3d(46.610158362488612, 80.405727129349287, 28.035147408715048)
    workPart.ModelingViews.WorkView.SetOrigin(origin14)
    
    origin15 = NXOpen.Point3d(46.610158362488612, 80.405727129349287, 28.035147408715048)
    workPart.ModelingViews.WorkView.SetOrigin(origin15)
    
    rotMatrix8 = NXOpen.Matrix3x3()
    
    rotMatrix8.Xx = 0.81247841248959141
    rotMatrix8.Xy = 0.57291519186634177
    rotMatrix8.Xz = -0.10792132396863589
    rotMatrix8.Yx = 0.041605015595458428
    rotMatrix8.Yy = 0.12766436840614334
    rotMatrix8.Yz = 0.9909444140398399
    rotMatrix8.Zx = 0.58150481676052479
    rotMatrix8.Zy = -0.80961101275131453
    rotMatrix8.Zz = 0.079888397881635292
    translation8 = NXOpen.Point3d(-102.2907918547937, -38.603074418998084, 28.207666463071906)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix8, translation8, 1.090945849833264)
    
    rotMatrix9 = NXOpen.Matrix3x3()
    
    rotMatrix9.Xx = 0.84131944120836
    rotMatrix9.Xy = 0.53050398000004373
    rotMatrix9.Xz = -0.10366834159454362
    rotMatrix9.Yx = 0.041605015595458428
    rotMatrix9.Yy = 0.12766436840614334
    rotMatrix9.Yz = 0.9909444140398399
    rotMatrix9.Zx = 0.53893470896032558
    rotMatrix9.Zy = -0.83801392365733962
    rotMatrix9.Zz = 0.085334888728319958
    translation9 = NXOpen.Point3d(-102.03593849651874, -38.603074418998084, 32.416452680862847)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix9, translation9, 1.090945849833264)
    
    rotMatrix10 = NXOpen.Matrix3x3()
    
    rotMatrix10.Xx = 0.86476853483142091
    rotMatrix10.Xy = 0.49123995806649662
    rotMatrix10.Xz = -0.10420501314399667
    rotMatrix10.Yx = 0.11909636367189978
    rotMatrix10.Yy = 0.00096188906871794329
    rotMatrix10.Yz = 0.99288223416956589
    rotMatrix10.Zx = 0.48784366074147534
    rotMatrix10.Zy = -0.87102375304479551
    rotMatrix10.Zz = -0.057673081295431458
    translation10 = NXOpen.Point3d(-101.41030756693378, -36.847360012816161, 43.165474294228133)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix10, translation10, 1.090945849833264)
    
    rotMatrix11 = NXOpen.Matrix3x3()
    
    rotMatrix11.Xx = 0.92590785878800552
    rotMatrix11.Xy = 0.35712659144935682
    rotMatrix11.Xz = -0.12310659898790841
    rotMatrix11.Yx = 0.098869073686249628
    rotMatrix11.Yy = 0.085425036544790778
    rotMatrix11.Yz = 0.99142698641893989
    rotMatrix11.Zx = 0.36458132604815019
    rotMatrix11.Zy = -0.93014147354640453
    rotMatrix11.Zz = 0.04378693738874849
    translation11 = NXOpen.Point3d(-97.348707958355376, -40.11317056497824, 50.773321141901313)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix11, translation11, 1.090945849833264)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Components->Add Component...
    # ----------------------------------------------
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder4 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner9 = workPart.ComponentAssembly.Positioner
    
    componentPositioner9.ClearNetwork()
    
    componentPositioner9.PrimaryArrangement = arrangement1
    
    componentPositioner9.BeginAssemblyConstraints()
    
    allowInterpartPositioning8 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression62 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression63 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression64 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression65 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression66 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression67 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression68 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression69 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network9 = componentPositioner9.EstablishNetwork()
    
    componentNetwork9 = network9
    componentNetwork9.MoveObjectsState = True
    
    componentNetwork9.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId42, "Add Component Dialog")
    
    componentNetwork9.MoveObjectsState = True
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder4.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder4.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder4.SetCount(1)
    
    addComponentBuilder4.SetScatterOption(True)
    
    addComponentBuilder4.ReferenceSet = "Unknown"
    
    addComponentBuilder4.Layer = -1
    
    basePart4, partLoadStatus4 = theSession.Parts.OpenBase(current_directory + "\\y_link.prt")
    
    partLoadStatus4.Dispose()
    addComponentBuilder4.ReferenceSet = "Use Model"
    
    addComponentBuilder4.Layer = -1
    
    partstouse4 = [NXOpen.BasePart.Null] * 1 
    part4 = basePart4
    partstouse4[0] = part4
    addComponentBuilder4.SetPartsToAdd(partstouse4)
    
    productinterfaceobjects4 = addComponentBuilder4.GetAllProductInterfaceObjects()
    
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    expression70 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression71 = workPart.Expressions.CreateSystemExpressionWithUnits("p9_x=0.00000000000", unit1)
    
    expression72 = workPart.Expressions.CreateSystemExpressionWithUnits("p10_y=0.00000000000", unit1)
    
    expression73 = workPart.Expressions.CreateSystemExpressionWithUnits("p11_z=0.00000000000", unit1)
    
    expression74 = workPart.Expressions.CreateSystemExpressionWithUnits("p12_xdelta=0.00000000000", unit1)
    
    expression75 = workPart.Expressions.CreateSystemExpressionWithUnits("p13_ydelta=0.00000000000", unit1)
    
    expression76 = workPart.Expressions.CreateSystemExpressionWithUnits("p14_zdelta=0.00000000000", unit1)
    
    expression77 = workPart.Expressions.CreateSystemExpressionWithUnits("p15_radius=0.00000000000", unit1)
    
    expression78 = workPart.Expressions.CreateSystemExpressionWithUnits("p16_angle=0.00000000000", unit2)
    
    expression79 = workPart.Expressions.CreateSystemExpressionWithUnits("p17_zdelta=0.00000000000", unit1)
    
    expression80 = workPart.Expressions.CreateSystemExpressionWithUnits("p18_radius=0.00000000000", unit1)
    
    expression81 = workPart.Expressions.CreateSystemExpressionWithUnits("p19_angle1=0.00000000000", unit2)
    
    expression82 = workPart.Expressions.CreateSystemExpressionWithUnits("p20_angle2=0.00000000000", unit2)
    
    expression83 = workPart.Expressions.CreateSystemExpressionWithUnits("p21_distance=0", unit1)
    
    expression84 = workPart.Expressions.CreateSystemExpressionWithUnits("p22_arclen=0", unit1)
    
    expression85 = workPart.Expressions.CreateSystemExpressionWithUnits("p23_percent=0", NXOpen.Unit.Null)
    
    theSession.SetUndoMarkName(markId44, "Point Dialog")
    
    expression86 = workPart.Expressions.CreateSystemExpressionWithUnits("p24_x=0.00000000000", unit1)
    
    scalar1 = workPart.Scalars.CreateScalarExpression(expression86, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression87 = workPart.Expressions.CreateSystemExpressionWithUnits("p25_y=0.00000000000", unit1)
    
    scalar2 = workPart.Scalars.CreateScalarExpression(expression87, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression88 = workPart.Expressions.CreateSystemExpressionWithUnits("p26_z=0.00000000000", unit1)
    
    scalar3 = workPart.Scalars.CreateScalarExpression(expression88, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point172 = workPart.Points.CreatePoint(scalar1, scalar2, scalar3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression71.SetFormula("0")
    
    expression72.SetFormula("0")
    
    expression73.SetFormula("0")
    
    expression71.SetFormula("0.00000000000")
    
    expression72.SetFormula("0.00000000000")
    
    expression73.SetFormula("0.00000000000")
    
    expression71.SetFormula("0")
    
    expression72.SetFormula("0")
    
    expression73.SetFormula("0")
    
    expression71.SetFormula("0.00000000000")
    
    expression72.SetFormula("0.00000000000")
    
    expression73.SetFormula("0.00000000000")
    
    expression85.SetFormula("100.00000000000")
    
    # ----------------------------------------------
    #   Dialog Begin Point
    # ----------------------------------------------
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression71)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression72)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression73)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression74)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression75)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression76)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression77)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression78)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression79)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression80)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression81)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression82)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression83)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression84)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression85)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Expressions.Delete(expression70)
    
    theSession.UndoToMark(markId44, None)
    
    theSession.DeleteUndoMark(markId44, None)
    
    theSession.DeleteUndoMark(markId44, None)
    
    movableObjects6 = [NXOpen.NXObject.Null] * 1 
    component7 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT y_link 1")
    movableObjects6[0] = component7
    componentNetwork9.SetMovingGroup(movableObjects6)
    
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Transform Origin")
    
    loaded3 = componentNetwork9.IsReferencedGeometryLoaded()
    
    componentNetwork9.BeginDrag()
    
    point173 = NXOpen.Point3d(40.393242532238872, 65.392490337762325, 26.399999999999999)
    direction170 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point173, direction170)
    
    point174 = NXOpen.Point3d(32.813928868564098, 65.392490337762325, 22.012913488294355)
    direction171 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point174, direction171)
    
    point175 = NXOpen.Point3d(31.425100688577039, 65.392490337762325, 21.417541864567816)
    direction172 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point175, direction172)
    
    point176 = NXOpen.Point3d(30.585383978952624, 65.392490337762325, 21.012034356180454)
    direction173 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point176, direction173)
    
    point177 = NXOpen.Point3d(30.036272508589985, 65.392490337762325, 20.822170240841274)
    direction174 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point177, direction174)
    
    point178 = NXOpen.Point3d(29.487161038227327, 65.392490337762325, 20.632306125502087)
    direction175 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point178, direction175)
    
    point179 = NXOpen.Point3d(29.228654807126475, 65.392490337762325, 20.658085403211061)
    direction176 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point179, direction176)
    
    point180 = NXOpen.Point3d(29.196555798965559, 65.392490337762325, 20.416662732453915)
    direction177 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point180, direction177)
    
    point181 = NXOpen.Point3d(28.938049567864685, 65.392490337762325, 20.442442010162889)
    direction178 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point181, direction178)
    
    point182 = NXOpen.Point3d(28.388938097502049, 65.392490337762325, 20.25257789482372)
    direction179 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point182, direction179)
    
    point183 = NXOpen.Point3d(27.839826627139384, 65.392490337762325, 20.062713779484525)
    direction180 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point183, direction180)
    
    point184 = NXOpen.Point3d(27.581320396038539, 65.392490337762325, 20.088493057193499)
    direction181 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point184, direction181)
    
    point185 = NXOpen.Point3d(27.290715156776756, 65.392490337762325, 19.872849664145331)
    direction182 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point185, direction182)
    
    point186 = NXOpen.Point3d(27.032208925675882, 65.392490337762325, 19.898628941854309)
    direction183 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point186, direction183)
    
    point187 = NXOpen.Point3d(26.483097455313253, 65.392490337762325, 19.708764826515132)
    direction184 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point187, direction184)
    
    point188 = NXOpen.Point3d(25.901886976789697, 65.392490337762325, 19.277478040418792)
    direction185 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point188, direction185)
    
    point189 = NXOpen.Point3d(25.062170267165261, 65.392490337762325, 18.871970532031447)
    direction186 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point189, direction186)
    
    point190 = NXOpen.Point3d(24.707367011581656, 65.392490337762325, 18.173481797469012)
    direction187 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point190, direction187)
    
    point191 = NXOpen.Point3d(25.484599870697846, 65.392490337762325, 16.138983320576017)
    direction188 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point191, direction188)
    
    point192 = NXOpen.Point3d(28.556289801560883, 65.392490337762325, 13.631048673545102)
    direction189 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point192, direction189)
    
    point193 = NXOpen.Point3d(32.499795450209277, 65.392490337762325, 11.770044205658671)
    direction190 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point193, direction190)
    
    point194 = NXOpen.Point3d(36.733906338119425, 65.392490337762325, 10.124683130820392)
    direction191 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point194, direction191)
    
    point195 = NXOpen.Point3d(39.933992301626134, 65.392490337762325, 8.5824391668180304)
    direction192 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point195, direction192)
    
    point196 = NXOpen.Point3d(41.098127424486819, 65.392490337762325, 7.4878520952445973)
    direction193 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point196, direction193)
    
    point197 = NXOpen.Point3d(41.001830400004081, 65.392490337762325, 6.7635840829731855)
    direction194 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point197, direction194)
    
    point198 = NXOpen.Point3d(40.873434367360439, 65.392490337762325, 5.7978933999446465)
    direction195 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point198, direction195)
    
    point199 = NXOpen.Point3d(40.422334087294111, 65.392490337762325, 4.375136653110796)
    direction196 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point199, direction196)
    
    point200 = NXOpen.Point3d(38.840911858341542, 65.392490337762325, 2.3312290048414339)
    direction197 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point200, direction197)
    
    point201 = NXOpen.Point3d(36.678279150865471, 65.392490337762325, -0.14396542952426838)
    direction198 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point201, direction198)
    
    point202 = NXOpen.Point3d(34.225041204127578, 65.392490337762325, -2.8348032569381156)
    direction199 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point202, direction199)
    
    point203 = NXOpen.Point3d(31.707605241067892, 65.392490337762325, -6.0084864258662378)
    direction200 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point203, direction200)
    
    point204 = NXOpen.Point3d(29.093872253525465, 65.392490337762325, -9.9064376070657651)
    direction201 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point204, direction201)
    
    point205 = NXOpen.Point3d(26.25373204304308, 65.392490337762325, -13.537186839799203)
    direction202 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point205, direction202)
    
    point206 = NXOpen.Point3d(23.80049409630519, 65.392490337762325, -16.228024667213049)
    direction203 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point206, direction203)
    
    point207 = NXOpen.Point3d(21.41145416588915, 65.392490337762325, -18.436017153112633)
    direction204 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point207, direction204)
    
    point208 = NXOpen.Point3d(19.571525705835736, 65.392490337762325, -20.45414552367302)
    direction205 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point208, direction205)
    
    point209 = NXOpen.Point3d(18.054301493205038, 65.392490337762325, -22.015207830428096)
    direction206 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point209, direction206)
    
    point210 = NXOpen.Point3d(17.118287759097871, 65.392490337762325, -23.144983351086868)
    direction207 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point210, direction207)
    
    point211 = NXOpen.Point3d(16.827682519836088, 65.392490337762325, -23.360626744135036)
    direction208 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point211, direction208)
    
    point212 = NXOpen.Point3d(16.827682519836088, 65.392490337762325, -23.360626744135036)
    direction209 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point212, direction209)
    
    point213 = NXOpen.Point3d(16.859781527996997, 65.392490337762325, -23.11920407337789)
    direction210 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point213, direction210)
    
    point214 = NXOpen.Point3d(16.891880536157913, 65.392490337762325, -22.877781402620744)
    direction211 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point214, direction211)
    
    point215 = NXOpen.Point3d(17.407178832546084, 65.392490337762325, -20.97217931427263)
    direction212 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point215, direction212)
    
    point216 = NXOpen.Point3d(17.952861971281589, 65.392490337762325, -16.867993911401271)
    direction213 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point216, direction213)
    
    point217 = NXOpen.Point3d(18.659040150821646, 65.392490337762325, -11.556695154744258)
    direction214 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point217, direction214)
    
    point218 = NXOpen.Point3d(19.49361436300536, 65.392490337762325, -5.279705715058669)
    direction215 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point218, direction215)
    
    point219 = NXOpen.Point3d(20.167693534384515, 65.392490337762325, -0.20982962915877901)
    direction216 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point219, direction216)
    
    point220 = NXOpen.Point3d(21.262488143482667, 65.392490337762325, 4.0842198890517496)
    direction217 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point220, direction217)
    
    point221 = NXOpen.Point3d(23.455505693306097, 65.392490337762325, 8.7579976379406421)
    direction218 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point221, direction218)
    
    point222 = NXOpen.Point3d(25.680622251290448, 65.392490337762325, 13.673198057586683)
    direction219 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point222, direction219)
    
    point223 = NXOpen.Point3d(27.809441784792053, 65.392490337762325, 17.86413046496131)
    direction220 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point223, direction220)
    
    point224 = NXOpen.Point3d(29.551359054549152, 65.392490337762325, 21.115151467016354)
    direction221 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point224, direction221)
    
    point225 = NXOpen.Point3d(30.389361598360018, 65.392490337762325, 23.477819619169786)
    direction222 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point225, direction222)
    
    point226 = NXOpen.Point3d(31.485870373271737, 65.392490337762325, 25.814708493614241)
    direction223 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point226, direction223)
    
    point227 = NXOpen.Point3d(32.001168669659883, 65.392490337762325, 27.720310581962362)
    direction224 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point227, direction224)
    
    point228 = NXOpen.Point3d(32.3880709334044, 65.392490337762325, 28.66022198728195)
    direction225 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point228, direction225)
    
    point229 = NXOpen.Point3d(32.710775180827099, 65.392490337762325, 29.11728805108724)
    direction226 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point229, direction226)
    
    point230 = NXOpen.Point3d(32.742874188988004, 65.392490337762325, 29.358710721844382)
    direction227 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point230, direction227)
    
    point231 = NXOpen.Point3d(32.807072205309829, 65.392490337762325, 29.841556063358649)
    direction228 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point231, direction228)
    
    point232 = NXOpen.Point3d(32.903369229792574, 65.392490337762325, 30.565824075630061)
    direction229 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point232, direction229)
    
    point233 = NXOpen.Point3d(32.22414756097271, 65.392490337762325, 31.36742992102841)
    direction230 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point233, direction230)
    
    point234 = NXOpen.Point3d(31.060012438112011, 65.392490337762325, 32.462016992601846)
    direction231 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point234, direction231)
    
    point235 = NXOpen.Point3d(29.637371084150459, 65.392490337762325, 33.582383341884224)
    direction232 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point235, direction232)
    
    point236 = NXOpen.Point3d(28.150531713867093, 65.392490337762325, 34.219904349652367)
    direction233 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point236, direction233)
    
    point237 = NXOpen.Point3d(26.178778889542905, 65.392490337762325, 35.150406583595583)
    direction234 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point237, direction234)
    
    point238 = NXOpen.Point3d(22.171075224572686, 65.392490337762325, 36.528565709967722)
    direction235 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point238, direction235)
    
    point239 = NXOpen.Point3d(17.419951874460804, 65.392490337762325, 38.225485340223948)
    direction236 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point239, direction236)
    
    point240 = NXOpen.Point3d(12.087618045825344, 65.392490337762325, 39.491118184383843)
    direction237 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point240, direction237)
    
    point241 = NXOpen.Point3d(8.0157163645333025, 65.392490337762325, 40.386431969241713)
    direction238 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point241, direction238)
    
    point242 = NXOpen.Point3d(5.7212592927864279, 65.392490337762325, 40.859868139379643)
    direction239 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point242, direction239)
    
    point243 = NXOpen.Point3d(5.2042468305846974, 65.392490337762325, 40.911426694797591)
    direction240 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point243, direction240)
    
    point244 = NXOpen.Point3d(5.2042468305846974, 65.392490337762325, 40.911426694797591)
    direction241 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point244, direction241)
    
    point245 = NXOpen.Point3d(4.9457405994838313, 65.392490337762325, 40.937205972506561)
    direction242 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point245, direction242)
    
    point246 = NXOpen.Point3d(4.6872343683829509, 65.392490337762325, 40.962985250215546)
    direction243 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point246, direction243)
    
    point247 = NXOpen.Point3d(4.6872343683829509, 65.392490337762325, 40.962985250215546)
    direction244 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point247, direction244)
    
    point248 = NXOpen.Point3d(4.6872343683829509, 65.392490337762325, 40.962985250215546)
    direction245 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    componentNetwork9.DragByRay(point248, direction245)
    
    componentNetwork9.EndDrag()
    
    componentNetwork9.ResetDisplay()
    
    componentNetwork9.ApplyToModel()
    
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Rotate About Y-axis")
    
    loaded4 = componentNetwork9.IsReferencedGeometryLoaded()
    
    componentNetwork9.BeginDrag()
    
    translation12 = NXOpen.Vector3d(-36.659914818593471, 14.514585381795392, 0.0)
    rotation1 = NXOpen.Matrix3x3()
    
    rotation1.Xx = 0.81915204428899202
    rotation1.Xy = 0.57357643635104572
    rotation1.Xz = 0.0
    rotation1.Yx = -0.57357643635104572
    rotation1.Yy = 0.81915204428899202
    rotation1.Yz = 0.0
    rotation1.Zx = 0.0
    rotation1.Zy = 0.0
    rotation1.Zz = 1.0
    componentNetwork9.DragByTransform(translation12, rotation1)
    
    translation13 = NXOpen.Vector3d(-40.936878028773435, 18.311832668501481, 0.0)
    rotation2 = NXOpen.Matrix3x3()
    
    rotation2.Xx = 0.76604444311897835
    rotation2.Xy = 0.64278760968653892
    rotation2.Xz = 0.0
    rotation2.Yx = -0.64278760968653892
    rotation2.Yy = 0.76604444311897835
    rotation2.Yz = 0.0
    rotation2.Zx = 0.0
    rotation2.Zy = 0.0
    rotation2.Zz = 1.0
    componentNetwork9.DragByTransform(translation13, rotation2)
    
    translation14 = NXOpen.Vector3d(-44.866614195018784, 22.467392188148992, 0.0)
    rotation3 = NXOpen.Matrix3x3()
    
    rotation3.Xx = 0.70710678118654802
    rotation3.Xy = 0.70710678118654713
    rotation3.Xz = 0.0
    rotation3.Yx = -0.70710678118654713
    rotation3.Yy = 0.70710678118654802
    rotation3.Yz = 0.0
    rotation3.Zx = 0.0
    rotation3.Zy = 0.0
    rotation3.Zz = 1.0
    componentNetwork9.DragByTransform(translation14, rotation3)
    
    translation15 = NXOpen.Vector3d(-48.419215652264789, 26.949637623597972, 0.0)
    rotation4 = NXOpen.Matrix3x3()
    
    rotation4.Xx = 0.64278760968653992
    rotation4.Xy = 0.76604444311897757
    rotation4.Xz = 0.0
    rotation4.Yx = -0.76604444311897757
    rotation4.Yy = 0.64278760968653992
    rotation4.Yz = 0.0
    rotation4.Zx = 0.0
    rotation4.Zy = 0.0
    rotation4.Zz = 1.0
    componentNetwork9.DragByTransform(translation15, rotation4)
    
    translation16 = NXOpen.Vector3d(-51.567644958302417, 31.724456380630862, 0.0)
    rotation5 = NXOpen.Matrix3x3()
    
    rotation5.Xx = 0.57357643635104683
    rotation5.Xy = 0.81915204428899135
    rotation5.Xz = 0.0
    rotation5.Yx = -0.81915204428899135
    rotation5.Yy = 0.57357643635104683
    rotation5.Yz = 0.0
    rotation5.Zx = 0.0
    rotation5.Zy = 0.0
    rotation5.Zz = 1.0
    componentNetwork9.DragByTransform(translation16, rotation5)
    
    translation17 = NXOpen.Vector3d(-54.287940665039123, 36.755509205392244, 0.0)
    rotation6 = NXOpen.Matrix3x3()
    
    rotation6.Xx = 0.50000000000000089
    rotation6.Xy = 0.86602540378443826
    rotation6.Xz = 0.0
    rotation6.Yx = -0.86602540378443826
    rotation6.Yy = 0.50000000000000089
    rotation6.Yz = 0.0
    rotation6.Zx = 0.0
    rotation6.Zy = 0.0
    rotation6.Zz = 1.0
    componentNetwork9.DragByTransform(translation17, rotation6)
    
    translation18 = NXOpen.Vector3d(-56.559399679587187, 42.00450674805294, 0.0)
    rotation7 = NXOpen.Matrix3x3()
    
    rotation7.Xx = 0.42261826174070044
    rotation7.Xy = 0.9063077870366496
    rotation7.Xz = 0.0
    rotation7.Yx = -0.9063077870366496
    rotation7.Yy = 0.42261826174070044
    rotation7.Yz = 0.0
    rotation7.Zx = 0.0
    rotation7.Zy = 0.0
    rotation7.Zz = 1.0
    componentNetwork9.DragByTransform(translation18, rotation7)
    
    translation19 = NXOpen.Vector3d(-58.36473482730144, 47.431500967881931, 0.0)
    rotation8 = NXOpen.Matrix3x3()
    
    rotation8.Xx = 0.34202014332566988
    rotation8.Xy = 0.93969262078590809
    rotation8.Xz = 0.0
    rotation8.Yx = -0.93969262078590809
    rotation8.Yy = 0.34202014332566988
    rotation8.Yz = 0.0
    rotation8.Zx = 0.0
    rotation8.Zy = 0.0
    rotation8.Zz = 1.0
    componentNetwork9.DragByTransform(translation19, rotation8)
    
    translation20 = NXOpen.Vector3d(-59.690206417616615, 52.995189161957612, 0.0)
    rotation9 = NXOpen.Matrix3x3()
    
    rotation9.Xx = 0.25881904510252196
    rotation9.Xy = 0.96592582628906809
    rotation9.Xz = 0.0
    rotation9.Yx = -0.96592582628906809
    rotation9.Yy = 0.25881904510252196
    rotation9.Yz = 0.0
    rotation9.Zx = 0.0
    rotation9.Zy = 0.0
    rotation9.Zz = 1.0
    componentNetwork9.DragByTransform(translation20, rotation9)
    
    translation21 = NXOpen.Vector3d(-60.5257268113888, 58.653228303676272, 0.0)
    rotation10 = NXOpen.Matrix3x3()
    
    rotation10.Xx = 0.17364817766693166
    rotation10.Xy = 0.98480775301220802
    rotation10.Xz = 0.0
    rotation10.Yx = -0.98480775301220802
    rotation10.Yy = 0.17364817766693166
    rotation10.Yz = 0.0
    rotation10.Zx = 0.0
    rotation10.Zy = 0.0
    rotation10.Zz = 1.0
    componentNetwork9.DragByTransform(translation21, rotation10)
    
    translation22 = NXOpen.Vector3d(-60.864937193920348, 64.362557298752009, 0.0)
    rotation11 = NXOpen.Matrix3x3()
    
    rotation11.Xx = 0.087155742747659554
    rotation11.Xy = 0.99619469809174555
    rotation11.Xz = 0.0
    rotation11.Yx = -0.99619469809174555
    rotation11.Yy = 0.087155742747659554
    rotation11.Yz = 0.0
    rotation11.Zx = 0.0
    rotation11.Zy = 0.0
    rotation11.Zz = 1.0
    componentNetwork9.DragByTransform(translation22, rotation11)
    
    translation23 = NXOpen.Vector3d(-60.705255969379387, 70.079724706145186, 0.0)
    rotation12 = NXOpen.Matrix3x3()
    
    rotation12.Xx = 1.457167719820518e-15
    rotation12.Xy = 1.0000000000000002
    rotation12.Xz = 0.0
    rotation12.Yx = -1.0000000000000002
    rotation12.Yy = 1.457167719820518e-15
    rotation12.Yz = 0.0
    rotation12.Zx = 0.0
    rotation12.Zy = 0.0
    rotation12.Zz = 1.0
    componentNetwork9.DragByTransform(translation23, rotation12)
    
    translation24 = NXOpen.Vector3d(-60.047898408302835, 75.761219429765475, 0.0)
    rotation13 = NXOpen.Matrix3x3()
    
    rotation13.Xx = -0.087155742747656653
    rotation13.Xy = 0.99619469809174588
    rotation13.Xz = 0.0
    rotation13.Yx = -0.99619469809174588
    rotation13.Yy = -0.087155742747656653
    rotation13.Yz = 0.0
    rotation13.Zx = 0.0
    rotation13.Zy = 0.0
    rotation13.Zz = 1.0
    componentNetwork9.DragByTransform(translation24, rotation13)
    
    translation25 = NXOpen.Vector3d(-58.89786739865383, 81.363801864185817, 0.0)
    rotation14 = NXOpen.Matrix3x3()
    
    rotation14.Xx = -0.1736481776669288
    rotation14.Xy = 0.98480775301220858
    rotation14.Xz = 0.0
    rotation14.Yx = -0.98480775301220858
    rotation14.Yy = -0.1736481776669288
    rotation14.Yz = 0.0
    rotation14.Zx = 0.0
    rotation14.Zy = 0.0
    rotation14.Zz = 1.0
    componentNetwork9.DragByTransform(translation25, rotation14)
    
    translation26 = NXOpen.Vector3d(-57.263915370823497, 86.844832974148503, 0.0)
    rotation15 = NXOpen.Matrix3x3()
    
    rotation15.Xx = -0.25881904510251919
    rotation15.Xy = 0.96592582628906898
    rotation15.Xz = 0.0
    rotation15.Yx = -0.96592582628906898
    rotation15.Yy = -0.25881904510251919
    rotation15.Yz = 0.0
    rotation15.Zx = 0.0
    rotation15.Zy = 0.0
    rotation15.Zz = 1.0
    componentNetwork9.DragByTransform(translation26, rotation15)
    
    translation27 = NXOpen.Vector3d(-55.158477686350849, 92.162598803369661, 0.0)
    rotation16 = NXOpen.Matrix3x3()
    
    rotation16.Xx = -0.34202014332566716
    rotation16.Xy = 0.93969262078590932
    rotation16.Xz = 0.0
    rotation16.Yx = -0.93969262078590932
    rotation16.Yy = -0.34202014332566716
    rotation16.Yz = 0.0
    rotation16.Zx = 0.0
    rotation16.Zy = 0.0
    rotation16.Zz = 1.0
    componentNetwork9.DragByTransform(translation27, rotation16)
    
    translation28 = NXOpen.Vector3d(-55.158477686350849, 92.162598803369661, 0.0)
    rotation17 = NXOpen.Matrix3x3()
    
    rotation17.Xx = -0.34202014332566716
    rotation17.Xy = 0.93969262078590932
    rotation17.Xz = 0.0
    rotation17.Yx = -0.93969262078590932
    rotation17.Yy = -0.34202014332566716
    rotation17.Yz = 0.0
    rotation17.Zx = 0.0
    rotation17.Zy = 0.0
    rotation17.Zz = 1.0
    componentNetwork9.DragByTransform(translation28, rotation17)
    
    componentNetwork9.EndDrag()
    
    componentNetwork9.ResetDisplay()
    
    componentNetwork9.ApplyToModel()
    
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Translate Along X-axis")
    
    loaded5 = componentNetwork9.IsReferencedGeometryLoaded()
    
    componentNetwork9.BeginDrag()
    
    translation29 = NXOpen.Vector3d(-2.8190778623577262, 1.026060429977008, 0.0)
    componentNetwork9.DragByTranslation(translation29)
    
    translation30 = NXOpen.Vector3d(-3.7587704831436355, 1.3680805733026631, 0.0)
    componentNetwork9.DragByTranslation(translation30)
    
    translation31 = NXOpen.Vector3d(-4.6984631039295444, 1.7101007166283324, 0.0)
    componentNetwork9.DragByTranslation(translation31)
    
    translation32 = NXOpen.Vector3d(-5.6381557247154541, 2.0521208599540017, 0.0)
    componentNetwork9.DragByTranslation(translation32)
    
    componentNetwork9.EndDrag()
    
    componentNetwork9.ResetDisplay()
    
    componentNetwork9.ApplyToModel()
    
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Transform Origin")
    
    loaded6 = componentNetwork9.IsReferencedGeometryLoaded()
    
    componentNetwork9.BeginDrag()
    
    translation33 = NXOpen.Vector3d(22.060124317840781, -8.029228615906014, 9.6407886430497669)
    componentNetwork9.DragByTranslation(translation33)
    
    componentNetwork9.EndDrag()
    
    componentNetwork9.ResetDisplay()
    
    componentNetwork9.ApplyToModel()
    
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Rotate About Z-axis")
    
    loaded7 = componentNetwork9.IsReferencedGeometryLoaded()
    
    componentNetwork9.BeginDrag()
    
    translation34 = NXOpen.Vector3d(-12.322893789154978, 4.4851665392762428, 1.5987298505488354)
    rotation18 = NXOpen.Matrix3x3()
    
    rotation18.Xx = 0.96991174743196917
    rotation18.Xy = 0.010951228335846774
    rotation18.Xz = 0.24321034680169401
    rotation18.Yx = 0.010951228335846774
    rotation18.Yy = 0.99601407885709925
    rotation18.Yz = -0.088521326901376401
    rotation18.Zx = -0.24321034680169384
    rotation18.Zy = 0.088521326901376346
    rotation18.Zz = 0.96592582628906831
    componentNetwork9.DragByTransform(translation34, rotation18)
    
    translation35 = NXOpen.Vector3d(-16.291229981690133, 5.9295227929203023, 2.8858685792400962)
    rotation19 = NXOpen.Matrix3x3()
    
    rotation19.Xx = 0.94674724402994226
    rotation19.Xy = 0.019382418065742701
    rotation19.Xz = 0.32139380484326974
    rotation19.Yx = 0.019382418065742701
    rotation19.Yy = 0.99294537675596617
    rotation19.Yz = -0.11697777844051037
    rotation19.Zx = -0.32139380484326951
    rotation19.Zy = 0.11697777844051029
    rotation19.Zz = 0.93969262078590843
    componentNetwork9.DragByTransform(translation35, rotation19)
    
    translation36 = NXOpen.Vector3d(-20.139049299207098, 7.3300144913309637, 4.536169380230092)
    rotation20 = NXOpen.Matrix3x3()
    
    rotation20.Xx = 0.91726769396627783
    rotation20.Xy = 0.030112096808476818
    rotation20.Xz = 0.39713126196710297
    rotation20.Yx = 0.030112096808476818
    rotation20.Yy = 0.98904009307037222
    rotation20.Yz = -0.14454395845259826
    rotation20.Zx = -0.39713126196710263
    rotation20.Zy = 0.14454395845259813
    rotation20.Zz = 0.90630778703665016
    componentNetwork9.DragByTransform(translation36, rotation20)
    
    translation37 = NXOpen.Vector3d(-23.837067513322733, 8.6759830470433101, 6.5370724679444123)
    rotation21 = NXOpen.Matrix3x3()
    
    rotation21.Xx = 0.88169745441719949
    rotation21.Xy = 0.043058605230059721
    rotation21.Xz = 0.46984631039295432
    rotation21.Yx = 0.043058605230059721
    rotation21.Yy = 0.98432794936723933
    rotation21.Yz = -0.1710100716628335
    rotation21.Zx = -0.46984631039295394
    rotation21.Zy = 0.17101007166283333
    rotation21.Zz = 0.86602540378443893
    componentNetwork9.DragByTransform(translation37, rotation21)
    
    translation38 = NXOpen.Vector3d(-27.357140472503172, 9.957184826630332, 8.8733497617072388)
    rotation22 = NXOpen.Matrix3x3()
    
    rotation22.Xx = 0.84030723638357352
    rotation22.Xy = 0.058123412584087708
    rotation22.Xz = 0.53898554469575644
    rotation22.Yx = 0.058123412584087708
    rotation22.Yy = 0.97884480790541861
    rotation22.Yz = -0.19617469496901008
    rotation22.Zx = -0.5389855446957561
    rotation22.Zy = 0.19617469496900994
    rotation22.Zz = 0.81915204428899213
    componentNetwork9.DragByTransform(translation38, rotation22)
    
    translation39 = NXOpen.Vector3d(-30.672478296050894, 11.163869110938585, 11.527220780630252)
    rotation23 = NXOpen.Matrix3x3()
    
    rotation23.Xx = 0.79341204441673263
    rotation23.Xy = 0.075191866590217232
    rotation23.Xz = 0.60402277355505396
    rotation23.Yx = 0.075191866590217177
    rotation23.Yy = 0.97263239870224583
    rotation23.Yz = -0.21984631039295305
    rotation23.Zx = -0.60402277355505352
    rotation23.Zy = 0.21984631039295291
    rotation23.Zz = 0.76604444311897846
    componentNetwork9.DragByTransform(translation39, rotation23)
    
    translation40 = NXOpen.Vector3d(-33.75784926127298, 12.286852303948606, 14.478487963808284)
    rotation24 = NXOpen.Matrix3x3()
    
    rotation24.Xx = 0.74136877924363564
    rotation24.Xy = 0.094134066007247275
    rotation24.Xz = 0.66446302438867499
    rotation24.Yx = 0.094134066007247247
    rotation24.Yy = 0.96573800194291226
    rotation24.Yz = -0.241844762647974
    rotation24.Zx = -0.66446302438867455
    rotation24.Zy = 0.24184476264797386
    rotation24.Zz = 0.70710678118654813
    componentNetwork9.DragByTransform(translation40, rotation24)
    
    translation41 = NXOpen.Vector3d(-36.589771832126175, 13.317587825485781, 17.704690385953519)
    rotation25 = NXOpen.Matrix3x3()
    
    rotation25.Xx = 0.68457352153683271
    rotation25.Xy = 0.11480584926000156
    rotation25.Xz = 0.71984631039295455
    rotation25.Yx = 0.11480584926000154
    rotation25.Yy = 0.95821408814970721
    rotation25.Yz = -0.26200263022938358
    rotation25.Zx = -0.71984631039295399
    rotation25.Zy = 0.26200263022938342
    rotation25.Zz = 0.64278760968654003
    componentNetwork9.DragByTransform(translation41, rotation25)
    
    translation42 = NXOpen.Vector3d(-39.14669336788468, 14.248231155856097, 21.18127469859915)
    rotation26 = NXOpen.Matrix3x3()
    
    rotation26.Xx = 0.62345851750138659
    rotation26.Xy = 0.13704989159596268
    rotation26.Xz = 0.76975113132005768
    rotation26.Yx = 0.13704989159596262
    rotation26.Yy = 0.95011791884966013
    rotation26.Yz = -0.28016649959323409
    rotation26.Zx = -0.76975113132005701
    rotation26.Zy = 0.28016649959323392
    rotation26.Zz = 0.57357643635104694
    componentNetwork9.DragByTransform(translation42, rotation26)
    
    translation43 = NXOpen.Vector3d(-41.409154151749931, 15.071699537377626, 24.881781995906938)
    rotation27 = NXOpen.Matrix3x3()
    
    rotation27.Xx = 0.55848888922025564
    rotation27.Xy = 0.16069690242163387
    rotation27.Xz = 0.81379768134937425
    rotation27.Yx = 0.16069690242163384
    rotation27.Yy = 0.94151111077974525
    rotation27.Yz = -0.29619813272602236
    rotation27.Zx = -0.81379768134937358
    rotation27.Zy = 0.29619813272602213
    rotation27.Zz = 0.500000000000001
    componentNetwork9.DragByTransform(translation43, rotation27)
    
    translation44 = NXOpen.Vector3d(-43.359935491045562, 15.781725878443183, 28.77804918291697)
    rotation28 = NXOpen.Matrix3x3()
    
    rotation28.Xx = 0.49015909479439312
    rotation28.Xy = 0.18556691370617637
    rotation28.Xz = 0.85165073963914717
    rotation28.Yx = 0.18556691370617631
    rotation28.Yy = 0.93245916694630726
    rotation28.Yz = -0.30997551921944316
    rotation28.Zx = -0.8516507396391465
    rotation28.Zy = 0.30997551921944294
    rotation28.Zz = 0.42261826174070055
    componentNetwork9.DragByTransform(translation44, rotation28)
    
    translation45 = NXOpen.Vector3d(-44.984190761865534, 16.372906449871643, 32.840423313705656)
    rotation29 = NXOpen.Matrix3x3()
    
    rotation29.Xx = 0.41898916521803792
    rotation29.Xy = 0.21147064964679135
    rotation29.Xz = 0.88302222155948973
    rotation29.Yx = 0.2114706496467913
    rotation29.Yy = 0.92303097810763179
    rotation29.Yz = -0.32139380484326813
    rotation29.Zx = -0.88302222155948906
    rotation29.Zy = 0.32139380484326791
    rotation29.Zz = 0.34202014332566993
    componentNetwork9.DragByTransform(translation45, rotation29)
    
    translation46 = NXOpen.Vector3d(-46.269558400846762, 16.840742010549839, 37.037987268209129)
    rotation30 = NXOpen.Matrix3x3()
    
    rotation30.Xx = 0.34552074662884458
    rotation30.Xy = 0.23821096717186735
    rotation30.Xz = 0.90767337119036939
    rotation30.Yx = 0.23821096717186729
    rotation30.Yy = 0.91329829847367727
    rotation30.Yz = -0.33036608954935059
    rotation30.Zx = -0.90767337119036884
    rotation30.Zy = 0.33036608954935037
    rotation30.Zz = 0.25881904510252202
    componentNetwork9.DragByTransform(translation46, rotation30)
    
    translation47 = NXOpen.Vector3d(-47.206255984130422, 17.181672049374171, 41.338795050175193)
    rotation31 = NXOpen.Matrix3x3()
    
    rotation31.Xx = 0.27031297805372079
    rotation31.Xy = 0.26558435631879329
    rotation31.Xz = 0.92541657839832414
    rotation31.Yx = 0.26558435631879329
    rotation31.Yy = 0.90333519961321085
    rotation31.Yz = -0.33682408883346365
    rotation31.Zx = -0.9254165783983237
    rotation31.Zy = 0.33682408883346343
    rotation31.Zz = 0.17364817766693169
    componentNetwork9.DragByTransform(translation47, rotation31)
    
    translation48 = NXOpen.Vector3d(-47.787154677514224, 17.393101882890001, 45.710114915484361)
    rotation32 = NXOpen.Matrix3x3()
    
    rotation32.Xx = 0.19393823602321547
    rotation32.Xy = 0.29338248906765696
    rotation32.Xz = 0.93611680666286001
    rotation32.Yx = 0.2933824890676569
    rotation32.Yy = 0.893217506724444
    rotation32.Yz = -0.34071865342160862
    rotation32.Zx = -0.93611680666285946
    rotation32.Zy = 0.34071865342160834
    rotation32.Zz = 0.087155742747659568
    componentNetwork9.DragByTransform(translation48, rotation32)
    
    translation49 = NXOpen.Vector3d(-48.007833491185323, 17.473422402399464, 50.118678480486516)
    rotation33 = NXOpen.Matrix3x3()
    
    rotation33.Xx = 0.11697777844051101
    rotation33.Xy = 0.32139380484326785
    rotation33.Xz = 0.93969262078590932
    rotation33.Yx = 0.32139380484326779
    rotation33.Yy = 0.88302222155949039
    rotation33.Yz = -0.34202014332566727
    rotation33.Zx = -0.93969262078590887
    rotation33.Zy = 0.34202014332566699
    rotation33.Zz = 1.457167719820518e-15
    componentNetwork9.DragByTransform(translation49, rotation33)
    
    translation50 = NXOpen.Vector3d(-48.007833491185323, 17.473422402399464, 50.118678480486516)
    rotation34 = NXOpen.Matrix3x3()
    
    rotation34.Xx = 0.11697777844051101
    rotation34.Xy = 0.32139380484326785
    rotation34.Xz = 0.93969262078590932
    rotation34.Yx = 0.32139380484326779
    rotation34.Yy = 0.88302222155949039
    rotation34.Yz = -0.34202014332566727
    rotation34.Zx = -0.93969262078590887
    rotation34.Zy = 0.34202014332566699
    rotation34.Zz = 1.457167719820518e-15
    componentNetwork9.DragByTransform(translation50, rotation34)
    
    componentNetwork9.EndDrag()
    
    componentNetwork9.ResetDisplay()
    
    componentNetwork9.ApplyToModel()
    
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    theSession.DeleteUndoMark(markId50, None)
    
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork9.Solve()
    
    componentPositioner9.ClearNetwork()
    
    nErrs20 = theSession.UpdateManager.AddToDeleteList(componentNetwork9)
    
    nErrs21 = theSession.UpdateManager.DoUpdate(markId43)
    
    componentPositioner9.EndAssemblyConstraints()
    
    logicalobjects4 = addComponentBuilder4.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder4.ComponentName = "Y_LINK"
    
    nXObject5 = addComponentBuilder4.Commit()
    
    errorList4 = addComponentBuilder4.GetOperationFailures()
    
    errorList4.Dispose()
    theSession.DeleteUndoMark(markId51, None)
    
    theSession.SetUndoMarkName(markId42, "Add Component")
    
    addComponentBuilder4.Destroy()
    
    componentPositioner9.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId43, None)
    
    theSession.DeleteUndoMark(markId49, None)
    
    theSession.DeleteUndoMark(markId48, None)
    
    theSession.DeleteUndoMark(markId47, None)
    
    theSession.DeleteUndoMark(markId46, None)
    
    theSession.DeleteUndoMark(markId45, None)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner10 = workPart.ComponentAssembly.Positioner
    
    componentPositioner10.ClearNetwork()
    
    componentPositioner10.PrimaryArrangement = arrangement1
    
    componentPositioner10.BeginAssemblyConstraints()
    
    allowInterpartPositioning9 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression89 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression90 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression91 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression92 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression93 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression94 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression95 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression96 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network10 = componentPositioner10.EstablishNetwork()
    
    componentNetwork10 = network10
    componentNetwork10.MoveObjectsState = True
    
    componentNetwork10.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork10.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId54, "Assembly Constraints Dialog")
    
    componentNetwork10.MoveObjectsState = True
    
    componentNetwork10.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    scaleAboutPoint38 = NXOpen.Point3d(-50.930575526266402, 25.222761213008219, 0.0)
    viewCenter38 = NXOpen.Point3d(50.930575526266509, -25.222761213008095, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint38, viewCenter38)
    
    scaleAboutPoint39 = NXOpen.Point3d(-40.938481661113187, 19.014081529806198, 0.0)
    viewCenter39 = NXOpen.Point3d(40.938481661113286, -19.014081529806084, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint39, viewCenter39)
    
    scaleAboutPoint40 = NXOpen.Point3d(-32.750785328890551, 14.435180263444746, 0.0)
    viewCenter40 = NXOpen.Point3d(32.750785328890629, -14.4351802634446, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint40, viewCenter40)
    
    scaleAboutPoint41 = NXOpen.Point3d(-26.200628263112424, 10.803102648771569, 0.0)
    viewCenter41 = NXOpen.Point3d(26.200628263112531, -10.80310264877142, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint41, viewCenter41)
    
    component8 = nXObject5
    face3 = component8.FindObject("PROTO#.Features|SIMPLE HOLE(4:1A)|FACE 3 {(3,1.4,1.5) EXTRUDE(2)}")
    line4 = workPart.Lines.CreateFaceAxis(face3, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects4 = [NXOpen.TaggedObject.Null] * 1 
    objects4[0] = line4
    nErrs22 = theSession.UpdateManager.AddObjectsToDeleteList(objects4)
    
    rotMatrix12 = NXOpen.Matrix3x3()
    
    rotMatrix12.Xx = 0.98720374752753726
    rotMatrix12.Xy = -0.13045802454393168
    rotMatrix12.Xz = -0.091703133532464259
    rotMatrix12.Yx = 0.10198487527177169
    rotMatrix12.Yy = 0.074434619807106639
    rotMatrix12.Yz = 0.99199726440649483
    rotMatrix12.Zx = -0.12258811558784841
    rotMatrix12.Zy = -0.98865574959449676
    rotMatrix12.Zz = 0.086786880980677772
    translation51 = NXOpen.Point3d(-45.342956880426669, -53.621860405678397, 83.618601971516952)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix12, translation51, 2.6634420161944918)
    
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint5 = componentPositioner10.CreateConstraint(True)
    
    componentConstraint5 = constraint5
    componentConstraint5.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge7 = component8.FindObject("PROTO#.Features|EXTRUDE(10)|EDGE * 140 EXTRUDE(12) 140 {(4.2990381056767,-0.5,47.75)(3,-0.5,45.5)(1.7009618943233,-0.5,47.75) EXTRUDE(2)}")
    constraintReference8 = componentConstraint5.CreateConstraintReference(component8, edge7, False, False, False)
    
    helpPoint7 = NXOpen.Point3d(11.380704174082448, 38.241780198475965, 51.470822854981016)
    constraintReference8.HelpPoint = helpPoint7
    
    edge8 = component4.FindObject("PROTO#.Features|EXTRUDE(4)|EDGE * 160 EXTRUDE(2) 120 {(2.25,1.7009618943233,0)(4.5,3,0)(2.25,4.2990381056767,0) EXTRUDE(2)}")
    constraintReference9 = componentConstraint5.CreateConstraintReference(component4, edge8, False, False, False)
    
    helpPoint8 = NXOpen.Point3d(67.093242532238861, -6.9712611322590519, 21.624645441842485)
    constraintReference9.HelpPoint = helpPoint8
    
    constraintReference9.SetFixHint(True)
    
    componentNetwork10.Solve()
    
    rotMatrix13 = NXOpen.Matrix3x3()
    
    rotMatrix13.Xx = 0.98212595800194147
    rotMatrix13.Xy = 0.13407886629619659
    rotMatrix13.Xz = -0.13210397507832081
    rotMatrix13.Yx = 0.10212675472360616
    rotMatrix13.Yy = 0.20996176093594068
    rotMatrix13.Yz = 0.97236113914239841
    rotMatrix13.Zx = 0.15810986240077299
    rotMatrix13.Zy = -0.96847246556492439
    rotMatrix13.Zz = 0.19251585611113459
    translation52 = NXOpen.Point3d(-58.101804819907088, -60.375383715886308, 60.418198893952074)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix13, translation52, 2.6634420161944918)
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    theSession.DeleteUndoMark(markId57, None)
    
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs23 = theSession.UpdateManager.DoUpdate(markId55)
    
    componentNetwork10.Solve()
    
    componentPositioner10.ClearNetwork()
    
    nErrs24 = theSession.UpdateManager.AddToDeleteList(componentNetwork10)
    
    componentPositioner10.DeleteNonPersistentConstraints()
    
    nErrs25 = theSession.UpdateManager.DoUpdate(markId55)
    
    theSession.DeleteUndoMark(markId58, None)
    
    theSession.SetUndoMarkName(markId54, "Assembly Constraints")
    
    componentPositioner10.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner10.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId55, None)
    
    theSession.DeleteUndoMark(markId56, None)
    
    theSession.DeleteUndoMark(markId53, None)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Move Component...
    # ----------------------------------------------
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner11 = workPart.ComponentAssembly.Positioner
    
    componentPositioner11.ClearNetwork()
    
    componentPositioner11.PrimaryArrangement = arrangement1
    
    componentPositioner11.BeginMoveComponent()
    
    allowInterpartPositioning10 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression97 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression98 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression99 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression100 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression101 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression102 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression103 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression104 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network11 = componentPositioner11.EstablishNetwork()
    
    componentNetwork11 = network11
    componentNetwork11.MoveObjectsState = True
    
    componentNetwork11.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork11.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    expression105 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression106 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression107 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression108 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression109 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    componentNetwork11.RemoveAllConstraints()
    
    movableObjects7 = []
    componentNetwork11.SetMovingGroup(movableObjects7)
    
    componentNetwork11.Solve()
    
    theSession.SetUndoMarkName(markId59, "Move Component Dialog")
    
    componentNetwork11.MoveObjectsState = True
    
    componentNetwork11.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId60 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component Update")
    
    componentNetwork11.RemoveAllConstraints()
    
    movableObjects8 = [NXOpen.NXObject.Null] * 1 
    movableObjects8[0] = component8
    componentNetwork11.SetMovingGroup(movableObjects8)
    
    componentNetwork11.Solve()
    
    markId61 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Rotate About X-axis")
    
    loaded8 = componentNetwork11.IsReferencedGeometryLoaded()
    
    componentNetwork11.BeginDrag()
    
    translation53 = NXOpen.Vector3d(54.692079943446522, -53.064388394260213, 1.7763568394002505e-14)
    rotation35 = NXOpen.Matrix3x3()
    
    rotation35.Xx = 0.42261826174070022
    rotation35.Xy = -0.90630778703664927
    rotation35.Xz = 3.6223648659104477e-16
    rotation35.Yx = 0.90630778703664994
    rotation35.Yy = 0.42261826174070022
    rotation35.Yz = 1.3579182359182838e-16
    rotation35.Zx = -3.2172203079250096e-16
    rotation35.Zy = 1.9938678052356684e-16
    rotation35.Zz = 1.0
    componentNetwork11.DragByTransform(translation53, rotation35)
    
    translation54 = NXOpen.Vector3d(3.8946884556135757, -11.731512075099538, 3.5527136788005009e-15)
    rotation36 = NXOpen.Matrix3x3()
    
    rotation36.Xx = 0.98480775301220813
    rotation36.Xy = -0.17364817766693011
    rotation36.Xz = 6.2290427340821237e-17
    rotation36.Yx = 0.17364817766693028
    rotation36.Yy = 0.98480775301220813
    rotation36.Yz = -7.5936303674375339e-18
    rotation36.Zx = -6.1224398441252842e-17
    rotation36.Zy = 4.5911357108845039e-18
    rotation36.Zz = 1.0
    componentNetwork11.DragByTransform(translation54, rotation36)
    
    translation55 = NXOpen.Vector3d(1.6912397883360768, -5.9507789227032575, 3.5527136788005009e-15)
    rotation37 = NXOpen.Matrix3x3()
    
    rotation37.Xx = 0.99619469809174555
    rotation37.Xy = -0.087155742747658055
    rotation37.Xz = 3.0979441139440111e-17
    rotation37.Yx = 0.087155742747658138
    rotation37.Yy = 0.99619469809174555
    rotation37.Yz = -5.1566445796559415e-18
    rotation37.Zx = -3.0712425877705507e-17
    rotation37.Zy = 9.5901037296653402e-19
    rotation37.Zz = 1.0
    componentNetwork11.DragByTransform(translation55, rotation37)
    
    translation56 = NXOpen.Vector3d(1.6912397883360768, -5.9507789227032575, 3.5527136788005009e-15)
    rotation38 = NXOpen.Matrix3x3()
    
    rotation38.Xx = 0.99619469809174555
    rotation38.Xy = -0.087155742747658055
    rotation38.Xz = 3.0979441139440111e-17
    rotation38.Yx = 0.087155742747658138
    rotation38.Yy = 0.99619469809174555
    rotation38.Yz = -5.1566445796559415e-18
    rotation38.Zx = -3.0712425877705507e-17
    rotation38.Zy = 9.5901037296653402e-19
    rotation38.Zz = 1.0
    componentNetwork11.DragByTransform(translation56, rotation38)
    
    translation57 = NXOpen.Vector3d(1.6912397883360768, -5.9507789227032575, 3.5527136788005009e-15)
    rotation39 = NXOpen.Matrix3x3()
    
    rotation39.Xx = 0.99619469809174555
    rotation39.Xy = -0.087155742747658055
    rotation39.Xz = 3.0979441139440111e-17
    rotation39.Yx = 0.087155742747658138
    rotation39.Yy = 0.99619469809174555
    rotation39.Yz = -5.1566445796559415e-18
    rotation39.Zx = -3.0712425877705507e-17
    rotation39.Zy = 9.5901037296653402e-19
    rotation39.Zz = 1.0
    componentNetwork11.DragByTransform(translation57, rotation39)
    
    translation58 = NXOpen.Vector3d(0.0, 0.0, 0.0)
    rotation40 = NXOpen.Matrix3x3()
    
    rotation40.Xx = 1.0
    rotation40.Xy = 0.0
    rotation40.Xz = 2.5165938909012688e-33
    rotation40.Yx = 0.0
    rotation40.Yy = 1.0
    rotation40.Yz = 0.0
    rotation40.Zx = 2.0547795763658576e-34
    rotation40.Zy = 0.0
    rotation40.Zz = 1.0
    componentNetwork11.DragByTransform(translation58, rotation40)
    
    componentNetwork11.EndDrag()
    
    componentNetwork11.ResetDisplay()
    
    componentNetwork11.ApplyToModel()
    
    markId62 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Rotate About Y-axis")
    
    loaded9 = componentNetwork11.IsReferencedGeometryLoaded()
    
    componentNetwork11.BeginDrag()
    
    translation59 = NXOpen.Vector3d(0.0, -1.7678922229374905, 1.508611010944815)
    rotation41 = NXOpen.Matrix3x3()
    
    rotation41.Xx = 1.0
    rotation41.Xy = 2.5863262713832379e-18
    rotation41.Xz = -2.0832263015998274e-16
    rotation41.Yx = 8.7019812240056148e-18
    rotation41.Yy = 0.99619469809174555
    rotation41.Yz = 0.087155742747658138
    rotation41.Zx = 2.0805561489824794e-16
    rotation41.Zy = -0.087155742747658055
    rotation41.Zz = 0.99619469809174555
    componentNetwork11.DragByTransform(translation59, rotation41)
    
    translation60 = NXOpen.Vector3d(1.4210854715202004e-14, -8.3038227260308233, 11.00971168940786)
    rotation42 = NXOpen.Matrix3x3()
    
    rotation42.Xx = 1.0
    rotation42.Xy = 2.8252311017963698e-16
    rotation42.Xz = -1.2034766211112577e-15
    rotation42.Yx = 3.1760774579756289e-16
    rotation42.Yy = 0.86602540378443893
    rotation42.Yz = 0.49999999999999994
    rotation42.Zx = 1.1940757213306928e-15
    rotation42.Zy = -0.49999999999999939
    rotation42.Zz = 0.86602540378443915
    componentNetwork11.DragByTransform(translation60, rotation42)
    
    translation61 = NXOpen.Vector3d(1.4210854715202004e-14, -7.1349985500693691, 33.496839844800334)
    rotation43 = NXOpen.Matrix3x3()
    
    rotation43.Xx = 1.0
    rotation43.Xy = 1.8990743281414515e-15
    rotation43.Xz = -2.4123146727744856e-15
    rotation43.Yx = 1.9681775704777358e-15
    rotation43.Yy = 0.17364817766693141
    rotation43.Yz = 0.98480775301220824
    rotation43.Zx = 2.3543301676169531e-15
    rotation43.Zy = -0.98480775301220758
    rotation43.Zz = 0.17364817766693161
    componentNetwork11.DragByTransform(translation61, rotation43)
    
    translation62 = NXOpen.Vector3d(-1.4210854715202004e-14, 6.4022020271700182, 45.696313063792978)
    rotation44 = NXOpen.Matrix3x3()
    
    rotation44.Xx = 1.0
    rotation44.Xy = 3.5159131142511054e-15
    rotation44.Xz = -2.1789994025686875e-15
    rotation44.Yx = 3.5766814857063943e-15
    rotation44.Yy = -0.49999999999999856
    rotation44.Yz = 0.86602540378444004
    rotation44.Zx = 2.0737454957149066e-15
    rotation44.Zy = -0.86602540378443948
    rotation44.Zz = -0.49999999999999861
    componentNetwork11.DragByTransform(translation62, rotation44)
    
    translation63 = NXOpen.Vector3d(-2.8421709430404007e-14, 13.13448901121123, 47.440483483284083)
    rotation45 = NXOpen.Matrix3x3()
    
    rotation45.Xx = 1.0
    rotation45.Xy = 4.0221190283065106e-15
    rotation45.Xz = -1.8151022706119275e-15
    rotation45.Yx = 4.0717361958282993e-15
    rotation45.Yy = -0.70710678118654613
    rotation45.Yz = 0.70710678118654913
    rotation45.Zx = 1.6953158318542843e-15
    rotation45.Zy = -0.70710678118654879
    rotation45.Zz = -0.70710678118654635
    componentNetwork11.DragByTransform(translation63, rotation45)
    
    translation64 = NXOpen.Vector3d(-4.2632564145606011e-14, 15.451326666469061, 47.623822986518377)
    rotation46 = NXOpen.Matrix3x3()
    
    rotation46.Xx = 1.0
    rotation46.Xy = 4.1675965639223962e-15
    rotation46.Xz = -1.6659671173063308e-15
    rotation46.Yx = 4.212700502053535e-15
    rotation46.Yy = -0.76604444311897668
    rotation46.Yz = 0.64278760968654103
    rotation46.Zx = 1.5420450657625437e-15
    rotation46.Zy = -0.64278760968654081
    rotation46.Zz = -0.7660444431189769
    componentNetwork11.DragByTransform(translation64, rotation46)
    
    translation65 = NXOpen.Vector3d(-4.2632564145606011e-14, 17.775327145555593, 47.604539120921416)
    rotation47 = NXOpen.Matrix3x3()
    
    rotation47.Xx = 1.0
    rotation47.Xy = 4.2995225285382585e-15
    rotation47.Xz = -1.5047202656144943e-15
    rotation47.Yx = 4.3397699690750676e-15
    rotation47.Yy = -0.81915204428899047
    rotation47.Yz = 0.57357643635104816
    rotation47.Zx = 1.3770716923995232e-15
    rotation47.Zy = -0.57357643635104782
    rotation47.Zz = -0.8191520442889908
    componentNetwork11.DragByTransform(translation65, rotation47)
    
    translation66 = NXOpen.Vector3d(-4.2632564145606011e-14, 20.088803401555126, 47.382778648354304)
    rotation48 = NXOpen.Matrix3x3()
    
    rotation48.Xx = 1.0
    rotation48.Xy = 4.4168928859042966e-15
    rotation48.Xz = -1.3325889014413039e-15
    rotation48.Yx = 4.4519775215222222e-15
    rotation48.Yy = -0.86602540378443749
    rotation48.Yz = 0.50000000000000211
    rotation48.Zx = 1.2016512587501618e-15
    rotation48.Zy = -0.500000000000002
    rotation48.Zz = -0.86602540378443782
    componentNetwork11.DragByTransform(translation66, rotation48)
    
    translation67 = NXOpen.Vector3d(-4.2632564145606011e-14, 22.374148483244348, 46.960229299915923)
    rotation49 = NXOpen.Matrix3x3()
    
    rotation49.Xx = 1.0
    rotation49.Xy = 4.5188143767307961e-15
    rotation49.Xz = -1.1508830484038771e-15
    rotation49.Yx = 4.5484691921681026e-15
    rotation49.Yy = -0.90630778703664905
    rotation49.Yz = 0.42261826174070166
    rotation49.Zx = 1.0171188202362842e-15
    rotation49.Zy = -0.42261826174070161
    rotation49.Zz = -0.90630778703664927
    componentNetwork11.DragByTransform(translation67, rotation49)
    
    translation68 = NXOpen.Vector3d(-7.1054273576010019e-14, 24.613969534622505, 46.340106931290151)
    rotation50 = NXOpen.Matrix3x3()
    
    rotation50.Xx = 1.0
    rotation50.Xy = 4.6045113169306867e-15
    rotation50.Xz = -9.6098559776082253e-16
    rotation50.Yx = 4.6285106211358302e-15
    rotation50.Yy = -0.93969262078590754
    rotation50.Yz = 0.34202014332567104
    rotation50.Zx = 8.2487878013871412e-16
    rotation50.Zy = -0.3420201433256711
    rotation50.Zz = -0.93969262078590787
    componentNetwork11.DragByTransform(translation68, rotation50)
    
    translation69 = NXOpen.Vector3d(-7.1054273576010019e-14, 26.791220165047694, 45.527131048142365)
    rotation51 = NXOpen.Matrix3x3()
    
    rotation51.Xx = 1.0
    rotation51.Xy = 4.673331501043821e-15
    rotation51.Xz = -7.6434178377474951e-16
    rotation51.Yx = 4.6914926448206228e-15
    rotation51.Yy = -0.96592582628906765
    rotation51.Yz = 0.25881904510252318
    rotation51.Zx = 6.2639420124030405e-16
    rotation51.Zy = -0.25881904510252324
    rotation51.Zz = -0.96592582628906798
    componentNetwork11.DragByTransform(translation69, rotation51)
    
    translation70 = NXOpen.Vector3d(-7.1054273576010019e-14, 28.889330182562492, 44.527488887831566)
    rotation52 = NXOpen.Matrix3x3()
    
    rotation52.Xx = 1.0
    rotation52.Xy = 4.7247511659143347e-15
    rotation52.Xz = -5.6244818460687337e-16
    rotation52.Yx = 4.7369359319926563e-15
    rotation52.Yy = -0.98480775301220758
    rotation52.Yz = 0.17364817766693286
    rotation52.Zx = 4.2317567103473662e-16
    rotation52.Zy = -0.17364817766693297
    rotation52.Zz = -0.98480775301220802
    componentNetwork11.DragByTransform(translation70, rotation52)
    
    translation71 = NXOpen.Vector3d(-7.1054273576010019e-14, 26.791220165047694, 45.527131048142365)
    rotation53 = NXOpen.Matrix3x3()
    
    rotation53.Xx = 1.0
    rotation53.Xy = 4.673331501043821e-15
    rotation53.Xz = -7.6434178377474951e-16
    rotation53.Yx = 4.6914926448206228e-15
    rotation53.Yy = -0.96592582628906765
    rotation53.Yz = 0.25881904510252318
    rotation53.Zx = 6.2639420124030415e-16
    rotation53.Zy = -0.25881904510252329
    rotation53.Zz = -0.96592582628906809
    componentNetwork11.DragByTransform(translation71, rotation53)
    
    translation72 = NXOpen.Vector3d(-7.1054273576010019e-14, 24.613969534622505, 46.340106931290151)
    rotation54 = NXOpen.Matrix3x3()
    
    rotation54.Xx = 1.0
    rotation54.Xy = 4.6045113169306867e-15
    rotation54.Xz = -9.6098559776082253e-16
    rotation54.Yx = 4.6285106211358302e-15
    rotation54.Yy = -0.93969262078590765
    rotation54.Yz = 0.34202014332567104
    rotation54.Zx = 8.2487878013871422e-16
    rotation54.Zy = -0.34202014332567116
    rotation54.Zz = -0.93969262078590798
    componentNetwork11.DragByTransform(translation72, rotation54)
    
    translation73 = NXOpen.Vector3d(-4.2632564145606011e-14, 22.374148483244348, 46.96022929991593)
    rotation55 = NXOpen.Matrix3x3()
    
    rotation55.Xx = 1.0
    rotation55.Xy = 4.5188143767307961e-15
    rotation55.Xz = -1.1508830484038773e-15
    rotation55.Yx = 4.5484691921681034e-15
    rotation55.Yy = -0.90630778703664927
    rotation55.Yz = 0.42261826174070166
    rotation55.Zx = 1.0171188202362842e-15
    rotation55.Zy = -0.42261826174070166
    rotation55.Zz = -0.90630778703664949
    componentNetwork11.DragByTransform(translation73, rotation55)
    
    translation74 = NXOpen.Vector3d(-4.2632564145606011e-14, 20.088803401555133, 47.382778648354311)
    rotation56 = NXOpen.Matrix3x3()
    
    rotation56.Xx = 1.0
    rotation56.Xy = 4.4168928859042966e-15
    rotation56.Xz = -1.3325889014413041e-15
    rotation56.Yx = 4.4519775215222229e-15
    rotation56.Yy = -0.86602540378443771
    rotation56.Yz = 0.50000000000000211
    rotation56.Zx = 1.201651258750162e-15
    rotation56.Zy = -0.50000000000000211
    rotation56.Zz = -0.86602540378443804
    componentNetwork11.DragByTransform(translation74, rotation56)
    
    translation75 = NXOpen.Vector3d(-4.2632564145606011e-14, 17.7753271455556, 47.604539120921416)
    rotation57 = NXOpen.Matrix3x3()
    
    rotation57.Xx = 1.0
    rotation57.Xy = 4.2995225285382593e-15
    rotation57.Xz = -1.5047202656144943e-15
    rotation57.Yx = 4.3397699690750692e-15
    rotation57.Yy = -0.8191520442889908
    rotation57.Yz = 0.57357643635104816
    rotation57.Zx = 1.3770716923995238e-15
    rotation57.Zy = -0.57357643635104805
    rotation57.Zz = -0.81915204428899102
    componentNetwork11.DragByTransform(translation75, rotation57)
    
    translation76 = NXOpen.Vector3d(-4.2632564145606011e-14, 15.451326666469063, 47.623822986518384)
    rotation58 = NXOpen.Matrix3x3()
    
    rotation58.Xx = 1.0
    rotation58.Xy = 4.1675965639223962e-15
    rotation58.Xz = -1.6659671173063308e-15
    rotation58.Yx = 4.2127005020535358e-15
    rotation58.Yy = -0.76604444311897701
    rotation58.Yz = 0.64278760968654114
    rotation58.Zx = 1.5420450657625447e-15
    rotation58.Zy = -0.64278760968654114
    rotation58.Zz = -0.76604444311897713
    componentNetwork11.DragByTransform(translation76, rotation58)
    
    translation77 = NXOpen.Vector3d(-2.8421709430404007e-14, 10.842446713283442, 47.055915935541577)
    rotation59 = NXOpen.Matrix3x3()
    
    rotation59.Xx = 1.0
    rotation59.Xy = 3.8641970935783777e-15
    rotation59.Xz = -1.9509907169643615e-15
    rotation59.Yx = 3.9179498738863111e-15
    rotation59.Yy = -0.64278760968653825
    rotation59.Yz = 0.76604444311897968
    rotation59.Zx = 1.8357175075973681e-15
    rotation59.Zy = -0.76604444311897957
    rotation59.Zz = -0.64278760968653825
    componentNetwork11.DragByTransform(translation77, rotation59)
    
    translation78 = NXOpen.Vector3d(-1.4210854715202004e-14, 6.40220202717002, 45.696313063792985)
    rotation60 = NXOpen.Matrix3x3()
    
    rotation60.Xx = 1.0
    rotation60.Xy = 3.5159131142511061e-15
    rotation60.Xz = -2.1789994025686875e-15
    rotation60.Yx = 3.5766814857063943e-15
    rotation60.Yy = -0.49999999999999883
    rotation60.Yz = 0.86602540378444026
    rotation60.Zx = 2.0737454957149078e-15
    rotation60.Zy = -0.86602540378443993
    rotation60.Zz = -0.49999999999999878
    componentNetwork11.DragByTransform(translation78, rotation60)
    
    translation79 = NXOpen.Vector3d(-1.4210854715202004e-14, 4.2877925821387564, 44.731625138591582)
    rotation61 = NXOpen.Matrix3x3()
    
    rotation61.Xx = 1.0
    rotation61.Xy = 3.3282017210342637e-15
    rotation61.Xz = -2.2693843580477221e-15
    rotation61.Yx = 3.3917966779660036e-15
    rotation61.Yy = -0.42261826174069822
    rotation61.Yz = 0.90630778703665127
    rotation61.Zx = 2.169560271374561e-15
    rotation61.Zy = -0.90630778703665105
    rotation61.Zz = -0.42261826174069811
    componentNetwork11.DragByTransform(translation79, rotation61)
    
    translation80 = NXOpen.Vector3d(-1.4210854715202004e-14, 0.35073668176362105, 42.269129721591412)
    rotation62 = NXOpen.Matrix3x3()
    
    rotation62.Xx = 1.0
    rotation62.Xy = 2.932772240236131e-15
    rotation62.Xz = -2.3994813091371734e-15
    rotation62.Yx = 3.0005505515347235e-15
    rotation62.Yy = -0.25881904510251957
    rotation62.Yz = 0.96592582628906942
    rotation62.Zx = 2.3111508941245174e-15
    rotation62.Zy = -0.96592582628906909
    rotation62.Zz = -0.25881904510251941
    componentNetwork11.DragByTransform(translation80, rotation62)
    
    translation81 = NXOpen.Vector3d(0.0, -1.4419464009190541, 40.790063306811419)
    rotation63 = NXOpen.Matrix3x3()
    
    rotation63.Xx = 1.0
    rotation63.Xy = 2.7280636097705631e-15
    rotation63.Xz = -2.4382031883951136e-15
    rotation63.Yx = 2.7971668521068469e-15
    rotation63.Yy = -0.17364817766692919
    rotation63.Yz = 0.98480775301220913
    rotation63.Zx = 2.3558491510809382e-15
    rotation63.Zy = -0.9848077530122088
    rotation63.Zz = -0.17364817766692897
    componentNetwork11.DragByTransform(translation81, rotation63)
    
    translation82 = NXOpen.Vector3d(1.4210854715202004e-14, -3.0988986512930303, 39.160382560699645)
    rotation64 = NXOpen.Matrix3x3()
    
    rotation64.Xx = 1.0
    rotation64.Xy = 2.5207591232998309e-15
    rotation64.Xz = -2.4589361864769401e-15
    rotation64.Yx = 2.5906613792739485e-15
    rotation64.Yy = -0.087155742747657056
    rotation64.Yz = 0.99619469809174643
    rotation64.Zx = 2.3826512602884643e-15
    rotation64.Zy = -0.9961946980917461
    rotation64.Zz = -0.087155742747656778
    componentNetwork11.DragByTransform(translation82, rotation64)
    
    translation83 = NXOpen.Vector3d(1.4210854715202004e-14, -4.6075096622378453, 37.392490337762155)
    rotation65 = NXOpen.Matrix3x3()
    
    rotation65.Xx = 1.0
    rotation65.Xy = 2.3124364931398482e-15
    rotation65.Xz = -2.4615225127483233e-15
    rotation65.Yx = 2.3826057643757005e-15
    rotation65.Yy = 1.087717359863924e-15
    rotation65.Yz = 1.0000000000000009
    rotation65.Zx = 2.3913532415124695e-15
    rotation65.Zy = -1.0000000000000004
    rotation65.Zz = 1.406906479443651e-15
    componentNetwork11.DragByTransform(translation83, rotation65)
    
    translation84 = NXOpen.Vector3d(1.4210854715202004e-14, -5.9562979930359745, 35.499841365298003)
    rotation66 = NXOpen.Matrix3x3()
    
    rotation66.Xx = 1.0
    rotation66.Xy = 2.1046811802947755e-15
    rotation66.Xz = -2.4459424837046719e-15
    rotation66.Yx = 2.1745834362688931e-15
    rotation66.Yy = 0.087155742747659207
    rotation66.Yz = 0.99619469809174632
    rotation66.Zx = 2.3818888674214404e-15
    rotation66.Zy = -0.99619469809174588
    rotation66.Zz = 0.087155742747659568
    componentNetwork11.DragByTransform(translation84, rotation66)
    
    translation85 = NXOpen.Vector3d(1.4210854715202004e-14, -8.1346407103801752, 31.398729827285539)
    rotation67 = NXOpen.Matrix3x3()
    
    rotation67.Xx = 1.0
    rotation67.Xy = 1.6971807289735756e-15
    rotation67.Xz = -2.3608950079039728e-15
    rotation67.Yx = 1.7649590402721682e-15
    rotation67.Yy = 0.25881904510252168
    rotation67.Yz = 0.96592582628906887
    rotation67.Zx = 2.308886880444922e-15
    rotation67.Zy = -0.96592582628906842
    rotation67.Zz = 0.25881904510252213
    componentNetwork11.DragByTransform(translation85, rotation67)
    
    translation86 = NXOpen.Vector3d(1.4210854715202004e-14, -9.5677389621537472, 26.981658145482193)
    rotation68 = NXOpen.Matrix3x3()
    
    rotation68.Xx = 1.0
    rotation68.Xy = 1.3106394643444477e-15
    rotation68.Xz = -2.2063778835909486e-15
    rotation68.Yx = 1.3742344212761879e-15
    rotation68.Yy = 0.42261826174070022
    rotation68.Yz = 0.90630778703665049
    rotation68.Zx = 2.1658634277924018e-15
    rotation68.Zy = -0.90630778703665005
    rotation68.Zz = 0.42261826174070077
    componentNetwork11.DragByTransform(translation86, rotation68)
    
    translation87 = NXOpen.Vector3d(2.8421709430404007e-14, -10.231332648756215, 20.058836328706903)
    rotation69 = NXOpen.Matrix3x3()
    
    rotation69.Xx = 1.0
    rotation69.Xy = 7.9555539544199334e-16
    rotation69.Xz = -1.8551600707825496e-15
    rotation69.Yx = 8.493081757499268e-16
    rotation69.Yy = 0.64278760968653992
    rotation69.Yz = 0.76604444311897846
    rotation69.Zx = 1.8300947376778353e-15
    rotation69.Zy = -0.7660444431189779
    rotation69.Zz = 0.64278760968654047
    componentNetwork11.DragByTransform(translation87, rotation69)
    
    translation88 = NXOpen.Vector3d(1.4210854715202004e-14, -9.0805567967752339, 13.200153260783736)
    rotation70 = NXOpen.Matrix3x3()
    
    rotation70.Xx = 1.0
    rotation70.Xy = 3.8892424951312061e-16
    rotation70.Xz = -1.3825961478773026e-15
    rotation70.Yx = 4.2917169004993087e-16
    rotation70.Yy = 0.81915204428899224
    rotation70.Yz = 0.57357643635104638
    rotation70.Zx = 1.369906178620566e-15
    rotation70.Zy = -0.57357643635104583
    rotation70.Zz = 0.81915204428899291
    componentNetwork11.DragByTransform(translation88, rotation70)
    
    translation89 = NXOpen.Vector3d(1.4210854715202004e-14, -7.3391348008294273, 8.8953022443765946)
    rotation71 = NXOpen.Matrix3x3()
    
    rotation71.Xx = 1.0
    rotation71.Xy = 1.9213815470060159e-16
    rotation71.Xz = -1.0157652278944169e-15
    rotation71.Yx = 2.2179297013790931e-16
    rotation71.Yy = 0.90630778703665038
    rotation71.Yz = 0.42261826174069977
    rotation71.Zx = 1.009190913590303e-15
    rotation71.Zy = -0.42261826174069933
    rotation71.Zz = 0.90630778703665082
    componentNetwork11.DragByTransform(translation89, rotation71)
    
    translation90 = NXOpen.Vector3d(1.4210854715202004e-14, -6.1938348787763005, 6.8730168582819644)
    rotation72 = NXOpen.Matrix3x3()
    
    rotation72.Xx = 1.0
    rotation72.Xy = 1.1845726716314028e-16
    rotation72.Xz = -8.2089056527239457e-16
    rotation72.Yx = 1.4245657136828454e-16
    rotation72.Yy = 0.93969262078590876
    rotation72.Yz = 0.34202014332566905
    rotation72.Zx = 8.1665884042279637e-16
    rotation72.Zy = -0.34202014332566871
    rotation72.Zz = 0.93969262078590932
    componentNetwork11.DragByTransform(translation90, rotation72)
    
    translation91 = NXOpen.Vector3d(1.4210854715202004e-14, -4.8766393838292679, 4.9582463440014521)
    rotation73 = NXOpen.Matrix3x3()
    
    rotation73.Xx = 1.0
    rotation73.Xy = 6.2041203611149139e-17
    rotation73.Xz = -6.2033574709628418e-16
    rotation73.Yx = 8.0202347387952143e-17
    rotation73.Yy = 0.96592582628906865
    rotation73.Yz = 0.25881904510252107
    rotation73.Zx = 6.1794478715902322e-16
    rotation73.Zy = -0.25881904510252074
    rotation73.Zz = 0.9659258262890692
    componentNetwork11.DragByTransform(translation91, rotation73)
    
    translation92 = NXOpen.Vector3d(0.0, -1.7678922229375047, 1.5086110109447972)
    rotation74 = NXOpen.Matrix3x3()
    
    rotation74.Xx = 1.0
    rotation74.Xy = 2.5863262713820546e-18
    rotation74.Xz = -2.0832263015998372e-16
    rotation74.Yx = 8.701981224004826e-18
    rotation74.Yy = 0.99619469809174588
    rotation74.Yz = 0.087155742747658471
    rotation74.Zx = 2.0805561489824836e-16
    rotation74.Zy = -0.087155742747658235
    rotation74.Zz = 0.99619469809174643
    componentNetwork11.DragByTransform(translation92, rotation74)
    
    translation93 = NXOpen.Vector3d(0.0, -1.4210854715202004e-14, -1.7763568394002505e-14)
    rotation75 = NXOpen.Matrix3x3()
    
    rotation75.Xx = 1.0
    rotation75.Xy = -1.5777218104420236e-30
    rotation75.Xz = -8.8495192448273649e-31
    rotation75.Yx = -1.1832913578315177e-30
    rotation75.Yy = 1.0000000000000004
    rotation75.Yz = 3.0006142091752632e-16
    rotation75.Zx = 2.1570415377136919e-31
    rotation75.Zy = -9.1894603800309417e-17
    rotation75.Zz = 1.0000000000000009
    componentNetwork11.DragByTransform(translation93, rotation75)
    
    translation94 = NXOpen.Vector3d(-1.4210854715202004e-14, 3.8956504929617921, -2.5274888878315522)
    rotation76 = NXOpen.Matrix3x3()
    
    rotation76.Xx = 1.0
    rotation76.Xy = 4.9207839973834923e-17
    rotation76.Xz = 4.1336216499839568e-16
    rotation76.Yx = 3.7023073895512885e-17
    rotation76.Yy = 0.98480775301220858
    rotation76.Yz = -0.17364817766693003
    rotation76.Zx = -4.1442819389796441e-16
    rotation76.Zy = 0.17364817766693014
    rotation76.Zz = 0.98480775301220902
    componentNetwork11.DragByTransform(translation94, rotation76)
    
    translation95 = NXOpen.Vector3d(-1.4210854715202004e-14, 5.9937605104765961, -3.5271310481423583)
    rotation77 = NXOpen.Matrix3x3()
    
    rotation77.Xx = 1.0
    rotation77.Xy = 1.0062750484434855e-16
    rotation77.Xz = 6.1525576416627217e-16
    rotation77.Yx = 8.2466361067545546e-17
    rotation77.Yy = 0.96592582628906887
    rotation77.Yz = -0.25881904510252052
    rotation77.Zx = -6.1764672410353224e-16
    rotation77.Zy = 0.25881904510252057
    rotation77.Zz = 0.96592582628906931
    componentNetwork11.DragByTransform(translation95, rotation77)
    
    translation96 = NXOpen.Vector3d(-1.4210854715202004e-14, 8.1710111409017792, -4.3401069312901583)
    rotation78 = NXOpen.Matrix3x3()
    
    rotation78.Xx = 1.0
    rotation78.Xy = 1.6944768895748249e-16
    rotation78.Xz = 8.1189957815234548e-16
    rotation78.Yx = 1.4544838475233822e-16
    rotation78.Yy = 0.93969262078590909
    rotation78.Yz = -0.34202014332566849
    rotation78.Zx = -8.161313030019427e-16
    rotation78.Zy = 0.3420201433256686
    rotation78.Zz = 0.93969262078590954
    componentNetwork11.DragByTransform(translation96, rotation78)
    
    translation97 = NXOpen.Vector3d(-4.2632564145606011e-14, 10.410832192279939, -4.9602292999159374)
    rotation79 = NXOpen.Matrix3x3()
    
    rotation79.Xx = 1.0
    rotation79.Xy = 2.551446291573727e-16
    rotation79.Xz = 1.0017970287954005e-15
    rotation79.Yx = 2.2548981372006458e-16
    rotation79.Yy = 0.90630778703665082
    rotation79.Yz = -0.42261826174069927
    rotation79.Zx = -1.0083713430995132e-15
    rotation79.Zy = 0.42261826174069927
    rotation79.Zz = 0.90630778703665116
    componentNetwork11.DragByTransform(translation97, rotation79)
    
    translation98 = NXOpen.Vector3d(-4.2632564145606011e-14, 12.696177273969155, -5.3827786483543285)
    rotation80 = NXOpen.Matrix3x3()
    
    rotation80.Xx = 1.0
    rotation80.Xy = 3.5706611998387096e-16
    rotation80.Xz = 1.1835028818328277e-15
    rotation80.Yx = 3.2198148436594426e-16
    rotation80.Yy = 0.86602540378443948
    rotation80.Yz = -0.49999999999999983
    rotation80.Zx = -1.1929037816133912e-15
    rotation80.Zy = 0.49999999999999983
    rotation80.Zz = 0.86602540378443993
    componentNetwork11.DragByTransform(translation98, rotation80)
    
    translation99 = NXOpen.Vector3d(-4.2632564145606011e-14, 15.00965352996869, -5.6045391209214444)
    rotation81 = NXOpen.Matrix3x3()
    
    rotation81.Xx = 1.0
    rotation81.Xy = 4.7443647734990828e-16
    rotation81.Xz = 1.3556342460060183e-15
    rotation81.Yx = 4.3418903681309842e-16
    rotation81.Yy = 0.81915204428899269
    rotation81.Yz = -0.57357643635104605
    rotation81.Zx = -1.3683242152627535e-15
    rotation81.Zy = 0.57357643635104594
    rotation81.Zz = 0.81915204428899313
    componentNetwork11.DragByTransform(translation99, rotation81)
    
    translation100 = NXOpen.Vector3d(-4.2632564145606011e-14, 17.333654009055223, -5.6238229865184124)
    rotation82 = NXOpen.Matrix3x3()
    
    rotation82.Xx = 1.0
    rotation82.Xy = 6.0636244196577059e-16
    rotation82.Xz = 1.5168810976978553e-15
    rotation82.Yx = 5.6125850383463062e-16
    rotation82.Yy = 0.76604444311897912
    rotation82.Yz = -0.64278760968653914
    rotation82.Zx = -1.5332975886257743e-15
    rotation82.Zy = 0.64278760968653914
    rotation82.Zz = 0.76604444311897946
    componentNetwork11.DragByTransform(translation100, rotation82)
    
    translation101 = NXOpen.Vector3d(-5.6843418860808015e-14, 19.650491664313058, -5.440483483284126)
    rotation83 = NXOpen.Matrix3x3()
    
    rotation83.Xx = 1.0
    rotation83.Xy = 7.5183997758165559e-16
    rotation83.Xz = 1.6660162510034527e-15
    rotation83.Yx = 7.0222281005986595e-16
    rotation83.Yy = 0.70710678118654868
    rotation83.Yz = -0.70710678118654746
    rotation83.Zx = -1.6865683547175152e-15
    rotation83.Zy = 0.70710678118654735
    rotation83.Zz = 0.70710678118654902
    componentNetwork11.DragByTransform(translation101, rotation83)
    
    translation102 = NXOpen.Vector3d(-5.6843418860808015e-14, 21.942533962240852, -5.0559159355416199)
    rotation84 = NXOpen.Matrix3x3()
    
    rotation84.Xx = 1.0
    rotation84.Xy = 9.0976191230978835e-16
    rotation84.Xz = 1.8019046973558868e-15
    rotation84.Yx = 8.5600913200185489e-16
    rotation84.Yy = 0.64278760968654058
    rotation84.Yz = -0.76604444311897801
    rotation84.Zx = -1.8269700304605987e-15
    rotation84.Zy = 0.7660444431189779
    rotation84.Zz = 0.64278760968654081
    componentNetwork11.DragByTransform(translation102, rotation84)
    
    translation103 = NXOpen.Vector3d(-5.6843418860808015e-14, 24.192337076978397, -4.4730471345374383)
    rotation85 = NXOpen.Matrix3x3()
    
    rotation85.Xx = 1.0
    rotation85.Xy = 1.0789263648710163e-15
    rotation85.Xz = 1.9235122436267288e-15
    rotation85.Yx = 1.021447062891899e-15
    rotation85.Yy = 0.57357643635104727
    rotation85.Yz = -0.81915204428899191
    rotation85.Zx = -1.9534340743257708e-15
    rotation85.Zy = 0.81915204428899169
    rotation85.Zz = 0.5735764363510476
    componentNetwork11.DragByTransform(translation103, rotation85)
    
    translation104 = NXOpen.Vector3d(-7.1054273576010019e-14, 26.382778648354282, -3.6963130637930419)
    rotation86 = NXOpen.Matrix3x3()
    
    rotation86.Xx = 1.0
    rotation86.Xy = 1.2580458916370599e-15
    rotation86.Xz = 2.0299133829602136e-15
    rotation86.Yx = 1.1972775201817708e-15
    rotation86.Yy = 0.50000000000000133
    rotation86.Yz = -0.86602540378443893
    rotation86.Zx = -2.0649980185781391e-15
    rotation86.Zy = 0.86602540378443871
    rotation86.Zz = 0.50000000000000155
    componentNetwork11.DragByTransform(translation104, rotation86)
    
    translation105 = NXOpen.Vector3d(-7.1054273576010019e-14, 28.497188093385542, -2.7316251385916388)
    rotation87 = NXOpen.Matrix3x3()
    
    rotation87.Xx = 1.0
    rotation87.Xy = 1.4457572848539019e-15
    rotation87.Xz = 2.1202983384392486e-15
    rotation87.Yx = 1.3821623279221616e-15
    rotation87.Yy = 0.42261826174070088
    rotation87.Yz = -0.90630778703665016
    rotation87.Zx = -2.1608127942377931e-15
    rotation87.Zy = 0.90630778703665005
    rotation87.Zz = 0.42261826174070105
    componentNetwork11.DragByTransform(translation105, rotation87)
    
    translation106 = NXOpen.Vector3d(-7.1054273576010019e-14, 30.519473479480173, -1.5863252165385155)
    rotation88 = NXOpen.Matrix3x3()
    
    rotation88.Xx = 1.0
    rotation88.Xy = 1.640631947475924e-15
    rotation88.Xz = 2.1939792259767099e-15
    rotation88.Yx = 1.5746944010896685e-15
    rotation88.Yy = 0.34202014332567032
    rotation88.Yz = -0.93969262078590876
    rotation88.Zx = -2.2401491930074183e-15
    rotation88.Zy = 0.93969262078590854
    rotation88.Zz = 0.34202014332567038
    componentNetwork11.DragByTransform(translation106, rotation88)
    
    translation107 = NXOpen.Vector3d(-7.1054273576010019e-14, 32.434243993760688, -0.26912972159148296)
    rotation89 = NXOpen.Matrix3x3()
    
    rotation89.Xx = 1.0
    rotation89.Xy = 1.8411867656520342e-15
    rotation89.Xz = 2.2503952895287011e-15
    rotation89.Yx = 1.7734084543534414e-15
    rotation89.Yy = 0.2588190451025224
    rotation89.Yz = -0.96592582628906876
    rotation89.Zx = -2.3024034169877503e-15
    rotation89.Zy = 0.96592582628906853
    rotation89.Zz = 0.2588190451025224
    componentNetwork11.DragByTransform(translation107, rotation89)
    
    translation108 = NXOpen.Vector3d(-8.5265128291212022e-14, 34.22692707644336, 1.20993669318851)
    rotation90 = NXOpen.Matrix3x3()
    
    rotation90.Xx = 1.0
    rotation90.Xy = 2.0458953961176021e-15
    rotation90.Xz = 2.2891171687866417e-15
    rotation90.Yx = 1.9767921537813179e-15
    rotation90.Yy = 0.17364817766693208
    rotation90.Yz = -0.98480775301220869
    rotation90.Zx = -2.3471016739441719e-15
    rotation90.Zy = 0.98480775301220846
    rotation90.Zz = 0.17364817766693202
    componentNetwork11.DragByTransform(translation108, rotation90)
    
    translation109 = NXOpen.Vector3d(-9.9475983006414026e-14, 35.88387932681735, 2.8396174393002731)
    rotation91 = NXOpen.Matrix3x3()
    
    rotation91.Xx = 1.0
    rotation91.Xy = 2.2531998825883343e-15
    rotation91.Xz = 2.3098501668684686e-15
    rotation91.Yx = 2.1832976266142163e-15
    rotation91.Yy = 0.087155742747659956
    rotation91.Yz = -0.99619469809174621
    rotation91.Zx = -2.3739037831516984e-15
    rotation91.Zy = 0.99619469809174599
    rotation91.Zz = 0.087155742747659831
    componentNetwork11.DragByTransform(translation109, rotation91)
    
    translation110 = NXOpen.Vector3d(-9.9475983006414026e-14, 37.392490337762169, 4.6075096622377636)
    rotation92 = NXOpen.Matrix3x3()
    
    rotation92.Xx = 1.0
    rotation92.Xy = 2.461522512748317e-15
    rotation92.Xz = 2.3124364931398522e-15
    rotation92.Yx = 2.3913532415124644e-15
    rotation92.Yy = 1.8404958675849353e-15
    rotation92.Yz = -1.0000000000000009
    rotation92.Zx = -2.3826057643757048e-15
    rotation92.Zy = 1.0000000000000007
    rotation92.Zz = 1.6462068382755283e-15
    componentNetwork11.DragByTransform(translation110, rotation92)
    
    translation111 = NXOpen.Vector3d(-9.9475983006414026e-14, 38.741278668560298, 6.5001586347019096)
    rotation93 = NXOpen.Matrix3x3()
    
    rotation93.Xx = 1.0
    rotation93.Xy = 2.6692778255933897e-15
    rotation93.Xz = 2.2968564640962011e-15
    rotation93.Yx = 2.5993755696192713e-15
    rotation93.Yy = -0.087155742747656292
    rotation93.Yz = -0.99619469809174666
    rotation93.Zx = -2.3731413902846765e-15
    rotation93.Zy = 0.99619469809174643
    rotation93.Zz = -0.087155742747656556
    componentNetwork11.DragByTransform(translation111, rotation93)
    
    translation112 = NXOpen.Vector3d(-9.9475983006414026e-14, 39.919979225593707, 8.5031601551995699)
    rotation94 = NXOpen.Matrix3x3()
    
    rotation94.Xx = 1.0
    rotation94.Xy = 2.8748846777467133e-15
    rotation94.Xz = 2.2632286531660161e-15
    rotation94.Yx = 2.8057814354104287e-15
    rotation94.Yy = -0.17364817766692844
    rotation94.Yz = -0.98480775301220924
    rotation94.Zx = -2.3455826904801911e-15
    rotation94.Zy = 0.98480775301220902
    rotation94.Zz = -0.17364817766692878
    componentNetwork11.DragByTransform(translation112, rotation94)
    
    translation113 = NXOpen.Vector3d(-9.9475983006414026e-14, 40.91962138590452, 10.601270172714372)
    rotation95 = NXOpen.Matrix3x3()
    
    rotation95.Xx = 1.0
    rotation95.Xy = 3.0767782769145897e-15
    rotation95.Xz = 2.2118089882955028e-15
    rotation95.Yx = 3.0089999656159968e-15
    rotation95.Yy = -0.25881904510251891
    rotation95.Yz = -0.96592582628906964
    rotation95.Zx = -2.3001394033081589e-15
    rotation95.Zy = 0.96592582628906942
    rotation95.Zz = -0.2588190451025193
    componentNetwork11.DragByTransform(translation113, rotation95)
    
    translation114 = NXOpen.Vector3d(-9.9475983006414026e-14, 41.73259726905232, 12.778520803139553)
    rotation96 = NXOpen.Matrix3x3()
    
    rotation96.Xx = 1.0
    rotation96.Xy = 3.2734220909006629e-15
    rotation96.Xz = 2.1429888041823697e-15
    rotation96.Yx = 3.2074845445144074e-15
    rotation96.Yy = -0.34202014332566694
    rotation96.Yz = -0.93969262078590998
    rotation96.Zx = -2.2371573796233662e-15
    rotation96.Zy = 0.93969262078590976
    rotation96.Zz = -0.34202014332566733
    componentNetwork11.DragByTransform(translation114, rotation96)
    
    translation115 = NXOpen.Vector3d(-9.9475983006414026e-14, 42.352719637678099, 15.018341854517713)
    rotation97 = NXOpen.Matrix3x3()
    
    rotation97.Xx = 1.0
    rotation97.Xy = 3.4633195415437177e-15
    rotation97.Xz = 2.0572918639824799e-15
    rotation97.Yx = 3.3997245846119774e-15
    rotation97.Yy = -0.42261826174069766
    rotation97.Yz = -0.90630778703665171
    rotation97.Zx = -2.1571159506556398e-15
    rotation97.Zy = 0.9063077870366516
    rotation97.Zz = -0.42261826174069816
    componentNetwork11.DragByTransform(translation115, rotation97)
    
    translation116 = NXOpen.Vector3d(-9.9475983006414026e-14, 42.775268986116494, 17.30368693620693)
    rotation98 = NXOpen.Matrix3x3()
    
    rotation98.Xx = 1.0
    rotation98.Xy = 3.6450253945811449e-15
    rotation98.Xz = 1.955370373155982e-15
    rotation98.Yx = 3.5842570231258559e-15
    rotation98.Yy = -0.49999999999999828
    rotation98.Yz = -0.86602540378444059
    rotation98.Zx = -2.0606242800097609e-15
    rotation98.Zy = 0.86602540378444037
    rotation98.Zz = -0.49999999999999878
    componentNetwork11.DragByTransform(translation116, rotation98)
    
    translation117 = NXOpen.Vector3d(-1.1368683772161603e-13, 42.997029458683613, 19.617163192206462)
    rotation99 = NXOpen.Matrix3x3()
    
    rotation99.Xx = 1.0
    rotation99.Xy = 3.8171567587543362e-15
    rotation99.Xz = 1.8380000157899447e-15
    rotation99.Yx = 3.7596774567752187e-15
    rotation99.Yy = -0.57357643635104449
    rotation99.Yz = -0.81915204428899391
    rotation99.Zx = -1.9484167275626072e-15
    rotation99.Zy = 0.81915204428899369
    rotation99.Zz = -0.57357643635104505
    componentNetwork11.DragByTransform(translation117, rotation99)
    
    translation118 = NXOpen.Vector3d(-1.1368683772161603e-13, 43.016313324280588, 21.941163671292998)
    rotation100 = NXOpen.Matrix3x3()
    
    rotation100.Xx = 1.0
    rotation100.Xy = 3.9784036104461729e-15
    rotation100.Xz = 1.7060740511740828e-15
    rotation100.Yx = 3.9246508301382394e-15
    rotation100.Yy = -0.64278760968653781
    rotation100.Yz = -0.76604444311898034
    rotation100.Zx = -1.8213472605410754e-15
    rotation100.Zy = 0.76604444311898023
    rotation100.Zz = -0.64278760968653825
    componentNetwork11.DragByTransform(translation118, rotation100)
    
    translation119 = NXOpen.Vector3d(-9.9475983006414026e-14, 42.832973821046302, 24.258001326550833)
    rotation101 = NXOpen.Matrix3x3()
    
    rotation101.Xx = 1.0
    rotation101.Xy = 4.1275387637517706e-15
    rotation101.Xz = 1.5605965155581982e-15
    rotation101.Yx = 4.0779215962299812e-15
    rotation101.Yy = -0.70710678118654613
    rotation101.Yz = -0.70710678118655002
    rotation101.Zx = -1.6803829543158402e-15
    rotation101.Zy = 0.7071067811865499
    rotation101.Zz = -0.70710678118654668
    componentNetwork11.DragByTransform(translation119, rotation101)
    
    translation120 = NXOpen.Vector3d(-9.9475983006414026e-14, 42.448406273303796, 26.550043624478626)
    rotation102 = NXOpen.Matrix3x3()
    
    rotation102.Xx = 1.0
    rotation102.Xy = 4.263427210104205e-15
    rotation102.Xz = 1.402674580830066e-15
    rotation102.Yx = 4.2183232719730647e-15
    rotation102.Yy = -0.76604444311897679
    rotation102.Yz = -0.64278760968654192
    rotation102.Zx = -1.5265966323738513e-15
    rotation102.Zy = 0.64278760968654192
    rotation102.Zz = -0.76604444311897735
    componentNetwork11.DragByTransform(translation120, rotation102)
    
    translation121 = NXOpen.Vector3d(-9.9475983006414026e-14, 41.865537472299621, 28.799846739216171)
    rotation103 = NXOpen.Matrix3x3()
    
    rotation103.Xx = 1.0
    rotation103.Xy = 4.385034756375047e-15
    rotation103.Xz = 1.2335101282688378e-15
    rotation103.Yx = 4.3447873158382371e-15
    rotation103.Yy = -0.81915204428899069
    rotation103.Yz = -0.57357643635104882
    rotation103.Zx = -1.3611587014838076e-15
    rotation103.Zy = 0.57357643635104871
    rotation103.Zz = -0.81915204428899135
    componentNetwork11.DragByTransform(translation121, rotation103)
    
    translation122 = NXOpen.Vector3d(-9.9475983006414026e-14, 41.088803401555232, 30.990288310592057)
    rotation104 = NXOpen.Matrix3x3()
    
    rotation104.Xx = 1.0
    rotation104.Xy = 4.4914358957085322e-15
    rotation104.Xz = 1.0543906015027943e-15
    rotation104.Yx = 4.4563512600906059e-15
    rotation104.Yy = -0.86602540378443782
    rotation104.Yz = -0.50000000000000289
    rotation104.Zx = -1.1853282441939356e-15
    rotation104.Zy = 0.50000000000000278
    rotation104.Zz = -0.86602540378443849
    componentNetwork11.DragByTransform(translation122, rotation104)
    
    translation123 = NXOpen.Vector3d(-9.9475983006414026e-14, 40.124115476353836, 33.10469775562332)
    rotation105 = NXOpen.Matrix3x3()
    
    rotation105.Xx = 1.0
    rotation105.Xy = 4.5818208511875668e-15
    rotation105.Xz = 8.6667920828595243e-16
    rotation105.Yx = 4.5521660357502595e-15
    rotation105.Yy = -0.90630778703664938
    rotation105.Yz = -0.42261826174070249
    rotation105.Zx = -1.0004434364535448e-15
    rotation105.Zy = 0.42261826174070233
    rotation105.Zz = -0.90630778703664994
    componentNetwork11.DragByTransform(translation123, rotation105)
    
    translation124 = NXOpen.Vector3d(-9.9475983006414026e-14, 38.978815554300709, 35.126983141717957)
    rotation106 = NXOpen.Matrix3x3()
    
    rotation106.Xx = 1.0
    rotation106.Xy = 4.6555017387250285e-15
    rotation106.Xz = 6.7180454566393044e-16
    rotation106.Yx = 4.631502434519885e-15
    rotation106.Yy = -0.93969262078590798
    rotation106.Yz = -0.34202014332567188
    rotation106.Zx = -8.0791136328603836e-16
    rotation106.Zy = 0.34202014332567182
    rotation106.Zz = -0.93969262078590865
    componentNetwork11.DragByTransform(translation124, rotation106)
    
    translation125 = NXOpen.Vector3d(-9.9475983006414026e-14, 38.978815554300709, 35.126983141717957)
    rotation107 = NXOpen.Matrix3x3()
    
    rotation107.Xx = 1.0
    rotation107.Xy = 4.6555017387250285e-15
    rotation107.Xz = 6.7180454566393044e-16
    rotation107.Yx = 4.631502434519885e-15
    rotation107.Yy = -0.93969262078590798
    rotation107.Yz = -0.34202014332567188
    rotation107.Zx = -8.0791136328603836e-16
    rotation107.Zy = 0.34202014332567182
    rotation107.Zz = -0.93969262078590865
    componentNetwork11.DragByTransform(translation125, rotation107)
    
    componentNetwork11.EndDrag()
    
    componentNetwork11.ResetDisplay()
    
    componentNetwork11.ApplyToModel()
    
    scaleAboutPoint42 = NXOpen.Point3d(3.3775217476619459, -19.569758361452667, 0.0)
    viewCenter42 = NXOpen.Point3d(-3.3775217476618362, 19.569758361452813, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint42, viewCenter42)
    
    scaleAboutPoint43 = NXOpen.Point3d(4.2219021845774209, -24.462197951815828, 0.0)
    viewCenter43 = NXOpen.Point3d(-4.2219021845772939, 24.462197951815988, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint43, viewCenter43)
    
    scaleAboutPoint44 = NXOpen.Point3d(5.1221607386417354, -30.577747439769812, 0.0)
    viewCenter44 = NXOpen.Point3d(-5.122160738641603, 30.577747439769972, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint44, viewCenter44)
    
    rotMatrix14 = NXOpen.Matrix3x3()
    
    rotMatrix14.Xx = 0.55646891875093363
    rotMatrix14.Xy = 0.77654126152436465
    rotMatrix14.Xz = -0.29550974876357183
    rotMatrix14.Yx = -0.028105007300549149
    rotMatrix14.Yy = 0.37305255975298912
    rotMatrix14.Yz = 0.92738443820584815
    rotMatrix14.Zx = 0.83039294977064737
    rotMatrix14.Zy = -0.50775531194846657
    rotMatrix14.Zz = 0.2294168523873345
    translation126 = NXOpen.Point3d(-49.029968467945018, -75.974495571208195, -4.0185749625499305)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix14, translation126, 1.36368231229158)
    
    scaleAboutPoint45 = NXOpen.Point3d(2.522276121300854, -41.326524141313278, 0.0)
    viewCenter45 = NXOpen.Point3d(-2.5222761213007545, 41.326524141313442, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint45, viewCenter45)
    
    markId63 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Rotate About Y-axis")
    
    loaded10 = componentNetwork11.IsReferencedGeometryLoaded()
    
    componentNetwork11.BeginDrag()
    
    translation127 = NXOpen.Vector3d(0.0, 3.8956504929618081, -2.5274888878315345)
    rotation108 = NXOpen.Matrix3x3()
    
    rotation108.Xx = 1.0
    rotation108.Xy = 4.92078399738365e-17
    rotation108.Xz = 4.1336216499839573e-16
    rotation108.Yx = 3.7023073895514068e-17
    rotation108.Yy = 0.98480775301220824
    rotation108.Yz = -0.17364817766693019
    rotation108.Zx = -4.1442819389796461e-16
    rotation108.Zy = 0.17364817766693028
    rotation108.Zz = 0.98480775301220824
    componentNetwork11.DragByTransform(translation127, rotation108)
    
    translation128 = NXOpen.Vector3d(-1.4210854715202004e-14, 5.9937605104766067, -3.527131048142337)
    rotation109 = NXOpen.Matrix3x3()
    
    rotation109.Xx = 1.0
    rotation109.Xy = 1.0062750484434973e-16
    rotation109.Xz = 6.1525576416627178e-16
    rotation109.Yx = 8.2466361067547124e-17
    rotation109.Yy = 0.96592582628906842
    rotation109.Yz = -0.25881904510252052
    rotation109.Zx = -6.1764672410353224e-16
    rotation109.Zy = 0.25881904510252063
    rotation109.Zz = 0.96592582628906842
    componentNetwork11.DragByTransform(translation128, rotation109)
    
    translation129 = NXOpen.Vector3d(-1.4210854715202004e-14, 8.171011140901788, -4.340106931290137)
    rotation110 = NXOpen.Matrix3x3()
    
    rotation110.Xx = 1.0
    rotation110.Xy = 1.6944768895748407e-16
    rotation110.Xz = 8.1189957815234479e-16
    rotation110.Yx = 1.454483847523398e-16
    rotation110.Yy = 0.93969262078590865
    rotation110.Yz = -0.34202014332566844
    rotation110.Zx = -8.161313030019426e-16
    rotation110.Zy = 0.3420201433256686
    rotation110.Zz = 0.93969262078590865
    componentNetwork11.DragByTransform(translation129, rotation110)
    
    translation130 = NXOpen.Vector3d(-2.8421709430404007e-14, 10.410832192279944, -4.9602292999159161)
    rotation111 = NXOpen.Matrix3x3()
    
    rotation111.Xx = 1.0
    rotation111.Xy = 2.5514462915737388e-16
    rotation111.Xz = 1.0017970287953995e-15
    rotation111.Yx = 2.2548981372006576e-16
    rotation111.Yy = 0.90630778703665027
    rotation111.Yz = -0.42261826174069911
    rotation111.Zx = -1.008371343099513e-15
    rotation111.Zy = 0.42261826174069933
    rotation111.Zz = 0.90630778703665027
    componentNetwork11.DragByTransform(translation130, rotation111)
    
    translation131 = NXOpen.Vector3d(-2.8421709430404007e-14, 12.696177273969163, -5.3827786483543036)
    rotation112 = NXOpen.Matrix3x3()
    
    rotation112.Xx = 1.0
    rotation112.Xy = 3.5706611998387214e-16
    rotation112.Xz = 1.1835028818328263e-15
    rotation112.Yx = 3.2198148436594584e-16
    rotation112.Yy = 0.86602540378443904
    rotation112.Yz = -0.49999999999999956
    rotation112.Zx = -1.192903781613391e-15
    rotation112.Zy = 0.49999999999999989
    rotation112.Zz = 0.86602540378443904
    componentNetwork11.DragByTransform(translation131, rotation112)
    
    translation132 = NXOpen.Vector3d(-2.8421709430404007e-14, 15.009653529968691, -5.6045391209214195)
    rotation113 = NXOpen.Matrix3x3()
    
    rotation113.Xx = 1.0
    rotation113.Xy = 4.7443647734990986e-16
    rotation113.Xz = 1.3556342460060165e-15
    rotation113.Yx = 4.341890368130996e-16
    rotation113.Yy = 0.81915204428899224
    rotation113.Yz = -0.5735764363510456
    rotation113.Zx = -1.3683242152627531e-15
    rotation113.Zy = 0.57357643635104594
    rotation113.Zz = 0.81915204428899213
    componentNetwork11.DragByTransform(translation132, rotation113)
    
    translation133 = NXOpen.Vector3d(-4.2632564145606011e-14, 17.333654009055223, -5.6238229865183911)
    rotation114 = NXOpen.Matrix3x3()
    
    rotation114.Xx = 1.0
    rotation114.Xy = 6.0636244196577216e-16
    rotation114.Xz = 1.5168810976978533e-15
    rotation114.Yx = 5.612585038346322e-16
    rotation114.Yy = 0.76604444311897857
    rotation114.Yz = -0.64278760968653881
    rotation114.Zx = -1.5332975886257743e-15
    rotation114.Zy = 0.64278760968653914
    rotation114.Zz = 0.76604444311897857
    componentNetwork11.DragByTransform(translation133, rotation114)
    
    translation134 = NXOpen.Vector3d(-4.2632564145606011e-14, 19.650491664313055, -5.4404834832841047)
    rotation115 = NXOpen.Matrix3x3()
    
    rotation115.Xx = 1.0
    rotation115.Xy = 7.5183997758165658e-16
    rotation115.Xz = 1.6660162510034503e-15
    rotation115.Yx = 7.0222281005986713e-16
    rotation115.Yy = 0.70710678118654813
    rotation115.Yz = -0.70710678118654702
    rotation115.Zx = -1.6865683547175148e-15
    rotation115.Zy = 0.70710678118654735
    rotation115.Zz = 0.70710678118654813
    componentNetwork11.DragByTransform(translation134, rotation115)
    
    translation135 = NXOpen.Vector3d(-4.2632564145606011e-14, 21.942533962240844, -5.0559159355415986)
    rotation116 = NXOpen.Matrix3x3()
    
    rotation116.Xx = 1.0
    rotation116.Xy = 9.0976191230978874e-16
    rotation116.Xz = 1.8019046973558845e-15
    rotation116.Yx = 8.5600913200185607e-16
    rotation116.Yy = 0.64278760968654003
    rotation116.Yz = -0.76604444311897757
    rotation116.Zx = -1.8269700304605987e-15
    rotation116.Zy = 0.7660444431189779
    rotation116.Zz = 0.64278760968654003
    componentNetwork11.DragByTransform(translation135, rotation116)
    
    translation136 = NXOpen.Vector3d(-4.2632564145606011e-14, 19.650491664313055, -5.4404834832841082)
    rotation117 = NXOpen.Matrix3x3()
    
    rotation117.Xx = 1.0
    rotation117.Xy = 7.5183997758165618e-16
    rotation117.Xz = 1.6660162510034505e-15
    rotation117.Yx = 7.0222281005986713e-16
    rotation117.Yy = 0.70710678118654835
    rotation117.Yz = -0.70710678118654702
    rotation117.Zx = -1.6865683547175148e-15
    rotation117.Zy = 0.70710678118654746
    rotation117.Zz = 0.70710678118654824
    componentNetwork11.DragByTransform(translation136, rotation117)
    
    translation137 = NXOpen.Vector3d(-4.2632564145606011e-14, 17.333654009055223, -5.6238229865183911)
    rotation118 = NXOpen.Matrix3x3()
    
    rotation118.Xx = 1.0
    rotation118.Xy = 6.0636244196577177e-16
    rotation118.Xz = 1.5168810976978535e-15
    rotation118.Yx = 5.612585038346318e-16
    rotation118.Yy = 0.76604444311897868
    rotation118.Yz = -0.64278760968653881
    rotation118.Zx = -1.5332975886257743e-15
    rotation118.Zy = 0.64278760968653914
    rotation118.Zz = 0.76604444311897868
    componentNetwork11.DragByTransform(translation137, rotation118)
    
    translation138 = NXOpen.Vector3d(-2.8421709430404007e-14, 15.009653529968691, -5.604539120921423)
    rotation119 = NXOpen.Matrix3x3()
    
    rotation119.Xx = 1.0
    rotation119.Xy = 4.7443647734990986e-16
    rotation119.Xz = 1.3556342460060169e-15
    rotation119.Yx = 4.341890368130996e-16
    rotation119.Yy = 0.81915204428899235
    rotation119.Yz = -0.5735764363510456
    rotation119.Zx = -1.3683242152627531e-15
    rotation119.Zy = 0.57357643635104594
    rotation119.Zz = 0.81915204428899224
    componentNetwork11.DragByTransform(translation138, rotation119)
    
    translation139 = NXOpen.Vector3d(-2.8421709430404007e-14, 12.696177273969159, -5.3827786483543072)
    rotation120 = NXOpen.Matrix3x3()
    
    rotation120.Xx = 1.0
    rotation120.Xy = 3.5706611998387214e-16
    rotation120.Xz = 1.1835028818328263e-15
    rotation120.Yx = 3.2198148436594544e-16
    rotation120.Yy = 0.86602540378443915
    rotation120.Yz = -0.49999999999999967
    rotation120.Zx = -1.192903781613391e-15
    rotation120.Zy = 0.49999999999999983
    rotation120.Zz = 0.86602540378443915
    componentNetwork11.DragByTransform(translation139, rotation120)
    
    translation140 = NXOpen.Vector3d(-2.8421709430404007e-14, 10.410832192279944, -4.9602292999159161)
    rotation121 = NXOpen.Matrix3x3()
    
    rotation121.Xx = 1.0
    rotation121.Xy = 2.5514462915737388e-16
    rotation121.Xz = 1.0017970287953995e-15
    rotation121.Yx = 2.2548981372006576e-16
    rotation121.Yy = 0.90630778703665038
    rotation121.Yz = -0.42261826174069916
    rotation121.Zx = -1.008371343099513e-15
    rotation121.Zy = 0.42261826174069927
    rotation121.Zz = 0.90630778703665038
    componentNetwork11.DragByTransform(translation140, rotation121)
    
    translation141 = NXOpen.Vector3d(-1.4210854715202004e-14, 8.1710111409017863, -4.3401069312901441)
    rotation122 = NXOpen.Matrix3x3()
    
    rotation122.Xx = 1.0
    rotation122.Xy = 1.6944768895748407e-16
    rotation122.Xz = 8.1189957815234489e-16
    rotation122.Yx = 1.4544838475233901e-16
    rotation122.Yy = 0.93969262078590887
    rotation122.Yz = -0.34202014332566849
    rotation122.Zx = -8.161313030019426e-16
    rotation122.Zy = 0.34202014332566866
    rotation122.Zz = 0.93969262078590887
    componentNetwork11.DragByTransform(translation141, rotation122)
    
    translation142 = NXOpen.Vector3d(-1.4210854715202004e-14, 5.9937605104766014, -3.5271310481423441)
    rotation123 = NXOpen.Matrix3x3()
    
    rotation123.Xx = 1.0
    rotation123.Xy = 1.0062750484435013e-16
    rotation123.Xz = 6.1525576416627188e-16
    rotation123.Yx = 8.2466361067546335e-17
    rotation123.Yy = 0.96592582628906876
    rotation123.Yz = -0.25881904510252052
    rotation123.Zx = -6.1764672410353244e-16
    rotation123.Zy = 0.25881904510252068
    rotation123.Zz = 0.96592582628906876
    componentNetwork11.DragByTransform(translation142, rotation123)
    
    translation143 = NXOpen.Vector3d(0.0, 3.8956504929618045, -2.5274888878315416)
    rotation124 = NXOpen.Matrix3x3()
    
    rotation124.Xx = 1.0
    rotation124.Xy = 4.9207839973836895e-17
    rotation124.Xz = 4.1336216499839583e-16
    rotation124.Yx = 3.7023073895513674e-17
    rotation124.Yy = 0.98480775301220858
    rotation124.Yz = -0.17364817766693022
    rotation124.Zx = -4.1442819389796456e-16
    rotation124.Zy = 0.17364817766693028
    rotation124.Zz = 0.98480775301220846
    componentNetwork11.DragByTransform(translation143, rotation124)
    
    translation144 = NXOpen.Vector3d(0.0, 1.8926489724641424, -1.3487883307981363)
    rotation125 = NXOpen.Matrix3x3()
    
    rotation125.Xx = 1.0
    rotation125.Xy = 1.5580029043651444e-17
    rotation125.Xz = 2.0775531284507242e-16
    rotation125.Yx = 9.4643740910278838e-18
    rotation125.Yy = 0.99619469809174599
    rotation125.Yz = -0.08715574274765811
    rotation125.Zx = -2.0802232810680714e-16
    rotation125.Zy = 0.08715574274765811
    rotation125.Zz = 0.99619469809174599
    componentNetwork11.DragByTransform(translation144, rotation125)
    
    translation145 = NXOpen.Vector3d(0.0, -7.1054273576010019e-15, -7.1054273576010019e-15)
    rotation126 = NXOpen.Matrix3x3()
    
    rotation126.Xx = 1.0
    rotation126.Xy = 0.0
    rotation126.Xz = -9.8607613152626476e-32
    rotation126.Yx = -1.1832913578315177e-30
    rotation126.Yy = 1.0000000000000004
    rotation126.Yz = 0.0
    rotation126.Zx = 9.8607613152626476e-32
    rotation126.Zy = 0.0
    rotation126.Zz = 1.0000000000000004
    componentNetwork11.DragByTransform(translation145, rotation126)
    
    translation146 = NXOpen.Vector3d(1.4210854715202004e-14, -1.767892222937494, 1.5086110109448114)
    rotation127 = NXOpen.Matrix3x3()
    
    rotation127.Xx = 1.0
    rotation127.Xy = 2.5863262713832379e-18
    rotation127.Xz = -2.0832263015998229e-16
    rotation127.Yx = 8.7019812240052204e-18
    rotation127.Yy = 0.99619469809174588
    rotation127.Yz = 0.087155742747658138
    rotation127.Zx = 2.0805561489824826e-16
    rotation127.Zy = -0.087155742747658138
    rotation127.Zz = 0.99619469809174588
    componentNetwork11.DragByTransform(translation146, rotation127)
    
    translation147 = NXOpen.Vector3d(0.0, -7.1054273576010019e-15, -3.5527136788005009e-15)
    rotation128 = NXOpen.Matrix3x3()
    
    rotation128.Xx = 1.0
    rotation128.Xy = 0.0
    rotation128.Xz = -9.8607613152626476e-32
    rotation128.Yx = -7.8886090522101181e-31
    rotation128.Yy = 1.0000000000000004
    rotation128.Yz = 5.5511151231257827e-17
    rotation128.Zx = 1.9721522630525295e-31
    rotation128.Zy = -5.5511151231257827e-17
    rotation128.Zz = 1.0000000000000004
    componentNetwork11.DragByTransform(translation147, rotation128)
    
    translation148 = NXOpen.Vector3d(0.0, 3.8956504929618028, -2.5274888878315416)
    rotation129 = NXOpen.Matrix3x3()
    
    rotation129.Xx = 1.0
    rotation129.Xy = 4.92078399738365e-17
    rotation129.Xz = 4.1336216499839573e-16
    rotation129.Yx = 3.7023073895513674e-17
    rotation129.Yy = 0.98480775301220858
    rotation129.Yz = -0.17364817766693019
    rotation129.Zx = -4.1442819389796456e-16
    rotation129.Zy = 0.17364817766693028
    rotation129.Zz = 0.98480775301220846
    componentNetwork11.DragByTransform(translation148, rotation129)
    
    translation149 = NXOpen.Vector3d(-1.4210854715202004e-14, 5.9937605104766014, -3.5271310481423441)
    rotation130 = NXOpen.Matrix3x3()
    
    rotation130.Xx = 1.0
    rotation130.Xy = 1.0062750484434973e-16
    rotation130.Xz = 6.1525576416627178e-16
    rotation130.Yx = 8.246636106754594e-17
    rotation130.Yy = 0.96592582628906876
    rotation130.Yz = -0.25881904510252052
    rotation130.Zx = -6.1764672410353244e-16
    rotation130.Zy = 0.25881904510252068
    rotation130.Zz = 0.96592582628906876
    componentNetwork11.DragByTransform(translation149, rotation130)
    
    translation150 = NXOpen.Vector3d(-1.4210854715202004e-14, 8.1710111409017845, -4.3401069312901441)
    rotation131 = NXOpen.Matrix3x3()
    
    rotation131.Xx = 1.0
    rotation131.Xy = 1.6944768895748407e-16
    rotation131.Xz = 8.1189957815234479e-16
    rotation131.Yx = 1.4544838475233901e-16
    rotation131.Yy = 0.93969262078590887
    rotation131.Yz = -0.34202014332566844
    rotation131.Zx = -8.161313030019426e-16
    rotation131.Zy = 0.34202014332566866
    rotation131.Zz = 0.93969262078590887
    componentNetwork11.DragByTransform(translation150, rotation131)
    
    translation151 = NXOpen.Vector3d(-2.8421709430404007e-14, 10.410832192279941, -4.9602292999159197)
    rotation132 = NXOpen.Matrix3x3()
    
    rotation132.Xx = 1.0
    rotation132.Xy = 2.5514462915737388e-16
    rotation132.Xz = 1.0017970287953995e-15
    rotation132.Yx = 2.2548981372006537e-16
    rotation132.Yy = 0.90630778703665049
    rotation132.Yz = -0.42261826174069916
    rotation132.Zx = -1.008371343099513e-15
    rotation132.Zy = 0.42261826174069933
    rotation132.Zz = 0.90630778703665049
    componentNetwork11.DragByTransform(translation151, rotation132)
    
    translation152 = NXOpen.Vector3d(-2.8421709430404007e-14, 12.696177273969159, -5.3827786483543107)
    rotation133 = NXOpen.Matrix3x3()
    
    rotation133.Xx = 1.0
    rotation133.Xy = 3.5706611998387214e-16
    rotation133.Xz = 1.1835028818328263e-15
    rotation133.Yx = 3.2198148436594505e-16
    rotation133.Yy = 0.86602540378443937
    rotation133.Yz = -0.49999999999999967
    rotation133.Zx = -1.1929037816133912e-15
    rotation133.Zy = 0.49999999999999989
    rotation133.Zz = 0.86602540378443926
    componentNetwork11.DragByTransform(translation152, rotation133)
    
    translation153 = NXOpen.Vector3d(-4.2632564145606011e-14, 17.333654009055223, -5.6238229865183946)
    rotation134 = NXOpen.Matrix3x3()
    
    rotation134.Xx = 1.0
    rotation134.Xy = 6.0636244196577177e-16
    rotation134.Xz = 1.5168810976978535e-15
    rotation134.Yx = 5.6125850383463141e-16
    rotation134.Yy = 0.7660444431189789
    rotation134.Yz = -0.64278760968653903
    rotation134.Zx = -1.5332975886257745e-15
    rotation134.Zy = 0.64278760968653925
    rotation134.Zz = 0.76604444311897879
    componentNetwork11.DragByTransform(translation153, rotation134)
    
    translation154 = NXOpen.Vector3d(-4.2632564145606011e-14, 19.650491664313055, -5.4404834832841082)
    rotation135 = NXOpen.Matrix3x3()
    
    rotation135.Xx = 1.0
    rotation135.Xy = 7.5183997758165618e-16
    rotation135.Xz = 1.6660162510034505e-15
    rotation135.Yx = 7.0222281005986635e-16
    rotation135.Yy = 0.70710678118654846
    rotation135.Yz = -0.70710678118654724
    rotation135.Zx = -1.6865683547175154e-15
    rotation135.Zy = 0.70710678118654757
    rotation135.Zz = 0.70710678118654835
    componentNetwork11.DragByTransform(translation154, rotation135)
    
    translation155 = NXOpen.Vector3d(-4.2632564145606011e-14, 21.942533962240848, -5.0559159355416057)
    rotation136 = NXOpen.Matrix3x3()
    
    rotation136.Xx = 1.0
    rotation136.Xy = 9.0976191230978874e-16
    rotation136.Xz = 1.8019046973558845e-15
    rotation136.Yx = 8.5600913200185528e-16
    rotation136.Yy = 0.64278760968654036
    rotation136.Yz = -0.7660444431189779
    rotation136.Zx = -1.8269700304605991e-15
    rotation136.Zy = 0.76604444311897812
    rotation136.Zz = 0.64278760968654025
    componentNetwork11.DragByTransform(translation155, rotation136)
    
    translation156 = NXOpen.Vector3d(-5.6843418860808015e-14, 24.19233707697839, -4.4730471345374276)
    rotation137 = NXOpen.Matrix3x3()
    
    rotation137.Xx = 1.0
    rotation137.Xy = 1.0789263648710171e-15
    rotation137.Xz = 1.9235122436267264e-15
    rotation137.Yx = 1.0214470628918996e-15
    rotation137.Yy = 0.57357643635104716
    rotation137.Yz = -0.81915204428899169
    rotation137.Zx = -1.9534340743257708e-15
    rotation137.Zy = 0.81915204428899191
    rotation137.Zz = 0.57357643635104705
    componentNetwork11.DragByTransform(translation156, rotation137)
    
    translation157 = NXOpen.Vector3d(-5.6843418860808015e-14, 26.382778648354275, -3.6963130637930277)
    rotation138 = NXOpen.Matrix3x3()
    
    rotation138.Xx = 1.0
    rotation138.Xy = 1.2580458916370605e-15
    rotation138.Xz = 2.0299133829602113e-15
    rotation138.Yx = 1.1972775201817714e-15
    rotation138.Yy = 0.50000000000000111
    rotation138.Yz = -0.86602540378443837
    rotation138.Zx = -2.0649980185781395e-15
    rotation138.Zy = 0.86602540378443882
    rotation138.Zz = 0.50000000000000111
    componentNetwork11.DragByTransform(translation157, rotation138)
    
    translation158 = NXOpen.Vector3d(-5.6843418860808015e-14, 28.497188093385539, -2.7316251385916246)
    rotation139 = NXOpen.Matrix3x3()
    
    rotation139.Xx = 1.0
    rotation139.Xy = 1.4457572848539021e-15
    rotation139.Xz = 2.1202983384392463e-15
    rotation139.Yx = 1.3821623279221624e-15
    rotation139.Yy = 0.42261826174070066
    rotation139.Yz = -0.90630778703664983
    rotation139.Zx = -2.1608127942377931e-15
    rotation139.Zy = 0.90630778703665027
    rotation139.Zz = 0.42261826174070055
    componentNetwork11.DragByTransform(translation158, rotation139)
    
    translation159 = NXOpen.Vector3d(-5.6843418860808015e-14, 30.519473479480169, -1.5863252165384978)
    rotation140 = NXOpen.Matrix3x3()
    
    rotation140.Xx = 1.0
    rotation140.Xy = 1.6406319474759242e-15
    rotation140.Xz = 2.1939792259767076e-15
    rotation140.Yx = 1.5746944010896695e-15
    rotation140.Yy = 0.34202014332566988
    rotation140.Yz = -0.93969262078590843
    rotation140.Zx = -2.2401491930074179e-15
    rotation140.Zy = 0.93969262078590865
    rotation140.Zz = 0.34202014332566988
    componentNetwork11.DragByTransform(translation159, rotation140)
    
    translation160 = NXOpen.Vector3d(-7.1054273576010019e-14, 32.434243993760681, -0.26912972159147586)
    rotation141 = NXOpen.Matrix3x3()
    
    rotation141.Xx = 1.0
    rotation141.Xy = 1.8411867656520346e-15
    rotation141.Xz = 2.2503952895286995e-15
    rotation141.Yx = 1.7734084543534423e-15
    rotation141.Yy = 0.25881904510252202
    rotation141.Yz = -0.96592582628906831
    rotation141.Zx = -2.3024034169877507e-15
    rotation141.Zy = 0.96592582628906887
    rotation141.Zz = 0.25881904510252196
    componentNetwork11.DragByTransform(translation160, rotation141)
    
    translation161 = NXOpen.Vector3d(-5.6843418860808015e-14, 30.519473479480169, -1.5863252165385013)
    rotation142 = NXOpen.Matrix3x3()
    
    rotation142.Xx = 1.0
    rotation142.Xy = 1.6406319474759242e-15
    rotation142.Xz = 2.1939792259767076e-15
    rotation142.Yx = 1.5746944010896695e-15
    rotation142.Yy = 0.34202014332566988
    rotation142.Yz = -0.93969262078590843
    rotation142.Zx = -2.2401491930074183e-15
    rotation142.Zy = 0.93969262078590876
    rotation142.Zz = 0.34202014332566988
    componentNetwork11.DragByTransform(translation161, rotation142)
    
    translation162 = NXOpen.Vector3d(-5.6843418860808015e-14, 28.497188093385542, -2.7316251385916281)
    rotation143 = NXOpen.Matrix3x3()
    
    rotation143.Xx = 1.0
    rotation143.Xy = 1.4457572848539019e-15
    rotation143.Xz = 2.1202983384392463e-15
    rotation143.Yx = 1.3821623279221628e-15
    rotation143.Yy = 0.42261826174070061
    rotation143.Yz = -0.90630778703664994
    rotation143.Zx = -2.1608127942377931e-15
    rotation143.Zy = 0.90630778703665049
    rotation143.Zz = 0.4226182617407005
    componentNetwork11.DragByTransform(translation162, rotation143)
    
    translation163 = NXOpen.Vector3d(-5.6843418860808015e-14, 26.382778648354275, -3.6963130637930313)
    rotation144 = NXOpen.Matrix3x3()
    
    rotation144.Xx = 1.0
    rotation144.Xy = 1.2580458916370603e-15
    rotation144.Xz = 2.0299133829602113e-15
    rotation144.Yx = 1.1972775201817714e-15
    rotation144.Yy = 0.50000000000000111
    rotation144.Yz = -0.8660254037844386
    rotation144.Zx = -2.0649980185781395e-15
    rotation144.Zy = 0.86602540378443904
    rotation144.Zz = 0.50000000000000111
    componentNetwork11.DragByTransform(translation163, rotation144)
    
    translation164 = NXOpen.Vector3d(-5.6843418860808015e-14, 24.192337076978394, -4.4730471345374241)
    rotation145 = NXOpen.Matrix3x3()
    
    rotation145.Xx = 1.0
    rotation145.Xy = 1.0789263648710167e-15
    rotation145.Xz = 1.9235122436267268e-15
    rotation145.Yx = 1.0214470628918996e-15
    rotation145.Yy = 0.57357643635104705
    rotation145.Yz = -0.81915204428899169
    rotation145.Zx = -1.9534340743257712e-15
    rotation145.Zy = 0.81915204428899202
    rotation145.Zz = 0.57357643635104694
    componentNetwork11.DragByTransform(translation164, rotation145)
    
    translation165 = NXOpen.Vector3d(-4.2632564145606011e-14, 21.942533962240852, -5.0559159355416057)
    rotation146 = NXOpen.Matrix3x3()
    
    rotation146.Xx = 1.0
    rotation146.Xy = 9.0976191230978874e-16
    rotation146.Xz = 1.8019046973558849e-15
    rotation146.Yx = 8.5600913200185528e-16
    rotation146.Yy = 0.64278760968654036
    rotation146.Yz = -0.7660444431189779
    rotation146.Zx = -1.8269700304605995e-15
    rotation146.Zy = 0.76604444311897812
    rotation146.Zz = 0.64278760968654014
    componentNetwork11.DragByTransform(translation165, rotation146)
    
    translation166 = NXOpen.Vector3d(-4.2632564145606011e-14, 19.650491664313058, -5.4404834832841154)
    rotation147 = NXOpen.Matrix3x3()
    
    rotation147.Xx = 1.0
    rotation147.Xy = 7.5183997758165579e-16
    rotation147.Xz = 1.6660162510034509e-15
    rotation147.Yx = 7.0222281005986674e-16
    rotation147.Yy = 0.70710678118654857
    rotation147.Yz = -0.70710678118654746
    rotation147.Zx = -1.6865683547175156e-15
    rotation147.Zy = 0.70710678118654768
    rotation147.Zz = 0.70710678118654835
    componentNetwork11.DragByTransform(translation166, rotation147)
    
    translation167 = NXOpen.Vector3d(-4.2632564145606011e-14, 17.333654009055223, -5.6238229865184017)
    rotation148 = NXOpen.Matrix3x3()
    
    rotation148.Xx = 1.0
    rotation148.Xy = 6.0636244196577137e-16
    rotation148.Xz = 1.5168810976978539e-15
    rotation148.Yx = 5.6125850383463102e-16
    rotation148.Yy = 0.76604444311897901
    rotation148.Yz = -0.64278760968653925
    rotation148.Zx = -1.533297588625775e-15
    rotation148.Zy = 0.64278760968653947
    rotation148.Zz = 0.76604444311897879
    componentNetwork11.DragByTransform(translation167, rotation148)
    
    translation168 = NXOpen.Vector3d(-2.8421709430404007e-14, 15.009653529968695, -5.6045391209214301)
    rotation149 = NXOpen.Matrix3x3()
    
    rotation149.Xx = 1.0
    rotation149.Xy = 4.7443647734990907e-16
    rotation149.Xz = 1.3556342460060173e-15
    rotation149.Yx = 4.3418903681309881e-16
    rotation149.Yy = 0.81915204428899258
    rotation149.Yz = -0.57357643635104594
    rotation149.Zx = -1.3683242152627539e-15
    rotation149.Zy = 0.57357643635104627
    rotation149.Zz = 0.81915204428899246
    componentNetwork11.DragByTransform(translation168, rotation149)
    
    translation169 = NXOpen.Vector3d(-2.8421709430404007e-14, 12.696177273969163, -5.3827786483543143)
    rotation150 = NXOpen.Matrix3x3()
    
    rotation150.Xx = 1.0
    rotation150.Xy = 3.5706611998387135e-16
    rotation150.Xz = 1.1835028818328267e-15
    rotation150.Yx = 3.2198148436594465e-16
    rotation150.Yy = 0.86602540378443948
    rotation150.Yz = -0.49999999999999989
    rotation150.Zx = -1.1929037816133916e-15
    rotation150.Zy = 0.50000000000000022
    rotation150.Zz = 0.86602540378443926
    componentNetwork11.DragByTransform(translation169, rotation150)
    
    translation170 = NXOpen.Vector3d(-2.8421709430404007e-14, 10.410832192279944, -4.9602292999159232)
    rotation151 = NXOpen.Matrix3x3()
    
    rotation151.Xx = 1.0
    rotation151.Xy = 2.5514462915737309e-16
    rotation151.Xz = 1.0017970287953997e-15
    rotation151.Yx = 2.2548981372006537e-16
    rotation151.Yy = 0.90630778703665071
    rotation151.Yz = -0.42261826174069939
    rotation151.Zx = -1.0083713430995136e-15
    rotation151.Zy = 0.42261826174069961
    rotation151.Zz = 0.90630778703665049
    componentNetwork11.DragByTransform(translation170, rotation151)
    
    translation171 = NXOpen.Vector3d(-1.4210854715202004e-14, 8.1710111409017863, -4.3401069312901477)
    rotation152 = NXOpen.Matrix3x3()
    
    rotation152.Xx = 1.0
    rotation152.Xy = 1.6944768895748328e-16
    rotation152.Xz = 8.1189957815234509e-16
    rotation152.Yx = 1.4544838475233862e-16
    rotation152.Yy = 0.93969262078590909
    rotation152.Yz = -0.34202014332566871
    rotation152.Zx = -8.1613130300194319e-16
    rotation152.Zy = 0.34202014332566888
    rotation152.Zz = 0.93969262078590909
    componentNetwork11.DragByTransform(translation171, rotation152)
    
    translation172 = NXOpen.Vector3d(-1.4210854715202004e-14, 5.9937605104766014, -3.5271310481423512)
    rotation153 = NXOpen.Matrix3x3()
    
    rotation153.Xx = 1.0
    rotation153.Xy = 1.0062750484434894e-16
    rotation153.Xz = 6.1525576416627207e-16
    rotation153.Yx = 8.246636106754594e-17
    rotation153.Yy = 0.96592582628906898
    rotation153.Yz = -0.25881904510252074
    rotation153.Zx = -6.1764672410353303e-16
    rotation153.Zy = 0.25881904510252091
    rotation153.Zz = 0.96592582628906887
    componentNetwork11.DragByTransform(translation172, rotation153)
    
    translation173 = NXOpen.Vector3d(0.0, 3.8956504929618045, -2.5274888878315487)
    rotation154 = NXOpen.Matrix3x3()
    
    rotation154.Xx = 1.0
    rotation154.Xy = 4.9207839973836106e-17
    rotation154.Xz = 4.1336216499839583e-16
    rotation154.Yx = 3.7023073895512885e-17
    rotation154.Yy = 0.98480775301220869
    rotation154.Yz = -0.17364817766693036
    rotation154.Zx = -4.1442819389796515e-16
    rotation154.Zy = 0.17364817766693055
    rotation154.Zz = 0.98480775301220858
    componentNetwork11.DragByTransform(translation173, rotation154)
    
    translation174 = NXOpen.Vector3d(0.0, 1.8926489724641424, -1.3487883307981399)
    rotation155 = NXOpen.Matrix3x3()
    
    rotation155.Xx = 1.0
    rotation155.Xy = 1.5580029043650655e-17
    rotation155.Xz = 2.0775531284507232e-16
    rotation155.Yx = 9.4643740910274894e-18
    rotation155.Yy = 0.99619469809174621
    rotation155.Yz = -0.087155742747658221
    rotation155.Zx = -2.0802232810680764e-16
    rotation155.Zy = 0.087155742747658388
    rotation155.Zz = 0.99619469809174621
    componentNetwork11.DragByTransform(translation174, rotation155)
    
    translation175 = NXOpen.Vector3d(0.0, -7.1054273576010019e-15, -1.4210854715202004e-14)
    rotation156 = NXOpen.Matrix3x3()
    
    rotation156.Xx = 1.0
    rotation156.Xy = -3.944304526105059e-31
    rotation156.Xz = -1.9721522630525295e-31
    rotation156.Yx = -1.5777218104420236e-30
    rotation156.Yy = 1.0000000000000007
    rotation156.Yz = -1.1102230246251565e-16
    rotation156.Zx = -4.9303806576313238e-31
    rotation156.Zy = 2.2204460492503131e-16
    rotation156.Zz = 1.0000000000000007
    componentNetwork11.DragByTransform(translation175, rotation156)
    
    translation176 = NXOpen.Vector3d(1.4210854715202004e-14, -1.7678922229374976, 1.5086110109448008)
    rotation157 = NXOpen.Matrix3x3()
    
    rotation157.Xx = 1.0
    rotation157.Xy = 2.5863262713828434e-18
    rotation157.Xz = -2.0832263015998298e-16
    rotation157.Yx = 8.7019812240044315e-18
    rotation157.Yy = 0.9961946980917461
    rotation157.Yz = 0.087155742747658027
    rotation157.Zx = 2.0805561489824776e-16
    rotation157.Zy = -0.087155742747657916
    rotation157.Zz = 0.99619469809174621
    componentNetwork11.DragByTransform(translation176, rotation157)
    
    translation177 = NXOpen.Vector3d(1.4210854715202004e-14, -3.3975729690492642, 3.1655632613187805)
    rotation158 = NXOpen.Matrix3x3()
    
    rotation158.Xx = 1.0
    rotation158.Xy = 2.3319324353209271e-17
    rotation158.Xz = -4.1562711663071496e-16
    rotation158.Yx = 3.5504090431530915e-17
    rotation158.Yy = 0.9848077530122088
    rotation158.Yz = 0.17364817766693019
    rotation158.Zx = 4.1456108773114618e-16
    rotation158.Zy = -0.17364817766693014
    rotation158.Zz = 0.9848077530122088
    componentNetwork11.DragByTransform(translation177, rotation158)
    
    translation178 = NXOpen.Vector3d(1.4210854715202004e-14, -1.7678922229374976, 1.5086110109448008)
    rotation159 = NXOpen.Matrix3x3()
    
    rotation159.Xx = 1.0
    rotation159.Xy = 2.5863262713828434e-18
    rotation159.Xz = -2.0832263015998298e-16
    rotation159.Yx = 8.7019812240044315e-18
    rotation159.Yy = 0.99619469809174621
    rotation159.Yz = 0.087155742747658083
    rotation159.Zx = 2.0805561489824767e-16
    rotation159.Zy = -0.087155742747657972
    rotation159.Zz = 0.99619469809174632
    componentNetwork11.DragByTransform(translation178, rotation159)
    
    translation179 = NXOpen.Vector3d(0.0, -1.0658141036401503e-14, -1.4210854715202004e-14)
    rotation160 = NXOpen.Matrix3x3()
    
    rotation160.Xx = 1.0
    rotation160.Xy = -3.944304526105059e-31
    rotation160.Xz = -4.9303806576313238e-31
    rotation160.Yx = -1.5777218104420236e-30
    rotation160.Yy = 1.0000000000000007
    rotation160.Yz = 0.0
    rotation160.Zx = -4.9303806576313238e-31
    rotation160.Zy = 2.2204460492503131e-16
    rotation160.Zz = 1.0000000000000007
    componentNetwork11.DragByTransform(translation179, rotation160)
    
    translation180 = NXOpen.Vector3d(0.0, 1.8926489724641407, -1.3487883307981399)
    rotation161 = NXOpen.Matrix3x3()
    
    rotation161.Xx = 1.0
    rotation161.Xy = 1.5580029043651444e-17
    rotation161.Xz = 2.0775531284507173e-16
    rotation161.Yx = 9.4643740910274894e-18
    rotation161.Yy = 0.99619469809174621
    rotation161.Yz = -0.087155742747658138
    rotation161.Zx = -2.0802232810680764e-16
    rotation161.Zy = 0.087155742747658388
    rotation161.Zz = 0.99619469809174621
    componentNetwork11.DragByTransform(translation180, rotation161)
    
    translation181 = NXOpen.Vector3d(0.0, 3.8956504929617992, -2.5274888878315522)
    rotation162 = NXOpen.Matrix3x3()
    
    rotation162.Xx = 1.0
    rotation162.Xy = 4.92078399738365e-17
    rotation162.Xz = 4.1336216499839519e-16
    rotation162.Yx = 3.7023073895512885e-17
    rotation162.Yy = 0.9848077530122088
    rotation162.Yz = -0.1736481776669303
    rotation162.Zx = -4.144281938979653e-16
    rotation162.Zy = 0.17364817766693058
    rotation162.Zz = 0.98480775301220869
    componentNetwork11.DragByTransform(translation181, rotation162)
    
    translation182 = NXOpen.Vector3d(-1.4210854715202004e-14, 5.9937605104765996, -3.5271310481423548)
    rotation163 = NXOpen.Matrix3x3()
    
    rotation163.Xx = 1.0
    rotation163.Xy = 1.0062750484434973e-16
    rotation163.Xz = 6.1525576416627119e-16
    rotation163.Yx = 8.2466361067545546e-17
    rotation163.Yy = 0.96592582628906909
    rotation163.Yz = -0.25881904510252074
    rotation163.Zx = -6.1764672410353303e-16
    rotation163.Zy = 0.25881904510252102
    rotation163.Zz = 0.96592582628906887
    componentNetwork11.DragByTransform(translation182, rotation163)
    
    translation183 = NXOpen.Vector3d(-1.4210854715202004e-14, 8.1710111409017827, -4.3401069312901548)
    rotation164 = NXOpen.Matrix3x3()
    
    rotation164.Xx = 1.0
    rotation164.Xy = 1.6944768895748368e-16
    rotation164.Xz = 8.118995781523442e-16
    rotation164.Yx = 1.4544838475233822e-16
    rotation164.Yy = 0.93969262078590932
    rotation164.Yz = -0.34202014332566866
    rotation164.Zx = -8.1613130300194359e-16
    rotation164.Zy = 0.34202014332566899
    rotation164.Zz = 0.93969262078590921
    componentNetwork11.DragByTransform(translation183, rotation164)
    
    translation184 = NXOpen.Vector3d(-1.4210854715202004e-14, 8.1710111409017827, -4.3401069312901548)
    rotation165 = NXOpen.Matrix3x3()
    
    rotation165.Xx = 1.0
    rotation165.Xy = 1.6944768895748368e-16
    rotation165.Xz = 8.118995781523442e-16
    rotation165.Yx = 1.4544838475233822e-16
    rotation165.Yy = 0.93969262078590932
    rotation165.Yz = -0.34202014332566866
    rotation165.Zx = -8.1613130300194359e-16
    rotation165.Zy = 0.34202014332566899
    rotation165.Zz = 0.93969262078590921
    componentNetwork11.DragByTransform(translation184, rotation165)
    
    componentNetwork11.EndDrag()
    
    componentNetwork11.ResetDisplay()
    
    componentNetwork11.ApplyToModel()
    
    componentNetwork11.Solve()
    
    componentPositioner11.ClearNetwork()
    
    nErrs26 = theSession.UpdateManager.AddToDeleteList(componentNetwork11)
    
    componentPositioner11.DeleteNonPersistentConstraints()
    
    nErrs27 = theSession.UpdateManager.DoUpdate(markId60)
    
    theSession.SetUndoMarkName(markId59, "Move Component")
    
    componentPositioner11.EndMoveComponent()
    
    componentPositioner11.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMarksUpToMark(markId60, None, False)
    
    scaleAboutPoint46 = NXOpen.Point3d(-4.3654779022513495, -70.575226086397748, 0.0)
    viewCenter46 = NXOpen.Point3d(4.3654779022514525, 70.575226086397919, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint46, viewCenter46)
    
    scaleAboutPoint47 = NXOpen.Point3d(-3.4923823218010792, -56.65420210921824, 0.0)
    viewCenter47 = NXOpen.Point3d(3.4923823218011787, 56.654202109218403, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint47, viewCenter47)
    
    scaleAboutPoint48 = NXOpen.Point3d(-2.7939058574408504, -45.633795671534678, 0.0)
    viewCenter48 = NXOpen.Point3d(2.7939058574409299, 45.633795671534848, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint48, viewCenter48)
    
    scaleAboutPoint49 = NXOpen.Point3d(-2.1109510922886576, -36.755383724555799, 0.0)
    viewCenter49 = NXOpen.Point3d(2.1109510922887211, 36.755383724555962, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint49, viewCenter49)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Move Component...
    # ----------------------------------------------
    markId64 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner12 = workPart.ComponentAssembly.Positioner
    
    componentPositioner12.ClearNetwork()
    
    componentPositioner12.PrimaryArrangement = arrangement1
    
    componentPositioner12.BeginMoveComponent()
    
    allowInterpartPositioning11 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression110 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression111 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression112 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression113 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression114 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression115 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression116 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression117 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network12 = componentPositioner12.EstablishNetwork()
    
    componentNetwork12 = network12
    componentNetwork12.MoveObjectsState = True
    
    componentNetwork12.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork12.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    expression118 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression119 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression120 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression121 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression122 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    componentNetwork12.RemoveAllConstraints()
    
    movableObjects9 = [NXOpen.NXObject.Null] * 1 
    movableObjects9[0] = component4
    componentNetwork12.SetMovingGroup(movableObjects9)
    
    componentNetwork12.Solve()
    
    theSession.SetUndoMarkName(markId64, "Move Component Dialog")
    
    componentNetwork12.MoveObjectsState = True
    
    componentNetwork12.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId65 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component Update")
    
    markId66 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Rotate About X-axis")
    
    loaded11 = componentNetwork12.IsReferencedGeometryLoaded()
    
    componentNetwork12.BeginDrag()
    
    translation185 = NXOpen.Vector3d(-1.5678055020811996, 1.9396206755268155, 5.7300300802798265)
    rotation166 = NXOpen.Matrix3x3()
    
    rotation166.Xx = 0.99619469809174555
    rotation166.Xy = 0.027944717503611275
    rotation166.Xz = 0.082554323069959953
    rotation166.Yx = -0.027944717503611261
    rotation166.Yy = 0.99960880206870439
    rotation166.Yz = -0.0011556774692855201
    rotation166.Zx = -0.082554323069959898
    rotation166.Zy = -0.0011556774692855906
    rotation166.Zz = 0.99658589602304104
    componentNetwork12.DragByTransform(translation185, rotation166)
    
    translation186 = NXOpen.Vector3d(-1.5678055020811996, 1.9396206755268155, 5.7300300802798265)
    rotation167 = NXOpen.Matrix3x3()
    
    rotation167.Xx = 0.99619469809174555
    rotation167.Xy = 0.027944717503611275
    rotation167.Xz = 0.082554323069959953
    rotation167.Yx = -0.027944717503611261
    rotation167.Yy = 0.99960880206870439
    rotation167.Yz = -0.0011556774692855201
    rotation167.Zx = -0.082554323069959898
    rotation167.Zy = -0.0011556774692855906
    rotation167.Zz = 0.99658589602304104
    componentNetwork12.DragByTransform(translation186, rotation167)
    
    translation187 = NXOpen.Vector3d(-1.5678055020811996, 1.9396206755268155, 5.7300300802798265)
    rotation168 = NXOpen.Matrix3x3()
    
    rotation168.Xx = 0.99619469809174555
    rotation168.Xy = 0.027944717503611275
    rotation168.Xz = 0.082554323069959953
    rotation168.Yx = -0.027944717503611261
    rotation168.Yy = 0.99960880206870439
    rotation168.Yz = -0.0011556774692855201
    rotation168.Zx = -0.082554323069959898
    rotation168.Zy = -0.0011556774692855906
    rotation168.Zz = 0.99658589602304104
    componentNetwork12.DragByTransform(translation187, rotation168)
    
    translation188 = NXOpen.Vector3d(-1.5678055020811996, 1.9396206755268155, 5.7300300802798265)
    rotation169 = NXOpen.Matrix3x3()
    
    rotation169.Xx = 0.99619469809174555
    rotation169.Xy = 0.027944717503611275
    rotation169.Xz = 0.082554323069959953
    rotation169.Yx = -0.027944717503611261
    rotation169.Yy = 0.99960880206870439
    rotation169.Yz = -0.0011556774692855201
    rotation169.Zx = -0.082554323069959898
    rotation169.Zy = -0.0011556774692855906
    rotation169.Zz = 0.99658589602304104
    componentNetwork12.DragByTransform(translation188, rotation169)
    
    translation189 = NXOpen.Vector3d(-1.5678055020811996, 1.9396206755268155, 5.7300300802798265)
    rotation170 = NXOpen.Matrix3x3()
    
    rotation170.Xx = 0.99619469809174555
    rotation170.Xy = 0.027944717503611275
    rotation170.Xz = 0.082554323069959953
    rotation170.Yx = -0.027944717503611261
    rotation170.Yy = 0.99960880206870439
    rotation170.Yz = -0.0011556774692855201
    rotation170.Zx = -0.082554323069959898
    rotation170.Zy = -0.0011556774692855906
    rotation170.Zz = 0.99658589602304104
    componentNetwork12.DragByTransform(translation189, rotation170)
    
    translation190 = NXOpen.Vector3d(-1.5678055020811996, 1.9396206755268155, 5.7300300802798265)
    rotation171 = NXOpen.Matrix3x3()
    
    rotation171.Xx = 0.99619469809174555
    rotation171.Xy = 0.027944717503611275
    rotation171.Xz = 0.082554323069959953
    rotation171.Yx = -0.027944717503611261
    rotation171.Yy = 0.99960880206870439
    rotation171.Yz = -0.0011556774692855201
    rotation171.Zx = -0.082554323069959898
    rotation171.Zy = -0.0011556774692855906
    rotation171.Zz = 0.99658589602304104
    componentNetwork12.DragByTransform(translation190, rotation171)
    
    translation191 = NXOpen.Vector3d(2.0890804351021188, -1.8884279514126785, -5.5787964639513064)
    rotation172 = NXOpen.Matrix3x3()
    
    rotation172.Xx = 0.99619469809174555
    rotation172.Xy = -0.027944717503611279
    rotation172.Xz = -0.082554323069959953
    rotation172.Yx = 0.027944717503611261
    rotation172.Yy = 0.99960880206870439
    rotation172.Yz = -0.0011556774692855218
    rotation172.Zx = 0.082554323069959898
    rotation172.Zy = -0.0011556774692855624
    rotation172.Zz = 0.99658589602304104
    componentNetwork12.DragByTransform(translation191, rotation172)
    
    translation192 = NXOpen.Vector3d(4.6835366396927824, -3.7112911017369914, -10.963901301914021)
    rotation173 = NXOpen.Matrix3x3()
    
    rotation173.Xx = 0.98480775301220813
    rotation173.Xy = -0.055676758833538308
    rotation173.Xz = -0.16448035789369436
    rotation173.Yx = 0.055676758833538266
    rotation173.Yy = 0.99843818552728669
    rotation173.Yz = -0.004613914473783844
    rotation173.Zx = 0.16448035789369425
    rotation173.Zy = -0.004613914473783759
    rotation173.Zz = 0.98636956748492144
    componentNetwork12.DragByTransform(translation192, rotation173)
    
    translation193 = NXOpen.Vector3d(4.6835366396927824, -3.7112911017369914, -10.963901301914021)
    rotation174 = NXOpen.Matrix3x3()
    
    rotation174.Xx = 0.98480775301220813
    rotation174.Xy = -0.055676758833538308
    rotation174.Xz = -0.16448035789369436
    rotation174.Yx = 0.055676758833538266
    rotation174.Yy = 0.99843818552728669
    rotation174.Yz = -0.004613914473783844
    rotation174.Zx = 0.16448035789369425
    rotation174.Zy = -0.004613914473783759
    rotation174.Zz = 0.98636956748492144
    componentNetwork12.DragByTransform(translation193, rotation174)
    
    translation194 = NXOpen.Vector3d(2.0890804351021188, -1.8884279514126785, -5.5787964639513064)
    rotation175 = NXOpen.Matrix3x3()
    
    rotation175.Xx = 0.99619469809174555
    rotation175.Xy = -0.027944717503611279
    rotation175.Xz = -0.082554323069959953
    rotation175.Yx = 0.027944717503611261
    rotation175.Yy = 0.99960880206870439
    rotation175.Yz = -0.0011556774692855218
    rotation175.Zx = 0.082554323069959898
    rotation175.Zy = -0.0011556774692855624
    rotation175.Zz = 0.99658589602304104
    componentNetwork12.DragByTransform(translation194, rotation175)
    
    translation195 = NXOpen.Vector3d(2.0890804351021188, -1.8884279514126785, -5.5787964639513064)
    rotation176 = NXOpen.Matrix3x3()
    
    rotation176.Xx = 0.99619469809174555
    rotation176.Xy = -0.027944717503611279
    rotation176.Xz = -0.082554323069959953
    rotation176.Yx = 0.027944717503611261
    rotation176.Yy = 0.99960880206870439
    rotation176.Yz = -0.0011556774692855218
    rotation176.Zx = 0.082554323069959898
    rotation176.Zy = -0.0011556774692855624
    rotation176.Zz = 0.99658589602304104
    componentNetwork12.DragByTransform(translation195, rotation176)
    
    translation196 = NXOpen.Vector3d(4.6835366396927824, -3.7112911017369914, -10.963901301914021)
    rotation177 = NXOpen.Matrix3x3()
    
    rotation177.Xx = 0.98480775301220813
    rotation177.Xy = -0.055676758833538308
    rotation177.Xz = -0.16448035789369436
    rotation177.Yx = 0.055676758833538266
    rotation177.Yy = 0.99843818552728669
    rotation177.Yz = -0.004613914473783844
    rotation177.Zx = 0.16448035789369425
    rotation177.Zy = -0.004613914473783759
    rotation177.Zz = 0.98636956748492144
    componentNetwork12.DragByTransform(translation196, rotation177)
    
    translation197 = NXOpen.Vector3d(4.6835366396927824, -3.7112911017369914, -10.963901301914021)
    rotation178 = NXOpen.Matrix3x3()
    
    rotation178.Xx = 0.98480775301220813
    rotation178.Xy = -0.055676758833538308
    rotation178.Xz = -0.16448035789369436
    rotation178.Yx = 0.055676758833538266
    rotation178.Yy = 0.99843818552728669
    rotation178.Yz = -0.004613914473783844
    rotation178.Zx = 0.16448035789369425
    rotation178.Zy = -0.004613914473783759
    rotation178.Zz = 0.98636956748492144
    componentNetwork12.DragByTransform(translation197, rotation178)
    
    translation198 = NXOpen.Vector3d(4.6835366396927824, -3.7112911017369914, -10.963901301914021)
    rotation179 = NXOpen.Matrix3x3()
    
    rotation179.Xx = 0.98480775301220813
    rotation179.Xy = -0.055676758833538308
    rotation179.Xz = -0.16448035789369436
    rotation179.Yx = 0.055676758833538266
    rotation179.Yy = 0.99843818552728669
    rotation179.Yz = -0.004613914473783844
    rotation179.Zx = 0.16448035789369425
    rotation179.Zy = -0.004613914473783759
    rotation179.Zz = 0.98636956748492144
    componentNetwork12.DragByTransform(translation198, rotation179)
    
    translation199 = NXOpen.Vector3d(4.6835366396927824, -3.7112911017369914, -10.963901301914021)
    rotation180 = NXOpen.Matrix3x3()
    
    rotation180.Xx = 0.98480775301220813
    rotation180.Xy = -0.055676758833538308
    rotation180.Xz = -0.16448035789369436
    rotation180.Yx = 0.055676758833538266
    rotation180.Yy = 0.99843818552728669
    rotation180.Yz = -0.004613914473783844
    rotation180.Zx = 0.16448035789369425
    rotation180.Zy = -0.004613914473783759
    rotation180.Zz = 0.98636956748492144
    componentNetwork12.DragByTransform(translation199, rotation180)
    
    translation200 = NXOpen.Vector3d(2.0890804351021188, -1.8884279514126785, -5.5787964639513064)
    rotation181 = NXOpen.Matrix3x3()
    
    rotation181.Xx = 0.99619469809174555
    rotation181.Xy = -0.027944717503611279
    rotation181.Xz = -0.082554323069959953
    rotation181.Yx = 0.027944717503611261
    rotation181.Yy = 0.99960880206870439
    rotation181.Yz = -0.0011556774692855218
    rotation181.Zx = 0.082554323069959898
    rotation181.Zy = -0.0011556774692855624
    rotation181.Zz = 0.99658589602304104
    componentNetwork12.DragByTransform(translation200, rotation181)
    
    translation201 = NXOpen.Vector3d(4.6835366396927824, -3.7112911017369914, -10.963901301914021)
    rotation182 = NXOpen.Matrix3x3()
    
    rotation182.Xx = 0.98480775301220813
    rotation182.Xy = -0.055676758833538308
    rotation182.Xz = -0.16448035789369436
    rotation182.Yx = 0.055676758833538266
    rotation182.Yy = 0.99843818552728669
    rotation182.Yz = -0.004613914473783844
    rotation182.Zx = 0.16448035789369425
    rotation182.Zy = -0.004613914473783759
    rotation182.Zz = 0.98636956748492144
    componentNetwork12.DragByTransform(translation201, rotation182)
    
    translation202 = NXOpen.Vector3d(2.0890804351021188, -1.8884279514126785, -5.5787964639513064)
    rotation183 = NXOpen.Matrix3x3()
    
    rotation183.Xx = 0.99619469809174555
    rotation183.Xy = -0.027944717503611279
    rotation183.Xz = -0.082554323069959953
    rotation183.Yx = 0.027944717503611261
    rotation183.Yy = 0.99960880206870439
    rotation183.Yz = -0.0011556774692855218
    rotation183.Zx = 0.082554323069959898
    rotation183.Zy = -0.0011556774692855624
    rotation183.Zz = 0.99658589602304104
    componentNetwork12.DragByTransform(translation202, rotation183)
    
    translation203 = NXOpen.Vector3d(2.0890804351021188, -1.8884279514126785, -5.5787964639513064)
    rotation184 = NXOpen.Matrix3x3()
    
    rotation184.Xx = 0.99619469809174555
    rotation184.Xy = -0.027944717503611279
    rotation184.Xz = -0.082554323069959953
    rotation184.Yx = 0.027944717503611261
    rotation184.Yy = 0.99960880206870439
    rotation184.Yz = -0.0011556774692855218
    rotation184.Zx = 0.082554323069959898
    rotation184.Zy = -0.0011556774692855624
    rotation184.Zz = 0.99658589602304104
    componentNetwork12.DragByTransform(translation203, rotation184)
    
    translation204 = NXOpen.Vector3d(2.0890804351021188, -1.8884279514126785, -5.5787964639513064)
    rotation185 = NXOpen.Matrix3x3()
    
    rotation185.Xx = 0.99619469809174555
    rotation185.Xy = -0.027944717503611279
    rotation185.Xz = -0.082554323069959953
    rotation185.Yx = 0.027944717503611261
    rotation185.Yy = 0.99960880206870439
    rotation185.Yz = -0.0011556774692855218
    rotation185.Zx = 0.082554323069959898
    rotation185.Zy = -0.0011556774692855624
    rotation185.Zz = 0.99658589602304104
    componentNetwork12.DragByTransform(translation204, rotation185)
    
    translation205 = NXOpen.Vector3d(0.0, 0.0, 7.1054273576010019e-15)
    rotation186 = NXOpen.Matrix3x3()
    
    rotation186.Xx = 1.0
    rotation186.Xy = 0.0
    rotation186.Xz = 0.0
    rotation186.Yx = 0.0
    rotation186.Yy = 1.0
    rotation186.Yz = -5.1798122667284395e-33
    rotation186.Zx = -6.1629758220391547e-33
    rotation186.Zy = -5.1798122667284382e-33
    rotation186.Zz = 1.0
    componentNetwork12.DragByTransform(translation205, rotation186)
    
    componentNetwork12.EndDrag()
    
    componentNetwork12.ResetDisplay()
    
    componentNetwork12.ApplyToModel()
    
    markId67 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Rotate About Z-axis")
    
    loaded12 = componentNetwork12.IsReferencedGeometryLoaded()
    
    componentNetwork12.BeginDrag()
    
    translation206 = NXOpen.Vector3d(0.0, -1.67539012083971, 0.74159039182025666)
    rotation187 = NXOpen.Matrix3x3()
    
    rotation187.Xx = 1.0
    rotation187.Xy = -2.0052282990508222e-18
    rotation187.Xz = -1.494784053630511e-17
    rotation187.Yx = 3.3003879443931835e-18
    rotation187.Yy = 0.99619469809174555
    rotation187.Yz = 0.087155742747658083
    rotation187.Zx = 1.4716192328405617e-17
    rotation187.Zy = -0.087155742747658083
    rotation187.Zz = 0.99619469809174555
    componentNetwork12.DragByTransform(translation206, rotation187)
    
    translation207 = NXOpen.Vector3d(0.0, -3.2797710150418986, 1.6263786786812453)
    rotation188 = NXOpen.Matrix3x3()
    
    rotation188.Xx = 1.0
    rotation188.Xy = -2.7000359546135169e-18
    rotation188.Xz = -3.0013567188275523e-17
    rotation188.Yx = 7.8708175890431366e-18
    rotation188.Yy = 0.98480775301220802
    rotation188.Yz = 0.17364817766693025
    rotation188.Zx = 2.9088737339412714e-17
    rotation188.Zy = -0.17364817766693025
    rotation188.Zz = 0.98480775301220802
    componentNetwork12.DragByTransform(translation207, rotation188)
    
    translation208 = NXOpen.Vector3d(0.0, -4.8009323752500119, 2.6476310874701845)
    rotation189 = NXOpen.Matrix3x3()
    
    rotation189.Xx = 1.0
    rotation189.Xy = -2.0791350608929959e-18
    rotation189.Xz = -4.5082520679155301e-17
    rotation189.Yx = 1.3676505204653243e-17
    rotation189.Yy = 0.96592582628906831
    rotation189.Yz = 0.25881904510252052
    rotation189.Zx = 4.3008251287107581e-17
    rotation189.Zy = -0.25881904510252052
    rotation189.Zz = 0.96592582628906831
    componentNetwork12.DragByTransform(translation208, rotation189)
    
    translation209 = NXOpen.Vector3d(0.0, -6.2272972450105311, 3.7975752707071209)
    rotation190 = NXOpen.Matrix3x3()
    
    rotation190.Xx = 1.0
    rotation190.Xy = -1.472510486006203e-19
    rotation190.Xz = -6.0040017173995916e-17
    rotation190.Yx = 2.0673266002898691e-17
    rotation190.Yy = 0.93969262078590843
    rotation190.Yz = 0.34202014332566849
    rotation190.Zx = 5.6368798265515909e-17
    rotation190.Zy = -0.34202014332566849
    rotation190.Zz = 0.93969262078590843
    componentNetwork12.DragByTransform(translation209, rotation190)
    
    translation210 = NXOpen.Vector3d(0.0, -7.5480101264019162, 5.0674594588023485)
    rotation191 = NXOpen.Matrix3x3()
    
    rotation191.Xx = 1.0
    rotation191.Xy = 3.0809132784265446e-18
    rotation191.Xz = -7.4772221092888342e-17
    rotation191.Yx = 2.8807850409345112e-17
    rotation191.Yy = 0.90630778703665005
    rotation191.Yz = 0.42261826174069905
    rotation191.Zx = 6.9068696444813213e-17
    rotation191.Zy = -0.42261826174069905
    rotation191.Zz = 0.90630778703665005
    componentNetwork12.DragByTransform(translation210, rotation191)
    
    translation211 = NXOpen.Vector3d(0.0, -8.7530195969285369, 6.4476190663074231)
    rotation192 = NXOpen.Matrix3x3()
    
    rotation192.Xx = 1.0
    rotation192.Xy = 7.5807896404409688e-18
    rotation192.Xz = -8.9167011468461862e-17
    rotation192.Yx = 3.8018349324863157e-17
    rotation192.Yy = 0.86602540378443882
    rotation192.Yz = 0.49999999999999944
    rotation192.Zx = 8.1011291931446842e-17
    rotation192.Zy = -0.49999999999999944
    rotation192.Zz = 0.86602540378443882
    componentNetwork12.DragByTransform(translation211, rotation192)
    
    translation212 = NXOpen.Vector3d(0.0, -9.8331548069150845, 7.9275502452460707)
    rotation193 = NXOpen.Matrix3x3()
    
    rotation193.Xx = 1.0
    rotation193.Xy = 1.3318131261228058e-17
    rotation193.Xz = -1.0311483525414631e-16
    rotation193.Yx = 4.8234665291254344e-17
    rotation193.Yy = 0.81915204428899191
    rotation193.Yz = 0.5735764363510456
    rotation193.Zx = 9.2105694362627203e-17
    rotation193.Zy = -0.5735764363510456
    rotation193.Zz = 0.81915204428899191
    componentNetwork12.DragByTransform(translation212, rotation193)
    
    translation213 = NXOpen.Vector3d(0.0, -10.780195275210078, 9.4959898257396933)
    rotation194 = NXOpen.Matrix3x3()
    
    rotation194.Xx = 1.0
    rotation194.Xy = 2.024927350675202e-17
    rotation194.Xz = -1.1650954108900634e-16
    rotation194.Yx = 5.9379045975234251e-17
    rotation194.Yy = 0.76604444311897835
    rotation194.Yz = 0.64278760968653881
    rotation194.Zx = 1.022674686368697e-16
    rotation194.Zy = -0.64278760968653881
    rotation194.Zz = 0.76604444311897835
    componentNetwork12.DragByTransform(translation213, rotation194)
    
    translation214 = NXOpen.Vector3d(0.0, -11.586933452011129, 11.141001035531021)
    rotation195 = NXOpen.Matrix3x3()
    
    rotation195.Xx = 1.0
    rotation195.Xy = 2.8321466199386331e-17
    rotation195.Xz = -1.2924918717369412e-16
    rotation195.Yx = 7.1366675910636743e-17
    rotation195.Yy = 0.70710678118654791
    rotation195.Yz = 0.70710678118654702
    rotation195.Zx = 1.1141927751610021e-16
    rotation195.Zy = -0.70710678118654702
    rotation195.Zz = 0.70710678118654791
    componentNetwork12.DragByTransform(translation214, rotation195)
    
    translation215 = NXOpen.Vector3d(0.0, -12.247229572670948, 12.850064346028619)
    rotation196 = NXOpen.Matrix3x3()
    
    rotation196.Xx = 1.0
    rotation196.Xy = 3.747327507861684e-17
    rotation196.Xz = -1.4123681710909663e-16
    rotation196.Yx = 8.4106321995324556e-17
    rotation196.Yy = 0.64278760968653981
    rotation196.Yz = 0.76604444311897768
    rotation196.Zx = 1.1949147020873454e-16
    rotation196.Zy = -0.76604444311897768
    rotation196.Zz = 0.64278760968653981
    componentNetwork12.DragByTransform(translation215, rotation196)
    
    translation216 = NXOpen.Vector3d(0.0, -12.756058385013622, 14.610172753478954)
    rotation197 = NXOpen.Matrix3x3()
    
    rotation197.Xx = 1.0
    rotation197.Xy = 4.7635049352859287e-17
    rotation197.Xz = -1.5238119779307655e-16
    rotation197.Yx = 9.7501027830184579e-17
    rotation197.Yy = 0.57357643635104671
    rotation197.Yz = 0.81915204428899135
    rotation197.Zx = 1.2642261245425853e-16
    rotation197.Zy = -0.81915204428899135
    rotation197.Zz = 0.57357643635104671
    componentNetwork12.DragByTransform(translation216, rotation197)
    
    translation217 = NXOpen.Vector3d(0.0, -13.109547394537978, 16.407930770118821)
    rotation198 = NXOpen.Matrix3x3()
    
    rotation198.Xx = 1.0
    rotation198.Xy = 5.8729451784039624e-17
    rotation198.Xz = -1.6259751375946776e-16
    rotation198.Yx = 1.1144885161586901e-16
    rotation198.Yy = 0.50000000000000067
    rotation198.Yz = 0.86602540378443826
    rotation198.Zx = 1.3215995407504564e-16
    rotation198.Zy = -0.86602540378443826
    rotation198.Zz = 0.50000000000000067
    componentNetwork12.DragByTransform(translation217, rotation198)
    
    translation218 = NXOpen.Vector3d(0.0, -13.305006336439041, 18.229656371925614)
    rotation199 = NXOpen.Matrix3x3()
    
    rotation199.Xx = 1.0
    rotation199.Xy = 7.067204727067324e-17
    rotation199.Xz = -1.7180801267498578e-16
    rotation199.Yx = 1.2584364199144255e-16
    rotation199.Yy = 0.42261826174070016
    rotation199.Yz = 0.9063077870366496
    rotation199.Zx = 1.3665983043706007e-16
    rotation199.Zy = -0.9063077870366496
    rotation199.Zz = 0.42261826174070016
    componentNetwork12.DragByTransform(translation218, rotation199)
    
    translation219 = NXOpen.Vector3d(0.0, -13.340947650147607, 20.061485127081596)
    rotation200 = NXOpen.Matrix3x3()
    
    rotation200.Xx = 1.0
    rotation200.Xy = 8.3371945449970519e-17
    rotation200.Xz = -1.7994259708143222e-16
    rotation200.Yx = 1.4057584591033495e-16
    rotation200.Yy = 0.3420201433256696
    rotation200.Yz = 0.93969262078590798
    rotation200.Zx = 1.3988799476408728e-16
    rotation200.Zy = -0.93969262078590798
    rotation200.Zz = 0.3420201433256696
    componentNetwork12.DragByTransform(translation219, rotation200)
    
    translation220 = NXOpen.Vector3d(0.0, -13.217097800564394, 21.889475712671583)
    rotation201 = NXOpen.Matrix3x3()
    
    rotation201.Xx = 1.0
    rotation201.Xy = 9.6732492428378841e-17
    rotation201.Xz = -1.869393578796777e-16
    rotation201.Yx = 1.5553334240517559e-16
    rotation201.Yy = 0.25881904510252179
    rotation201.Yz = 0.96592582628906809
    rotation201.Zx = 1.4181987877637966e-16
    rotation201.Zy = -0.96592582628906809
    rotation201.Zz = 0.25881904510252179
    componentNetwork12.DragByTransform(translation220, rotation201)
    
    translation221 = NXOpen.Vector3d(0.0, -12.934399359827315, 23.699716016568345)
    rotation202 = NXOpen.Matrix3x3()
    
    rotation202.Xx = 1.0
    rotation202.Xy = 1.1065200637607368e-16
    rotation202.Xz = -1.9274504549528783e-16
    rotation202.Yx = 1.7060229589605535e-16
    rotation202.Yy = 0.17364817766693141
    rotation202.Yz = 0.9848077530122078
    rotation202.Zx = 1.424407796701002e-16
    rotation202.Zy = -0.9848077530122078
    rotation202.Zz = 0.17364817766693141
    componentNetwork12.DragByTransform(translation221, rotation202)
    
    translation222 = NXOpen.Vector3d(0.0, -12.49500383376837, 25.478429017006242)
    rotation203 = NXOpen.Matrix3x3()
    
    rotation203.Xx = 1.0
    rotation203.Xy = 1.2502455138708078e-16
    rotation203.Xz = -1.9731547513993786e-16
    rotation203.Yx = 1.8566802254802576e-16
    rotation203.Yy = 0.087155742747659387
    rotation203.Yz = 0.99619469809174555
    rotation203.Zx = 1.4174597201453751e-16
    rotation203.Zy = -0.99619469809174555
    rotation203.Zz = 0.087155742747659387
    componentNetwork12.DragByTransform(translation222, rotation203)
    
    translation223 = NXOpen.Vector3d(0.0, -11.902255287655128, 27.212077634035673)
    rotation204 = NXOpen.Matrix3x3()
    
    rotation204.Xx = 1.0
    rotation204.Xy = 1.3974074371548639e-16
    rotation204.Xz = -2.0061586308433104e-16
    rotation204.Yx = 2.0061586308433089e-16
    rotation204.Yy = 1.2212453270876722e-15
    rotation204.Yz = 1.0000000000000002
    rotation204.Zx = 1.3974074371548671e-16
    rotation204.Zy = -1.0000000000000002
    rotation204.Zz = 1.2212453270876722e-15
    componentNetwork12.DragByTransform(translation223, rotation204)
    
    translation224 = NXOpen.Vector3d(0.0, -11.160664895834882, 28.887467754875388)
    rotation205 = NXOpen.Matrix3x3()
    
    rotation205.Xx = 1.0
    rotation205.Xy = 1.546885842517915e-16
    rotation205.Xz = -2.0262109138338186e-16
    rotation205.Yx = 2.1533205541273653e-16
    rotation205.Yy = -0.087155742747656861
    rotation205.Yz = 0.99619469809174588
    rotation205.Zx = 1.3644035577109358e-16
    rotation205.Zy = -0.99619469809174588
    rotation205.Zz = -0.087155742747656861
    componentNetwork12.DragByTransform(translation224, rotation205)
    
    translation225 = NXOpen.Vector3d(0.0, -10.275876608973894, 30.491848649077575)
    rotation206 = NXOpen.Matrix3x3()
    
    rotation206.Xx = 1.0
    rotation206.Xy = 1.6975431090376191e-16
    rotation206.Xz = -2.0331589903894463e-16
    rotation206.Yx = 2.2970460042374366e-16
    rotation206.Yy = -0.17364817766692897
    rotation206.Yz = 0.98480775301220846
    rotation206.Zx = 1.3186992612644362e-16
    rotation206.Zy = -0.98480775301220846
    rotation206.Zz = -0.17364817766692897
    componentNetwork12.DragByTransform(translation225, rotation206)
    
    translation226 = NXOpen.Vector3d(0.0, -9.2546242001849581, 32.013010009285694)
    rotation207 = NXOpen.Matrix3x3()
    
    rotation207.Xx = 1.0
    rotation207.Xy = 1.8482326439464169e-16
    rotation207.Xz = -2.0269499814522411e-16
    rotation207.Yx = 2.4362411437143849e-16
    rotation207.Yy = -0.25881904510251941
    rotation207.Yz = 0.96592582628906887
    rotation207.Zx = 1.2606423851083352e-16
    rotation207.Zy = -0.96592582628906887
    rotation207.Zz = -0.25881904510251941
    componentNetwork12.DragByTransform(translation226, rotation207)
    
    translation227 = NXOpen.Vector3d(0.0, -8.1046800169480218, 33.439374879046213)
    rotation208 = NXOpen.Matrix3x3()
    
    rotation208.Xx = 1.0
    rotation208.Xy = 1.9978076088948231e-16
    rotation208.Xz = -2.0076311413293178e-16
    rotation208.Yx = 2.5698466134984685e-16
    rotation208.Yy = -0.34202014332566744
    rotation208.Yz = 0.93969262078590909
    rotation208.Zx = 1.1906747771258809e-16
    rotation208.Zy = -0.93969262078590909
    rotation208.Zz = -0.34202014332566744
    componentNetwork12.DragByTransform(translation227, rotation208)
    
    translation228 = NXOpen.Vector3d(0.0, -6.8347958288527941, 34.7600877604376)
    rotation209 = NXOpen.Matrix3x3()
    
    rotation209.Xx = 1.0
    rotation209.Xy = 2.1451296480837476e-16
    rotation209.Xz = -1.9753494980590462e-16
    rotation209.Yx = 2.696845595291442e-16
    rotation209.Yy = -0.42261826174069805
    rotation209.Yz = 0.90630778703665071
    rotation209.Zx = 1.1093289330614167e-16
    rotation209.Zy = -0.90630778703665071
    rotation209.Zz = -0.42261826174069805
    componentNetwork12.DragByTransform(translation228, rotation209)
    
    translation229 = NXOpen.Vector3d(0.0, -5.4546362213477249, 35.965097230964226)
    rotation210 = NXOpen.Matrix3x3()
    
    rotation210.Xx = 1.0
    rotation210.Xy = 2.2890775518394828e-16
    rotation210.Xz = -1.9303507344389019e-16
    rotation210.Yx = 2.8162715501577783e-16
    rotation210.Yy = -0.49999999999999867
    rotation210.Yz = 0.8660254037844396
    rotation210.Zx = 1.0172239439062368e-16
    rotation210.Zy = -0.8660254037844396
    rotation210.Zz = -0.49999999999999867
    componentNetwork12.DragByTransform(translation229, rotation210)
    
    translation230 = NXOpen.Vector3d(0.0, -3.9747050424090773, 37.04523244095077)
    rotation211 = NXOpen.Matrix3x3()
    
    rotation211.Xx = 1.0
    rotation211.Xy = 2.428555789696327e-16
    rotation211.Xz = -1.8729773182310315e-16
    rotation211.Yx = 2.9272155744695814e-16
    rotation211.Yy = -0.57357643635104472
    rotation211.Yz = 0.81915204428899291
    rotation211.Zx = 9.1506078424232492e-17
    rotation211.Zy = -0.81915204428899291
    rotation211.Zz = -0.57357643635104472
    componentNetwork12.DragByTransform(translation230, rotation211)
    
    translation231 = NXOpen.Vector3d(0.0, -2.40626546191546, 37.99227290924577)
    rotation212 = NXOpen.Matrix3x3()
    
    rotation212.Xx = 1.0
    rotation212.Xy = 2.5625028480449278e-16
    rotation212.Xz = -1.8036658957757919e-16
    rotation212.Yx = 3.0288333172120067e-16
    rotation212.Yy = -0.64278760968653792
    rotation212.Yz = 0.76604444311897946
    rotation212.Zx = 8.0361697740252596e-17
    rotation212.Zy = -0.76604444311897946
    rotation212.Zz = -0.64278760968653792
    componentNetwork12.DragByTransform(translation231, rotation212)
    
    translation232 = NXOpen.Vector3d(0.0, -0.76125425212413056, 38.799011086046818)
    rotation213 = NXOpen.Matrix3x3()
    
    rotation213.Xx = 1.0
    rotation213.Xy = 2.6898993088918061e-16
    rotation213.Xz = -1.7229439688494491e-16
    rotation213.Yx = 3.1203514060043115e-16
    rotation213.Yy = -0.70710678118654624
    rotation213.Yz = 0.70710678118654902
    rotation213.Zx = 6.8374067804850117e-17
    rotation213.Zy = -0.70710678118654902
    rotation213.Zz = -0.70710678118654624
    componentNetwork12.DragByTransform(translation232, rotation213)
    
    translation233 = NXOpen.Vector3d(0.0, 0.94780905837346641, 39.45930720670664)
    rotation214 = NXOpen.Matrix3x3()
    
    rotation214.Xx = 1.0
    rotation214.Xy = 2.8097756082458312e-16
    rotation214.Xz = -1.6314258800571442e-16
    rotation214.Yx = 3.2010733329306551e-16
    rotation214.Yy = -0.7660444431189769
    rotation214.Yz = 0.64278760968654103
    rotation214.Zx = 5.5634421720162329e-17
    rotation214.Zy = -0.64278760968654103
    rotation214.Zz = -0.7660444431189769
    componentNetwork12.DragByTransform(translation233, rotation214)
    
    translation234 = NXOpen.Vector3d(0.0, 2.707917465823801, 39.968136019049318)
    rotation215 = NXOpen.Matrix3x3()
    
    rotation215.Xx = 1.0
    rotation215.Xy = 2.9212194150856301e-16
    rotation215.Xz = -1.52980813731472e-16
    rotation215.Yx = 3.2703847553858957e-16
    rotation215.Yy = -0.81915204428899069
    rotation215.Yz = 0.57357643635104794
    rotation215.Zx = 4.2239715885302324e-17
    rotation215.Zy = -0.57357643635104794
    rotation215.Zz = -0.81915204428899069
    componentNetwork12.DragByTransform(translation234, rotation215)
    
    translation235 = NXOpen.Vector3d(0.0, 4.5056754824636664, 40.321625028573678)
    rotation216 = NXOpen.Matrix3x3()
    
    rotation216.Xx = 1.0
    rotation216.Xy = 3.0233825747495422e-16
    rotation216.Xz = -1.4188641130029166e-16
    rotation216.Yx = 3.3277581715937668e-16
    rotation216.Yy = -0.86602540378443771
    rotation216.Yz = 0.500000000000002
    rotation216.Zx = 2.8291892099617886e-17
    rotation216.Zy = -0.500000000000002
    rotation216.Zz = -0.86602540378443771
    componentNetwork12.DragByTransform(translation235, rotation216)
    
    translation236 = NXOpen.Vector3d(0.0, 6.3274010842704609, 40.517083970474744)
    rotation217 = NXOpen.Matrix3x3()
    
    rotation217.Xx = 1.0
    rotation217.Xy = 3.1154875639047229e-16
    rotation217.Xz = -1.2994381581365806e-16
    rotation217.Yx = 3.3727569352139108e-16
    rotation217.Yy = -0.90630778703664916
    rotation217.Yz = 0.4226182617407015
    rotation217.Zx = 1.3897101724044366e-17
    rotation217.Zy = -0.4226182617407015
    rotation217.Zz = -0.90630778703664916
    componentNetwork12.DragByTransform(translation236, rotation217)
    
    translation237 = NXOpen.Vector3d(0.0, 6.3274010842704609, 40.517083970474744)
    rotation218 = NXOpen.Matrix3x3()
    
    rotation218.Xx = 1.0
    rotation218.Xy = 3.1154875639047229e-16
    rotation218.Xz = -1.2994381581365806e-16
    rotation218.Yx = 3.3727569352139108e-16
    rotation218.Yy = -0.90630778703664916
    rotation218.Yz = 0.4226182617407015
    rotation218.Zx = 1.3897101724044366e-17
    rotation218.Zy = -0.4226182617407015
    rotation218.Zz = -0.90630778703664916
    componentNetwork12.DragByTransform(translation237, rotation218)
    
    componentNetwork12.EndDrag()
    
    componentNetwork12.ResetDisplay()
    
    componentNetwork12.ApplyToModel()
    
    markId68 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component")
    
    theSession.DeleteUndoMark(markId68, None)
    
    markId69 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component")
    
    componentNetwork12.Solve()
    
    componentPositioner12.ClearNetwork()
    
    nErrs28 = theSession.UpdateManager.AddToDeleteList(componentNetwork12)
    
    componentPositioner12.DeleteNonPersistentConstraints()
    
    nErrs29 = theSession.UpdateManager.DoUpdate(markId65)
    
    theSession.DeleteUndoMark(markId69, None)
    
    theSession.SetUndoMarkName(markId64, "Move Component")
    
    componentPositioner12.EndMoveComponent()
    
    componentPositioner12.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMarksUpToMark(markId65, None, False)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Move Component...
    # ----------------------------------------------
    markId70 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner13 = workPart.ComponentAssembly.Positioner
    
    componentPositioner13.ClearNetwork()
    
    componentPositioner13.PrimaryArrangement = arrangement1
    
    componentPositioner13.BeginMoveComponent()
    
    allowInterpartPositioning12 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression123 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression124 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression125 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression126 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression127 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression128 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression129 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression130 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network13 = componentPositioner13.EstablishNetwork()
    
    componentNetwork13 = network13
    componentNetwork13.MoveObjectsState = True
    
    componentNetwork13.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork13.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    expression131 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression132 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression133 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression134 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression135 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    componentNetwork13.RemoveAllConstraints()
    
    movableObjects10 = [NXOpen.NXObject.Null] * 1 
    movableObjects10[0] = component8
    componentNetwork13.SetMovingGroup(movableObjects10)
    
    componentNetwork13.Solve()
    
    theSession.SetUndoMarkName(markId70, "Move Component Dialog")
    
    componentNetwork13.MoveObjectsState = True
    
    componentNetwork13.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId71 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component Update")
    
    markId72 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Rotate About Y-axis")
    
    loaded13 = componentNetwork13.IsReferencedGeometryLoaded()
    
    componentNetwork13.BeginDrag()
    
    translation238 = NXOpen.Vector3d(-2.8421709430404007e-14, 10.892219458995168, -3.1525451258653732)
    rotation219 = NXOpen.Matrix3x3()
    
    rotation219.Xx = 1.0
    rotation219.Xy = -4.8237825717995684e-16
    rotation219.Xz = 7.2860530613227126e-16
    rotation219.Yx = 6.8003407102676793e-16
    rotation219.Yy = 0.93969262078590887
    rotation219.Yz = -0.34202014332566855
    rotation219.Zx = -5.3540224463432133e-16
    rotation219.Zy = 0.34202014332566832
    rotation219.Zz = 0.93969262078590832
    componentNetwork13.DragByTransform(translation238, rotation219)
    
    translation239 = NXOpen.Vector3d(-2.8421709430404007e-14, 13.734823161905853, -3.3334825654831448)
    rotation220 = NXOpen.Matrix3x3()
    
    rotation220.Xx = 1.0
    rotation220.Xy = -5.6106351308865989e-16
    rotation220.Xz = 9.3351438667230787e-16
    rotation220.Yx = 8.7591438079937925e-16
    rotation220.Yy = 0.90630778703665049
    rotation220.Yz = -0.42261826174069922
    rotation220.Zx = -6.2973182685124015e-16
    rotation220.Zy = 0.422618261740699
    rotation220.Zz = 0.90630778703665005
    componentNetwork13.DragByTransform(translation239, rotation220)
    
    translation240 = NXOpen.Vector3d(-4.2632564145606011e-14, 16.582379636462193, -3.2659822464522463)
    rotation221 = NXOpen.Matrix3x3()
    
    rotation221.Xx = 1.0
    rotation221.Xy = -6.2159034473269611e-16
    rotation221.Xz = 1.1445015982191594e-15
    rotation221.Yx = 1.0792706716566156e-15
    rotation221.Yy = 0.86602540378443915
    rotation221.Yz = -0.49999999999999983
    rotation221.Zx = -7.0663036264106996e-16
    rotation221.Zy = 0.49999999999999956
    rotation221.Zz = 0.86602540378443871
    componentNetwork13.DragByTransform(translation240, rotation221)
    
    translation241 = NXOpen.Vector3d(-4.2632564145606011e-14, 19.413217258491194, -2.9505578869582934)
    rotation222 = NXOpen.Matrix3x3()
    
    rotation222.Xx = 1.0
    rotation222.Xy = -6.6349810637615343e-16
    rotation222.Xz = 1.3599612006953928e-15
    rotation222.Yx = 1.288555279435167e-15
    rotation222.Yy = 0.81915204428899258
    rotation222.Yz = -0.57357643635104594
    rotation222.Zx = -7.655126077138462e-16
    rotation222.Zy = 0.57357643635104549
    rotation222.Zz = 0.81915204428899191
    componentNetwork13.DragByTransform(translation241, rotation222)
    
    translation242 = NXOpen.Vector3d(-4.2632564145606011e-14, 22.205791644382728, -2.3896100568354868)
    rotation223 = NXOpen.Matrix3x3()
    
    rotation223.Xx = 1.0
    rotation223.Xy = -6.8646785464832688e-16
    rotation223.Xz = 1.5782534164280991e-15
    rotation223.Yx = 1.5021754219003378e-15
    rotation223.Yy = 0.76604444311897879
    rotation223.Yz = -0.64278760968653925
    rotation223.Zx = -8.0593043263049257e-16
    rotation223.Zy = 0.64278760968653859
    rotation223.Zz = 0.76604444311897812
    componentNetwork13.DragByTransform(translation242, rotation223)
    
    translation243 = NXOpen.Vector3d(-4.2632564145606011e-14, 19.413217258491194, -2.9505578869582934)
    rotation224 = NXOpen.Matrix3x3()
    
    rotation224.Xx = 1.0
    rotation224.Xy = -6.6349810637615343e-16
    rotation224.Xz = 1.3599612006953928e-15
    rotation224.Yx = 1.2885552794351673e-15
    rotation224.Yy = 0.81915204428899258
    rotation224.Yz = -0.57357643635104605
    rotation224.Zx = -7.655126077138462e-16
    rotation224.Zy = 0.57357643635104549
    rotation224.Zz = 0.81915204428899191
    componentNetwork13.DragByTransform(translation243, rotation224)
    
    translation244 = NXOpen.Vector3d(-4.2632564145606011e-14, 16.582379636462189, -3.2659822464522463)
    rotation225 = NXOpen.Matrix3x3()
    
    rotation225.Xx = 1.0
    rotation225.Xy = -6.2159034473269611e-16
    rotation225.Xz = 1.1445015982191594e-15
    rotation225.Yx = 1.0792706716566154e-15
    rotation225.Yy = 0.86602540378443926
    rotation225.Yz = -0.49999999999999989
    rotation225.Zx = -7.0663036264106996e-16
    rotation225.Zy = 0.49999999999999956
    rotation225.Zz = 0.86602540378443871
    componentNetwork13.DragByTransform(translation244, rotation225)
    
    translation245 = NXOpen.Vector3d(-2.8421709430404007e-14, 13.734823161905853, -3.3334825654831448)
    rotation226 = NXOpen.Matrix3x3()
    
    rotation226.Xx = 1.0
    rotation226.Xy = -5.6106351308865989e-16
    rotation226.Xz = 9.3351438667230787e-16
    rotation226.Yx = 8.7591438079937905e-16
    rotation226.Yy = 0.9063077870366506
    rotation226.Yz = -0.42261826174069927
    rotation226.Zx = -6.2973182685124015e-16
    rotation226.Zy = 0.422618261740699
    rotation226.Zz = 0.90630778703665005
    componentNetwork13.DragByTransform(translation245, rotation226)
    
    translation246 = NXOpen.Vector3d(-2.8421709430404007e-14, 10.892219458995166, -3.1525451258653803)
    rotation227 = NXOpen.Matrix3x3()
    
    rotation227.Xx = 1.0
    rotation227.Xy = -4.8237825717995684e-16
    rotation227.Xz = 7.2860530613227126e-16
    rotation227.Yx = 6.8003407102676793e-16
    rotation227.Yy = 0.93969262078590898
    rotation227.Yz = -0.3420201433256686
    rotation227.Zx = -5.3540224463432153e-16
    rotation227.Zy = 0.34202014332566844
    rotation227.Zz = 0.93969262078590843
    componentNetwork13.DragByTransform(translation246, rotation227)
    
    translation247 = NXOpen.Vector3d(-2.8421709430404007e-14, 8.0762024583203296, -2.7245469707674346)
    rotation228 = NXOpen.Matrix3x3()
    
    rotation228.Xx = 1.0
    rotation228.Xy = -3.8613341931550737e-16
    rotation228.Xz = 5.3133383842944479e-16
    rotation228.Yx = 4.9312050977191539e-16
    rotation228.Yy = 0.96592582628906887
    rotation228.Yz = -0.25881904510252074
    rotation228.Zx = -4.2435952106874495e-16
    rotation228.Zy = 0.25881904510252057
    rotation228.Zz = 0.96592582628906831
    componentNetwork13.DragByTransform(translation247, rotation228)
    
    translation248 = NXOpen.Vector3d(-1.4210854715202004e-14, 5.3082037496140195, -2.0527454245819641)
    rotation229 = NXOpen.Matrix3x3()
    
    rotation229.Xx = 1.0
    rotation229.Xy = -2.7306148082568323e-16
    rotation229.Xz = 3.432013385488161e-16
    rotation229.Yx = 3.1659622209746553e-16
    rotation229.Yy = 0.98480775301220858
    rotation229.Yz = -0.17364817766693041
    rotation229.Zx = -2.974487583302733e-16
    rotation229.Zy = 0.17364817766693025
    rotation229.Zz = 0.98480775301220802
    componentNetwork13.DragByTransform(translation248, rotation229)
    
    translation249 = NXOpen.Vector3d(-1.4210854715202004e-14, 2.609289474412817, -1.1422533027203059)
    rotation230 = NXOpen.Matrix3x3()
    
    rotation230.Xx = 1.0
    rotation230.Xy = -1.4402298743709404e-16
    rotation230.Xz = 1.6563960841198606e-16
    rotation230.Yx = 1.5180466442089935e-16
    rotation230.Yy = 0.99619469809174599
    rotation230.Yz = -0.087155742747658194
    rotation230.Zx = -1.5563582395416081e-16
    rotation230.Zy = 0.087155742747658138
    rotation230.Zz = 0.99619469809174555
    componentNetwork13.DragByTransform(translation249, rotation230)
    
    translation250 = NXOpen.Vector3d(-1.4210854715202004e-14, 0.0, 0.0)
    rotation231 = NXOpen.Matrix3x3()
    
    rotation231.Xx = 1.0
    rotation231.Xy = -7.8886090522101181e-31
    rotation231.Xz = -3.944304526105059e-31
    rotation231.Yx = -3.944304526105059e-31
    rotation231.Yy = 1.0000000000000004
    rotation231.Yz = -1.1102230246251565e-16
    rotation231.Zx = 0.0
    rotation231.Zy = 1.1102230246251565e-16
    rotation231.Zz = 0.99999999999999989
    componentNetwork13.DragByTransform(translation250, rotation231)
    
    translation251 = NXOpen.Vector3d(-1.4210854715202004e-14, -2.4998064051920927, 1.3653212462338473)
    rotation232 = NXOpen.Matrix3x3()
    
    rotation232.Xx = 1.0
    rotation232.Xy = 1.5791137958774404e-16
    rotation232.Xz = -1.5245686925119754e-16
    rotation232.Yx = -1.37662446006829e-16
    rotation232.Yy = 0.99619469809174588
    rotation232.Yz = 0.087155742747658083
    rotation232.Zx = 1.6827423093643765e-16
    rotation232.Zy = -0.087155742747657972
    rotation232.Zz = 0.99619469809174555
    componentNetwork13.DragByTransform(translation251, rotation232)
    
    translation252 = NXOpen.Vector3d(0.0, -4.8711047049955738, 2.9433195168938902)
    rotation233 = NXOpen.Matrix3x3()
    
    rotation233.Xx = 1.0
    rotation233.Xy = 3.2850935037797916e-16
    rotation233.Xz = -2.9057071051062944e-16
    rotation233.Yx = -2.6013497926261665e-16
    rotation233.Yy = 0.98480775301220846
    rotation233.Yz = 0.17364817766693019
    rotation233.Zx = 3.4790620035096733e-16
    rotation233.Zy = -0.17364817766693
    rotation233.Zz = 0.98480775301220802
    componentNetwork13.DragByTransform(translation252, rotation233)
    
    translation253 = NXOpen.Vector3d(0.0, -7.0958478875198807, 4.7219852923190011)
    rotation234 = NXOpen.Matrix3x3()
    
    rotation234.Xx = 1.0
    rotation234.Xy = 5.1049555880311965e-16
    rotation234.Xz = -4.1329039405089421e-16
    rotation234.Yx = -3.6648550983834957e-16
    rotation234.Yy = 0.96592582628906876
    rotation234.Yz = 0.25881904510252063
    rotation234.Zx = 5.3752880049159583e-16
    rotation234.Zy = -0.2588190451025203
    rotation234.Zz = 0.96592582628906853
    componentNetwork13.DragByTransform(translation253, rotation234)
    
    translation254 = NXOpen.Vector3d(0.0, -9.1571043138093309, 6.6877818519704313)
    rotation235 = NXOpen.Matrix3x3()
    
    rotation235.Xx = 1.0
    rotation235.Xy = 7.0248497993077373e-16
    rotation235.Xz = -5.1968194898007941e-16
    rotation235.Yx = -4.5590464598013968e-16
    rotation235.Yy = 0.93969262078590887
    rotation235.Yz = 0.34202014332566855
    rotation235.Zx = 7.3569888887399671e-16
    rotation235.Zy = -0.34202014332566821
    rotation235.Zz = 0.93969262078590854
    componentNetwork13.DragByTransform(translation254, rotation235)
    
    translation255 = NXOpen.Vector3d(-1.4210854715202004e-14, -11.03918657783921, 8.8257482970488219)
    rotation236 = NXOpen.Matrix3x3()
    
    rotation236.Xx = 1.0
    rotation236.Xy = 9.0301645833977643e-16
    rotation236.Xz = -6.0893567132419718e-16
    rotation236.Yx = -5.2771185406919788e-16
    rotation236.Yy = 0.90630778703665049
    rotation236.Yz = 0.42261826174069927
    rotation236.Zx = 9.4090827146720857e-16
    rotation236.Zy = -0.42261826174069889
    rotation236.Zz = 0.90630778703665027
    componentNetwork13.DragByTransform(translation255, rotation236)
    
    translation256 = NXOpen.Vector3d(0.0, -12.727770897147906, 11.119613411967691)
    rotation237 = NXOpen.Matrix3x3()
    
    rotation237.Xx = 1.0
    rotation237.Xy = 1.11056382839522e-15
    rotation237.Xz = -6.8037228636333686e-16
    rotation237.Yx = -5.8136063789358867e-16
    rotation237.Yy = 0.86602540378443926
    rotation237.Yz = 0.49999999999999983
    rotation237.Zx = 1.1515951809608843e-15
    rotation237.Zy = -0.49999999999999939
    rotation237.Zz = 0.86602540378443904
    componentNetwork13.DragByTransform(translation256, rotation237)
    
    translation257 = NXOpen.Vector3d(-1.4210854715202004e-14, -15.47461155772104, 16.104155237550128)
    rotation238 = NXOpen.Matrix3x3()
    
    rotation238.Xx = 1.0
    rotation238.Xy = 1.5403466264585877e-15
    rotation238.Xz = -7.6775922807224603e-16
    rotation238.Yx = -6.3269103817246906e-16
    rotation238.Yy = 0.76604444311897879
    rotation238.Yz = 0.64278760968653925
    rotation238.Zx = 1.5829582782302488e-15
    rotation238.Zy = -0.64278760968653859
    rotation238.Zz = 0.76604444311897868
    componentNetwork13.DragByTransform(translation257, rotation238)
    
    translation258 = NXOpen.Vector3d(-1.4210854715202004e-14, -16.51196278297077, 18.75689657517237)
    rotation239 = NXOpen.Matrix3x3()
    
    rotation239.Xx = 1.0
    rotation239.Xy = 1.7593111478633018e-15
    rotation239.Xz = -7.8304448734993191e-16
    rotation239.Yx = -6.299819992866931e-16
    rotation239.Yy = 0.70710678118654824
    rotation239.Yz = 0.70710678118654746
    rotation239.Zx = 1.8003515323715579e-15
    rotation239.Zy = -0.7071067811865468
    rotation239.Zz = 0.70710678118654846
    componentNetwork13.DragByTransform(translation258, rotation239)
    
    translation259 = NXOpen.Vector3d(-1.4210854715202004e-14, -17.314164932025648, 21.489954547647287)
    rotation240 = NXOpen.Matrix3x3()
    
    rotation240.Xx = 1.0
    rotation240.Xy = 1.9787746412823111e-15
    rotation240.Xz = -7.7918756610290731e-16
    rotation240.Yx = -6.0833619857874247e-16
    rotation240.Yy = 0.64278760968654014
    rotation240.Yz = 0.76604444311897812
    rotation240.Zx = 2.0166814312518201e-15
    rotation240.Zy = -0.76604444311897746
    rotation240.Zz = 0.64278760968654036
    componentNetwork13.DragByTransform(translation259, rotation240)
    
    translation260 = NXOpen.Vector3d(-2.8421709430404007e-14, -17.875112762148454, 24.282528933538821)
    rotation241 = NXOpen.Matrix3x3()
    
    rotation241.Xx = 1.0
    rotation241.Xy = 2.1970668570150176e-15
    rotation241.Xz = -7.5621781783073416e-16
    rotation241.Yx = -5.6791837366209631e-16
    rotation241.Yy = 0.57357643635104716
    rotation241.Yz = 0.81915204428899191
    rotation241.Zx = 2.2303015737169908e-15
    rotation241.Zy = -0.81915204428899124
    rotation241.Zz = 0.57357643635104738
    componentNetwork13.DragByTransform(translation260, rotation241)
    
    translation261 = NXOpen.Vector3d(-1.4210854715202004e-14, -18.190537121642407, 27.113366555567818)
    rotation242 = NXOpen.Matrix3x3()
    
    rotation242.Xx = 1.0
    rotation242.Xy = 2.412526459491251e-15
    rotation242.Xz = -7.1431005618727703e-16
    rotation242.Yx = -5.0903612858932046e-16
    rotation242.Yy = 0.50000000000000111
    rotation242.Yz = 0.86602540378443882
    rotation242.Zx = 2.4395861814955424e-15
    rotation242.Zy = -0.86602540378443815
    rotation242.Zz = 0.50000000000000133
    componentNetwork13.DragByTransform(translation261, rotation242)
    
    translation262 = NXOpen.Vector3d(-2.8421709430404007e-14, -18.077100001055548, 32.803526733034843)
    rotation243 = NXOpen.Matrix3x3()
    
    rotation243.Xx = 1.0
    rotation243.Xy = 2.8284227515781397e-15
    rotation243.Xz = -5.7509796863453866e-16
    rotation243.Yx = -3.3780801058257262e-16
    rotation243.Yy = 0.34202014332566999
    rotation243.Yz = 0.93969262078590887
    rotation243.Zx = 2.8388227821253902e-15
    rotation243.Zy = -0.93969262078590787
    rotation243.Zz = 0.34202014332567027
    componentNetwork13.DragByTransform(translation262, rotation243)
    
    translation263 = NXOpen.Vector3d(-2.8421709430404007e-14, -17.64910184595761, 35.619543733709676)
    rotation244 = NXOpen.Matrix3x3()
    
    rotation244.Xx = 1.0
    rotation244.Xy = 3.025694219280966e-15
    rotation244.Xz = -4.7885313077008957e-16
    rotation244.Yx = -2.2676528701699604e-16
    rotation244.Yy = 0.25881904510252213
    rotation244.Yz = 0.96592582628906876
    rotation244.Zx = 3.025736343380243e-15
    rotation244.Zy = -0.96592582628906787
    rotation244.Zz = 0.25881904510252252
    componentNetwork13.DragByTransform(translation263, rotation244)
    
    translation264 = NXOpen.Vector3d(-4.2632564145606011e-14, -16.977300299772146, 38.387542442415985)
    rotation245 = NXOpen.Matrix3x3()
    
    rotation245.Xx = 1.0
    rotation245.Xy = 3.2138267191615949e-15
    rotation245.Xz = -3.6578119228026539e-16
    rotation245.Yx = -9.9854524278524588e-17
    rotation245.Yy = 0.1736481776669318
    rotation245.Yz = 0.98480775301220869
    rotation245.Zx = 3.2022606310546928e-15
    rotation245.Zy = -0.9848077530122078
    rotation245.Zz = 0.17364817766693214
    componentNetwork13.DragByTransform(translation264, rotation245)
    
    translation265 = NXOpen.Vector3d(-4.2632564145606011e-14, -16.066808177910492, 41.086456717617189)
    rotation246 = NXOpen.Matrix3x3()
    
    rotation246.Xx = 1.0
    rotation246.Xy = 3.3913884492984249e-15
    rotation246.Xz = -2.3674269889167674e-16
    rotation246.Yx = 4.1958410097587898e-17
    rotation246.Yy = 0.087155742747659526
    rotation246.Yz = 0.99619469809174632
    rotation246.Zx = 3.367052188731259e-15
    rotation246.Zy = -0.99619469809174532
    rotation246.Zz = 0.087155742747660081
    componentNetwork13.DragByTransform(translation265, rotation246)
    
    translation266 = NXOpen.Vector3d(-5.6843418860808015e-14, -14.924554875190189, 43.695746192030008)
    rotation247 = NXOpen.Matrix3x3()
    
    rotation247.Xx = 1.0
    rotation247.Xy = 3.5570280577104114e-15
    rotation247.Xz = -9.2719711454583393e-17
    rotation247.Yx = 1.9759423405174852e-16
    rotation247.Yy = 1.4432899320127035e-15
    rotation247.Yz = 1.0000000000000009
    rotation247.Zx = 3.5188568531521591e-15
    rotation247.Zy = -0.99999999999999989
    rotation247.Zz = 1.9984014443252818e-15
    componentNetwork13.DragByTransform(translation266, rotation247)
    
    translation267 = NXOpen.Vector3d(-4.2632564145606011e-14, -16.066808177910495, 41.086456717617189)
    rotation248 = NXOpen.Matrix3x3()
    
    rotation248.Xx = 1.0
    rotation248.Xy = 3.3913884492984249e-15
    rotation248.Xz = -2.367426988916763e-16
    rotation248.Yx = 4.1958410097587701e-17
    rotation248.Yy = 0.087155742747659581
    rotation248.Yz = 0.99619469809174632
    rotation248.Zx = 3.367052188731259e-15
    rotation248.Zy = -0.99619469809174532
    rotation248.Zz = 0.087155742747660081
    componentNetwork13.DragByTransform(translation267, rotation248)
    
    translation268 = NXOpen.Vector3d(-4.2632564145606011e-14, -16.977300299772146, 38.387542442415985)
    rotation249 = NXOpen.Matrix3x3()
    
    rotation249.Xx = 1.0
    rotation249.Xy = 3.2138267191615949e-15
    rotation249.Xz = -3.6578119228026534e-16
    rotation249.Yx = -9.9854524278524983e-17
    rotation249.Yy = 0.1736481776669318
    rotation249.Yz = 0.9848077530122088
    rotation249.Zx = 3.2022606310546928e-15
    rotation249.Zy = -0.9848077530122078
    rotation249.Zz = 0.17364817766693214
    componentNetwork13.DragByTransform(translation268, rotation249)
    
    translation269 = NXOpen.Vector3d(-2.8421709430404007e-14, -17.64910184595761, 35.619543733709683)
    rotation250 = NXOpen.Matrix3x3()
    
    rotation250.Xx = 1.0
    rotation250.Xy = 3.0256942192809656e-15
    rotation250.Xz = -4.7885313077008908e-16
    rotation250.Yx = -2.2676528701699604e-16
    rotation250.Yy = 0.25881904510252213
    rotation250.Yz = 0.96592582628906876
    rotation250.Zx = 3.025736343380243e-15
    rotation250.Zy = -0.96592582628906798
    rotation250.Zz = 0.25881904510252246
    componentNetwork13.DragByTransform(translation269, rotation250)
    
    translation270 = NXOpen.Vector3d(-2.8421709430404007e-14, -18.077100001055548, 32.803526733034843)
    rotation251 = NXOpen.Matrix3x3()
    
    rotation251.Xx = 1.0
    rotation251.Xy = 2.8284227515781393e-15
    rotation251.Xz = -5.7509796863453816e-16
    rotation251.Yx = -3.3780801058257282e-16
    rotation251.Yy = 0.34202014332567016
    rotation251.Yz = 0.93969262078590876
    rotation251.Zx = 2.8388227821253902e-15
    rotation251.Zy = -0.93969262078590798
    rotation251.Zz = 0.34202014332567027
    componentNetwork13.DragByTransform(translation270, rotation251)
    
    translation271 = NXOpen.Vector3d(-1.4210854715202004e-14, -18.258037440673313, 29.960923030124157)
    rotation252 = NXOpen.Matrix3x3()
    
    rotation252.Xx = 1.0
    rotation252.Xy = 2.6235136710381023e-15
    rotation252.Xz = -6.5378322454324121e-16
    rotation252.Yx = -4.3213759279949084e-16
    rotation252.Yy = 0.42261826174070072
    rotation252.Yz = 0.90630778703665005
    rotation252.Zx = 2.6429424723527787e-15
    rotation252.Zy = -0.9063077870366496
    rotation252.Zz = 0.42261826174070088
    componentNetwork13.DragByTransform(translation271, rotation252)
    
    translation272 = NXOpen.Vector3d(-1.4210854715202004e-14, -18.190537121642414, 27.113366555567822)
    rotation253 = NXOpen.Matrix3x3()
    
    rotation253.Xx = 1.0
    rotation253.Xy = 2.4125264594912506e-15
    rotation253.Xz = -7.1431005618727693e-16
    rotation253.Yx = -5.0903612858932125e-16
    rotation253.Yy = 0.50000000000000122
    rotation253.Yz = 0.86602540378443882
    rotation253.Zx = 2.4395861814955428e-15
    rotation253.Zy = -0.86602540378443826
    rotation253.Zz = 0.50000000000000133
    componentNetwork13.DragByTransform(translation272, rotation253)
    
    translation273 = NXOpen.Vector3d(-2.8421709430404007e-14, -17.875112762148461, 24.282528933538824)
    rotation254 = NXOpen.Matrix3x3()
    
    rotation254.Xx = 1.0
    rotation254.Xy = 2.1970668570150172e-15
    rotation254.Xz = -7.5621781783073377e-16
    rotation254.Yx = -5.679183736620969e-16
    rotation254.Yy = 0.57357643635104738
    rotation254.Yz = 0.81915204428899191
    rotation254.Zx = 2.2303015737169908e-15
    rotation254.Zy = -0.81915204428899135
    rotation254.Zz = 0.57357643635104738
    componentNetwork13.DragByTransform(translation273, rotation254)
    
    translation274 = NXOpen.Vector3d(-1.4210854715202004e-14, -17.314164932025648, 21.489954547647287)
    rotation255 = NXOpen.Matrix3x3()
    
    rotation255.Xx = 1.0
    rotation255.Xy = 1.9787746412823111e-15
    rotation255.Xz = -7.7918756610290682e-16
    rotation255.Yx = -6.0833619857874306e-16
    rotation255.Yy = 0.64278760968654058
    rotation255.Yz = 0.76604444311897812
    rotation255.Zx = 2.0166814312518201e-15
    rotation255.Zy = -0.76604444311897757
    rotation255.Zz = 0.64278760968654047
    componentNetwork13.DragByTransform(translation274, rotation255)
    
    translation275 = NXOpen.Vector3d(-1.4210854715202004e-14, -16.511962782970773, 18.75689657517237)
    rotation256 = NXOpen.Matrix3x3()
    
    rotation256.Xx = 1.0
    rotation256.Xy = 1.7593111478633018e-15
    rotation256.Xz = -7.8304448734993142e-16
    rotation256.Yx = -6.299819992866937e-16
    rotation256.Yy = 0.70710678118654868
    rotation256.Yz = 0.70710678118654746
    rotation256.Zx = 1.8003515323715583e-15
    rotation256.Zy = -0.70710678118654702
    rotation256.Zz = 0.70710678118654857
    componentNetwork13.DragByTransform(translation275, rotation256)
    
    translation276 = NXOpen.Vector3d(-1.4210854715202004e-14, -16.511962782970773, 18.75689657517237)
    rotation257 = NXOpen.Matrix3x3()
    
    rotation257.Xx = 1.0
    rotation257.Xy = 1.7593111478633018e-15
    rotation257.Xz = -7.8304448734993142e-16
    rotation257.Yx = -6.299819992866937e-16
    rotation257.Yy = 0.70710678118654868
    rotation257.Yz = 0.70710678118654746
    rotation257.Zx = 1.8003515323715583e-15
    rotation257.Zy = -0.70710678118654702
    rotation257.Zz = 0.70710678118654857
    componentNetwork13.DragByTransform(translation276, rotation257)
    
    componentNetwork13.EndDrag()
    
    componentNetwork13.ResetDisplay()
    
    componentNetwork13.ApplyToModel()
    
    componentNetwork13.Solve()
    
    componentPositioner13.ClearNetwork()
    
    nErrs30 = theSession.UpdateManager.AddToDeleteList(componentNetwork13)
    
    componentPositioner13.DeleteNonPersistentConstraints()
    
    nErrs31 = theSession.UpdateManager.DoUpdate(markId71)
    
    theSession.SetUndoMarkName(markId70, "Move Component")
    
    componentPositioner13.EndMoveComponent()
    
    componentPositioner13.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMarksUpToMark(markId71, None, False)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId73 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId74 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner14 = workPart.ComponentAssembly.Positioner
    
    componentPositioner14.ClearNetwork()
    
    componentPositioner14.PrimaryArrangement = arrangement1
    
    componentPositioner14.BeginAssemblyConstraints()
    
    allowInterpartPositioning13 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression136 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression137 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression138 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression139 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression140 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression141 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression142 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression143 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network14 = componentPositioner14.EstablishNetwork()
    
    componentNetwork14 = network14
    componentNetwork14.MoveObjectsState = True
    
    componentNetwork14.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork14.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId74, "Assembly Constraints Dialog")
    
    componentNetwork14.MoveObjectsState = True
    
    componentNetwork14.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId75 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    line5 = workPart.Lines.CreateFaceAxis(face3, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line5.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    objects5 = [NXOpen.TaggedObject.Null] * 1 
    objects5[0] = line5
    nErrs32 = theSession.UpdateManager.AddObjectsToDeleteList(objects5)
    
    componentPositioner14.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner14.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId75, None)
    
    theSession.UndoToMark(markId74, None)
    
    theSession.DeleteUndoMark(markId74, None)
    
    theSession.DeleteUndoMark(markId73, None)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId76 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId77 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner15 = workPart.ComponentAssembly.Positioner
    
    componentPositioner15.ClearNetwork()
    
    componentPositioner15.PrimaryArrangement = arrangement1
    
    componentPositioner15.BeginAssemblyConstraints()
    
    allowInterpartPositioning14 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression144 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression145 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression146 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression147 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression148 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression149 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression150 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression151 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network15 = componentPositioner15.EstablishNetwork()
    
    componentNetwork15 = network15
    componentNetwork15.MoveObjectsState = True
    
    componentNetwork15.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork15.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId77, "Assembly Constraints Dialog")
    
    componentNetwork15.MoveObjectsState = True
    
    componentNetwork15.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId78 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    rotMatrix15 = NXOpen.Matrix3x3()
    
    rotMatrix15.Xx = 0.67287762280305607
    rotMatrix15.Xy = -0.68044401022705636
    rotMatrix15.Xz = 0.29022690033320531
    rotMatrix15.Yx = -0.03370683054446575
    rotMatrix15.Yy = 0.3637200698649754
    rotMatrix15.Yz = 0.93089825456494546
    rotMatrix15.Zx = -0.73898548991542889
    rotMatrix15.Zy = -0.63616323355215254
    rotMatrix15.Zz = 0.22180348502878672
    translation277 = NXOpen.Point3d(7.0829558615990322, -43.626880590060424, 104.2947701482927)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix15, translation277, 2.6634420161944896)
    
    markId79 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint6 = componentPositioner15.CreateConstraint(True)
    
    componentConstraint6 = constraint6
    componentConstraint6.ConstraintType = NXOpen.Positioning.Constraint.Type.Distance
    
    face4 = component8.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 170 {(3,2.8,21) EXTRUDE(2)}")
    constraintReference10 = componentConstraint6.CreateConstraintReference(component8, face4, False, False, False)
    
    helpPoint9 = NXOpen.Point3d(70.393242532218039, 18.537239564457764, 21.753331677193572)
    constraintReference10.HelpPoint = helpPoint9
    
    face5 = component6.FindObject("PROTO#.Features|EXTRUDE(6)|FACE 440 {(63,-53,-5) EXTRUDE(6)5}")
    constraintReference11 = componentConstraint6.CreateConstraintReference(component6, face5, False, False, False)
    
    helpPoint10 = NXOpen.Point3d(71.34324253234071, 5.3146535126788601, 63.272308338291175)
    constraintReference11.HelpPoint = helpPoint10
    
    constraintReference11.SetFixHint(True)
    
    componentConstraint6.SetExpression("0")
    
    componentConstraint6.SetExpression("0.949999999999881")
    
    componentNetwork15.Solve()
    
    scaleAboutPoint50 = NXOpen.Point3d(-11.920664991747836, 15.596203364203529, 0.0)
    viewCenter50 = NXOpen.Point3d(11.920664991747888, -15.596203364203376, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint50, viewCenter50)
    
    rotMatrix16 = NXOpen.Matrix3x3()
    
    rotMatrix16.Xx = 0.97272422029821437
    rotMatrix16.Xy = -0.20194755353851399
    rotMatrix16.Xz = 0.11412614452889921
    rotMatrix16.Yx = -0.03370683054446575
    rotMatrix16.Yy = 0.3637200698649754
    rotMatrix16.Yz = 0.93089825456494546
    rotMatrix16.Zx = -0.22950259436413609
    rotMatrix16.Zy = -0.90935410946298478
    rotMatrix16.Zz = 0.34699230940022896
    translation278 = NXOpen.Point3d(-35.601299591351911, -39.727829749009558, 82.334282943192335)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix16, translation278, 2.130753612955592)
    
    constraintReference10.SetFixHint(False)
    
    constraintReference11.SetFixHint(True)
    
    componentNetwork15.AddConstraint(componentConstraint6)
    
    expression152 = workPart.Expressions.FindObject("p8")
    expression152.RightHandSide = "1"
    
    componentNetwork15.Solve()
    
    markId80 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs33 = theSession.UpdateManager.DoUpdate(markId78)
    
    componentNetwork15.Solve()
    
    componentPositioner15.ClearNetwork()
    
    nErrs34 = theSession.UpdateManager.AddToDeleteList(componentNetwork15)
    
    componentPositioner15.DeleteNonPersistentConstraints()
    
    nErrs35 = theSession.UpdateManager.DoUpdate(markId78)
    
    theSession.DeleteUndoMark(markId80, None)
    
    theSession.SetUndoMarkName(markId77, "Assembly Constraints")
    
    componentPositioner15.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner15.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId78, None)
    
    theSession.DeleteUndoMark(markId79, None)
    
    markId81 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner16 = workPart.ComponentAssembly.Positioner
    
    componentPositioner16.ClearNetwork()
    
    componentPositioner16.PrimaryArrangement = arrangement1
    
    componentPositioner16.BeginAssemblyConstraints()
    
    allowInterpartPositioning15 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression153 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression154 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression155 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression156 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression157 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression158 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression159 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression160 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network16 = componentPositioner16.EstablishNetwork()
    
    componentNetwork16 = network16
    componentNetwork16.MoveObjectsState = True
    
    componentNetwork16.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork16.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId81, "Assembly Constraints Dialog")
    
    componentNetwork16.MoveObjectsState = True
    
    componentNetwork16.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId82 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   Dialog Begin Assembly Constraints
    # ----------------------------------------------
    scaleAboutPoint51 = NXOpen.Point3d(11.920664991747872, -2.8559926542728582, 0.0)
    viewCenter51 = NXOpen.Point3d(-11.92066499174785, 2.8559926542730061, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint51, viewCenter51)
    
    rotMatrix17 = NXOpen.Matrix3x3()
    
    rotMatrix17.Xx = 0.8101241218883285
    rotMatrix17.Xy = 0.55311887995338449
    rotMatrix17.Xz = -0.1943152381409598
    rotMatrix17.Yx = -0.061071411618538844
    rotMatrix17.Yy = 0.40926792259403327
    rotMatrix17.Yz = 0.91036808501752953
    rotMatrix17.Zx = 0.58306876937251872
    rotMatrix17.Zy = -0.72564403957772405
    rotMatrix17.Zz = 0.36533756720016969
    translation279 = NXOpen.Point3d(-53.300163104014601, -40.488571056200861, 19.02476980855667)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix17, translation279, 1.7046028903644737)
    
    componentPositioner16.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner16.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId82, None)
    
    theSession.UndoToMark(markId81, None)
    
    theSession.DeleteUndoMark(markId81, None)
    
    theSession.DeleteUndoMark(markId76, None)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId83 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId84 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner17 = workPart.ComponentAssembly.Positioner
    
    componentPositioner17.ClearNetwork()
    
    componentPositioner17.PrimaryArrangement = arrangement1
    
    componentPositioner17.BeginAssemblyConstraints()
    
    allowInterpartPositioning16 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression161 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression162 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression163 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression164 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression165 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression166 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression167 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression168 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network17 = componentPositioner17.EstablishNetwork()
    
    componentNetwork17 = network17
    componentNetwork17.MoveObjectsState = True
    
    componentNetwork17.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork17.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId84, "Assembly Constraints Dialog")
    
    componentNetwork17.MoveObjectsState = True
    
    componentNetwork17.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId85 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    line6 = workPart.Lines.CreateFaceAxis(face3, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects6 = [NXOpen.TaggedObject.Null] * 1 
    objects6[0] = line6
    nErrs36 = theSession.UpdateManager.AddObjectsToDeleteList(objects6)
    
    scaleAboutPoint52 = NXOpen.Point3d(9.3130195248030443, -3.259556833680977, 0.0)
    viewCenter52 = NXOpen.Point3d(-9.3130195248030176, 3.2595568336811223, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint52, viewCenter52)
    
    scaleAboutPoint53 = NXOpen.Point3d(11.059210685703581, -3.1043398416009444, 0.0)
    viewCenter53 = NXOpen.Point3d(-11.059210685703581, 3.1043398416010768, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint53, viewCenter53)
    
    rotMatrix18 = NXOpen.Matrix3x3()
    
    rotMatrix18.Xx = 0.75124671551832212
    rotMatrix18.Xy = -0.58846955439830939
    rotMatrix18.Xz = 0.29888451945389743
    rotMatrix18.Yx = -0.077227853320857659
    rotMatrix18.Yy = 0.37135738126582668
    rotMatrix18.Yz = 0.92527269172435833
    rotMatrix18.Zx = -0.65548778104125216
    rotMatrix18.Zy = -0.71819028044498168
    rotMatrix18.Zz = 0.23353477252857444
    translation280 = NXOpen.Point3d(1.5772248783352083, -39.458219763781464, 103.15499304551706)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix18, translation280, 1.0909458498332634)
    
    scaleAboutPoint54 = NXOpen.Point3d(61.116690631519788, 12.126327506253981, 0.0)
    viewCenter54 = NXOpen.Point3d(-61.116690631519788, -12.126327506253856, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint54, viewCenter54)
    
    scaleAboutPoint55 = NXOpen.Point3d(49.087373745315887, 9.7010620050032195, 0.0)
    viewCenter55 = NXOpen.Point3d(-49.087373745315887, -9.7010620050030703, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint55, viewCenter55)
    
    scaleAboutPoint56 = NXOpen.Point3d(39.269898996252678, 7.7608496040025878, 0.0)
    viewCenter56 = NXOpen.Point3d(-39.269898996252735, -7.7608496040024422, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint56, viewCenter56)
    
    face6 = component6.FindObject("PROTO#.Features|SIMPLE HOLE(16:1A)|FACE 3 {(64,-51.5,-6) EXTRUDE(6)5}")
    line7 = workPart.Lines.CreateFaceAxis(face6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scaleAboutPoint57 = NXOpen.Point3d(39.487202785164762, 8.6921515564828766, 0.0)
    viewCenter57 = NXOpen.Point3d(-39.487202785164804, -8.6921515564827381, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint57, viewCenter57)
    
    scaleAboutPoint58 = NXOpen.Point3d(31.589762228131789, 6.9537212451863164, 0.0)
    viewCenter58 = NXOpen.Point3d(-31.589762228131857, -6.9537212451861814, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint58, viewCenter58)
    
    scaleAboutPoint59 = NXOpen.Point3d(25.271809782505432, 5.56297699614906, 0.0)
    viewCenter59 = NXOpen.Point3d(-25.271809782505485, -5.5629769961489313, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint59, viewCenter59)
    
    scaleAboutPoint60 = NXOpen.Point3d(20.217447826004335, 4.4503815969192537, 0.0)
    viewCenter60 = NXOpen.Point3d(-20.217447826004399, -4.4503815969191454, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint60, viewCenter60)
    
    markId86 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint7 = componentPositioner17.CreateConstraint(True)
    
    componentConstraint7 = constraint7
    componentConstraint7.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge9 = component8.FindObject("PROTO#.Features|EXTRUDE(2)|EDGE * 170 SIMPLE HOLE(4:1A) 3 {(2.25,2.8,4.2990381056767)(4.5,2.8,3)(2.25,2.8,1.7009618943233) EXTRUDE(2)}")
    constraintReference12 = componentConstraint7.CreateConstraintReference(component8, edge9, False, False, False)
    
    helpPoint11 = NXOpen.Point3d(70.393242532238716, 41.42315366957078, 13.038408848803144)
    constraintReference12.HelpPoint = helpPoint11
    
    edge10 = component6.FindObject("PROTO#.Features|EXTRUDE(6)|EDGE * 440 SIMPLE HOLE(16:1A) 3 {(63,-53.75,-4.7009618943233)(63,-51.5,-6)(63,-53.75,-7.2990381056767) EXTRUDE(6)5}")
    constraintReference13 = componentConstraint7.CreateConstraintReference(component6, edge10, False, False, False)
    
    helpPoint12 = NXOpen.Point3d(71.343242532238705, 7.2942549248301152, 62.116453184014858)
    constraintReference13.HelpPoint = helpPoint12
    
    constraintReference13.SetFixHint(True)
    
    objects7 = [NXOpen.TaggedObject.Null] * 1 
    objects7[0] = line7
    nErrs37 = theSession.UpdateManager.AddObjectsToDeleteList(objects7)
    
    componentNetwork17.Solve()
    
    markId87 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    theSession.DeleteUndoMark(markId87, None)
    
    markId88 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs38 = theSession.UpdateManager.DoUpdate(markId85)
    
    componentNetwork17.Solve()
    
    componentPositioner17.ClearNetwork()
    
    nErrs39 = theSession.UpdateManager.AddToDeleteList(componentNetwork17)
    
    componentPositioner17.DeleteNonPersistentConstraints()
    
    nErrs40 = theSession.UpdateManager.DoUpdate(markId85)
    
    theSession.DeleteUndoMark(markId88, None)
    
    theSession.SetUndoMarkName(markId84, "Assembly Constraints")
    
    componentPositioner17.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner17.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId85, None)
    
    theSession.DeleteUndoMark(markId86, None)
    
    theSession.DeleteUndoMark(markId83, None)
    
    scaleAboutPoint61 = NXOpen.Point3d(0.35603052775349836, -2.3396291823803241, 0.0)
    viewCenter61 = NXOpen.Point3d(-0.35603052775356775, 2.3396291823804369, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint61, viewCenter61)
    
    scaleAboutPoint62 = NXOpen.Point3d(0.44503815969188393, -2.9881133579314128, 0.0)
    viewCenter62 = NXOpen.Point3d(-0.44503815969194893, 2.9881133579315211, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint62, viewCenter62)
    
    scaleAboutPoint63 = NXOpen.Point3d(1.0331242992847689, -4.1324971971392044, 0.0)
    viewCenter63 = NXOpen.Point3d(-1.0331242992848502, 4.1324971971393127, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint63, viewCenter63)
    
    scaleAboutPoint64 = NXOpen.Point3d(1.2914053741059781, -5.1656214964240057, 0.0)
    viewCenter64 = NXOpen.Point3d(-1.2914053741060458, 5.1656214964241247, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint64, viewCenter64)
    
    scaleAboutPoint65 = NXOpen.Point3d(1.7384303112965058, -6.5812004641940831, 0.0)
    viewCenter65 = NXOpen.Point3d(-1.7384303112965693, 6.5812004641941888, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint65, viewCenter65)
    
    rotMatrix19 = NXOpen.Matrix3x3()
    
    rotMatrix19.Xx = 0.99719721600980682
    rotMatrix19.Xy = -0.066263180473612168
    rotMatrix19.Xz = -0.034740513752763866
    rotMatrix19.Yx = 0.041911085984103279
    rotMatrix19.Yy = 0.11009110098163338
    rotMatrix19.Yz = 0.99303746674346616
    rotMatrix19.Zx = -0.061977199468172331
    rotMatrix19.Zy = -0.99171020988904002
    rotMatrix19.Zz = 0.11255970126074789
    translation281 = NXOpen.Point3d(-82.158632557009554, -51.652091245422042, 84.813589540455027)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix19, translation281, 1.7046028903644743)
    
    scaleAboutPoint66 = NXOpen.Point3d(-4.0356417940813403, -2.9491228495209052, 0.0)
    viewCenter66 = NXOpen.Point3d(4.0356417940812737, 2.9491228495210242, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint66, viewCenter66)
    
    scaleAboutPoint67 = NXOpen.Point3d(-3.2285134352650937, -2.3592982796167137, 0.0)
    viewCenter67 = NXOpen.Point3d(3.2285134352650515, 2.35929827961683, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint67, viewCenter67)
    
    scaleAboutPoint68 = NXOpen.Point3d(-2.5828107482120748, -1.8874386236933456, 0.0)
    viewCenter68 = NXOpen.Point3d(2.5828107482120242, 1.8874386236934726, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint68, viewCenter68)
    
    scaleAboutPoint69 = NXOpen.Point3d(-2.0662485985696599, -1.5099508989546764, 0.0)
    viewCenter69 = NXOpen.Point3d(2.066248598569592, 1.5099508989547916, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint69, viewCenter69)
    
    markId89 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId90 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner18 = workPart.ComponentAssembly.Positioner
    
    componentPositioner18.ClearNetwork()
    
    componentPositioner18.PrimaryArrangement = arrangement1
    
    componentPositioner18.BeginAssemblyConstraints()
    
    allowInterpartPositioning17 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression169 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression170 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression171 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression172 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression173 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression174 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression175 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression176 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network18 = componentPositioner18.EstablishNetwork()
    
    componentNetwork18 = network18
    componentNetwork18.MoveObjectsState = True
    
    componentNetwork18.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork18.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId90, "Assembly Constraints Dialog")
    
    componentNetwork18.AddConstraint(componentConstraint6)
    
    loaded14 = componentNetwork18.IsReferencedGeometryLoaded()
    
    componentNetwork18.AddConstraint(componentConstraint6)
    
    loaded15 = componentNetwork18.IsReferencedGeometryLoaded()
    
    componentNetwork18.MoveObjectsState = True
    
    componentNetwork18.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId91 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   Dialog Begin Assembly Constraints
    # ----------------------------------------------
    constraintReference10.SetFixHint(False)
    
    constraintReference11.SetFixHint(True)
    
    componentNetwork18.AddConstraint(componentConstraint6)
    
    expression152.RightHandSide = "1"
    
    componentNetwork18.Solve()
    
    constraintReference10.SetFixHint(False)
    
    constraintReference11.SetFixHint(True)
    
    componentNetwork18.AddConstraint(componentConstraint6)
    
    expression152.RightHandSide = "1.5"
    
    componentNetwork18.Solve()
    
    markId92 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    theSession.DeleteUndoMark(markId92, None)
    
    markId93 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs41 = theSession.UpdateManager.DoUpdate(markId91)
    
    componentNetwork18.Solve()
    
    componentPositioner18.ClearNetwork()
    
    nErrs42 = theSession.UpdateManager.AddToDeleteList(componentNetwork18)
    
    componentPositioner18.DeleteNonPersistentConstraints()
    
    nErrs43 = theSession.UpdateManager.DoUpdate(markId91)
    
    theSession.DeleteUndoMark(markId93, None)
    
    theSession.SetUndoMarkName(markId90, "Assembly Constraints")
    
    componentPositioner18.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner18.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId91, None)
    
    theSession.DeleteUndoMark(markId89, None)
    
    scaleAboutPoint70 = NXOpen.Point3d(-6.1033804757749346, 2.6066520781955886, 0.0)
    viewCenter70 = NXOpen.Point3d(6.1033804757748689, -2.6066520781954643, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint70, viewCenter70)
    
    scaleAboutPoint71 = NXOpen.Point3d(-7.6292255947186538, 3.2583150977444721, 0.0)
    viewCenter71 = NXOpen.Point3d(7.6292255947185987, -3.25831509774435, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint71, viewCenter71)
    
    scaleAboutPoint72 = NXOpen.Point3d(-9.5365319933983024, 3.8742161223181211, 0.0)
    viewCenter72 = NXOpen.Point3d(9.5365319933982668, -3.8742161223179852, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint72, viewCenter72)
    
    scaleAboutPoint73 = NXOpen.Point3d(-11.672317804419778, 4.0977285909133991, 0.0)
    viewCenter73 = NXOpen.Point3d(11.672317804419768, -4.0977285909132615, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint73, viewCenter73)
    
    rotMatrix20 = NXOpen.Matrix3x3()
    
    rotMatrix20.Xx = 0.39767334839444679
    rotMatrix20.Xy = -0.91606678295531951
    rotMatrix20.Xz = 0.051745117089767124
    rotMatrix20.Yx = 0.049630535908386321
    rotMatrix20.Yy = 0.07779028397269841
    rotMatrix20.Yz = 0.99573363989818664
    rotMatrix20.Zx = -0.91618377953453589
    rotMatrix20.Zy = -0.39340859279549451
    rotMatrix20.Zz = 0.076400008065921773
    translation282 = NXOpen.Point3d(-6.4927405743264419, -45.269132820494356, 108.01873156094481)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix20, translation282, 1.7046028903644748)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Components->Add Component...
    # ----------------------------------------------
    markId94 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder5 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner19 = workPart.ComponentAssembly.Positioner
    
    componentPositioner19.ClearNetwork()
    
    componentPositioner19.PrimaryArrangement = arrangement1
    
    componentPositioner19.BeginAssemblyConstraints()
    
    allowInterpartPositioning18 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression177 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression178 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression179 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression180 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression181 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression182 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression183 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression184 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network19 = componentPositioner19.EstablishNetwork()
    
    componentNetwork19 = network19
    componentNetwork19.MoveObjectsState = True
    
    componentNetwork19.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId94, "Add Component Dialog")
    
    componentNetwork19.MoveObjectsState = True
    
    markId95 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder5.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder5.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder5.SetCount(1)
    
    addComponentBuilder5.SetScatterOption(True)
    
    addComponentBuilder5.ReferenceSet = "Unknown"
    
    addComponentBuilder5.Layer = -1
    
    addComponentBuilder5.ReferenceSet = "Use Model"
    
    addComponentBuilder5.Layer = -1
    
    partstouse5 = [NXOpen.BasePart.Null] * 1 
    partstouse5[0] = part2
    addComponentBuilder5.SetPartsToAdd(partstouse5)
    
    productinterfaceobjects5 = addComponentBuilder5.GetAllProductInterfaceObjects()
    
    scaleAboutPoint74 = NXOpen.Point3d(-57.119853085458494, -21.730378891206978, 0.0)
    viewCenter74 = NXOpen.Point3d(57.119853085458445, 21.730378891207099, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint74, viewCenter74)
    
    scaleAboutPoint75 = NXOpen.Point3d(-45.695882468366811, -17.508476706629612, 0.0)
    viewCenter75 = NXOpen.Point3d(45.695882468366769, 17.508476706629725, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint75, viewCenter75)
    
    scaleAboutPoint76 = NXOpen.Point3d(-36.457367099762209, -14.106120240234906, 0.0)
    viewCenter76 = NXOpen.Point3d(36.457367099762166, 14.106120240235033, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint76, viewCenter76)
    
    scaleAboutPoint77 = NXOpen.Point3d(-29.165893679809781, -11.364367292132906, 0.0)
    viewCenter77 = NXOpen.Point3d(29.165893679809741, 11.364367292133014, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint77, viewCenter77)
    
    scaleAboutPoint78 = NXOpen.Point3d(-23.269138063891845, -9.4729551134422447, 0.0)
    viewCenter78 = NXOpen.Point3d(23.269138063891791, 9.4729551134423584, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint78, viewCenter78)
    
    coordinates6 = NXOpen.Point3d(12.393242532238844, 60.892490337762325, 21.0)
    point249 = workPart.Points.CreatePoint(coordinates6)
    
    origin16 = NXOpen.Point3d(12.393242532238844, 60.892490337762325, 21.0)
    vector7 = NXOpen.Vector3d(-0.0, -1.0, -0.0)
    direction246 = workPart.Directions.CreateDirection(origin16, vector7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin17 = NXOpen.Point3d(12.393242532238844, 60.892490337762325, 21.0)
    vector8 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction247 = workPart.Directions.CreateDirection(origin17, vector8, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin18 = NXOpen.Point3d(12.393242532238844, 60.892490337762325, 21.0)
    matrix4 = NXOpen.Matrix3x3()
    
    matrix4.Xx = 1.0
    matrix4.Xy = 0.0
    matrix4.Xz = 0.0
    matrix4.Yx = -0.0
    matrix4.Yy = 0.0
    matrix4.Yz = 1.0
    matrix4.Zx = 0.0
    matrix4.Zy = -1.0
    matrix4.Zz = 0.0
    plane4 = workPart.Planes.CreateFixedTypePlane(origin18, matrix4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform4 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane4, direction247, point249, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem4 = workPart.CoordinateSystems.CreateCoordinateSystem(xform4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point250 = NXOpen.Point3d(12.393242532238844, 60.892490337762325, 21.0)
    orientation4 = NXOpen.Matrix3x3()
    
    orientation4.Xx = 1.0
    orientation4.Xy = 0.0
    orientation4.Xz = 0.0
    orientation4.Yx = -0.0
    orientation4.Yy = 0.0
    orientation4.Yz = 1.0
    orientation4.Zx = 0.0
    orientation4.Zy = -1.0
    orientation4.Zz = 0.0
    addComponentBuilder5.SetInitialLocationAndOrientation(point250, orientation4)
    
    movableObjects11 = [NXOpen.NXObject.Null] * 1 
    component9 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT s_link 1")
    movableObjects11[0] = component9
    componentNetwork19.SetMovingGroup(movableObjects11)
    
    markId96 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    theSession.DeleteUndoMark(markId96, None)
    
    markId97 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId98 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork19.Solve()
    
    componentPositioner19.ClearNetwork()
    
    nErrs44 = theSession.UpdateManager.AddToDeleteList(componentNetwork19)
    
    nErrs45 = theSession.UpdateManager.DoUpdate(markId95)
    
    componentPositioner19.EndAssemblyConstraints()
    
    logicalobjects5 = addComponentBuilder5.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder5.ComponentName = "S_LINK"
    
    nXObject6 = addComponentBuilder5.Commit()
    
    errorList5 = addComponentBuilder5.GetOperationFailures()
    
    errorList5.Dispose()
    theSession.DeleteUndoMark(markId97, None)
    
    theSession.SetUndoMarkName(markId94, "Add Component")
    
    addComponentBuilder5.Destroy()
    
    componentPositioner19.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId95, None)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId99 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId100 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner20 = workPart.ComponentAssembly.Positioner
    
    componentPositioner20.ClearNetwork()
    
    componentPositioner20.PrimaryArrangement = arrangement1
    
    componentPositioner20.BeginAssemblyConstraints()
    
    allowInterpartPositioning19 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression185 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression186 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression187 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression188 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression189 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression190 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression191 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression192 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network20 = componentPositioner20.EstablishNetwork()
    
    componentNetwork20 = network20
    componentNetwork20.MoveObjectsState = True
    
    componentNetwork20.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork20.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId100, "Assembly Constraints Dialog")
    
    componentNetwork20.MoveObjectsState = True
    
    componentNetwork20.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId101 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    component10 = nXObject6
    face7 = component10.FindObject("PROTO#.Features|EXTRUDE(4)|FACE 160 {(4.5,3,1.4) EXTRUDE(2)}")
    line8 = workPart.Lines.CreateFaceAxis(face7, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    face8 = component10.FindObject("PROTO#.Features|EXTRUDE(4)|FACE 170 {(13.5,3,1.4) EXTRUDE(2)}")
    line9 = workPart.Lines.CreateFaceAxis(face8, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects8 = [NXOpen.TaggedObject.Null] * 1 
    objects8[0] = line9
    nErrs46 = theSession.UpdateManager.AddObjectsToDeleteList(objects8)
    
    objects9 = [NXOpen.TaggedObject.Null] * 1 
    objects9[0] = line8
    nErrs47 = theSession.UpdateManager.AddObjectsToDeleteList(objects9)
    
    face9 = component2.FindObject("PROTO#.Features|SIMPLE HOLE(12:1A)|FACE 3 {(7,65.25,19.5) EXTRUDE(4)1}")
    line10 = workPart.Lines.CreateFaceAxis(face9, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId102 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint8 = componentPositioner20.CreateConstraint(True)
    
    componentConstraint8 = constraint8
    componentConstraint8.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge11 = component10.FindObject("PROTO#.Features|EXTRUDE(2)|EDGE * 130 EXTRUDE(4) 170 {(11.25,1.7009618943233,2.8)(13.5,3,2.8)(11.25,4.2990381056767,2.8) EXTRUDE(2)}")
    constraintReference14 = componentConstraint8.CreateConstraintReference(component10, edge11, False, False, False)
    
    helpPoint13 = NXOpen.Point3d(25.522277965292133, 58.092490337762328, 24.987562145340828)
    constraintReference14.HelpPoint = helpPoint13
    
    edge12 = component2.FindObject("PROTO#.Features|EXTRUDE(4)|EDGE * 170 SIMPLE HOLE(12:1A) 3 {(8.2990381056766,64.5,20.25)(7,64.5,22.5)(5.7009618943233,64.5,20.25) EXTRUDE(4)1}")
    constraintReference15 = componentConstraint8.CreateConstraintReference(component2, edge12, False, False, False)
    
    helpPoint14 = NXOpen.Point3d(11.643808357048997, 60.892490337762325, 19.700635379480605)
    constraintReference15.HelpPoint = helpPoint14
    
    constraintReference15.SetFixHint(True)
    
    objects10 = [NXOpen.TaggedObject.Null] * 1 
    objects10[0] = line10
    nErrs48 = theSession.UpdateManager.AddObjectsToDeleteList(objects10)
    
    componentNetwork20.Solve()
    
    markId103 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs49 = theSession.UpdateManager.DoUpdate(markId101)
    
    componentNetwork20.Solve()
    
    componentPositioner20.ClearNetwork()
    
    nErrs50 = theSession.UpdateManager.AddToDeleteList(componentNetwork20)
    
    componentPositioner20.DeleteNonPersistentConstraints()
    
    nErrs51 = theSession.UpdateManager.DoUpdate(markId101)
    
    theSession.DeleteUndoMark(markId103, None)
    
    theSession.SetUndoMarkName(markId100, "Assembly Constraints")
    
    componentPositioner20.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner20.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId101, None)
    
    theSession.DeleteUndoMark(markId102, None)
    
    markId104 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner21 = workPart.ComponentAssembly.Positioner
    
    componentPositioner21.ClearNetwork()
    
    componentPositioner21.PrimaryArrangement = arrangement1
    
    componentPositioner21.BeginAssemblyConstraints()
    
    allowInterpartPositioning20 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression193 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression194 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression195 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression196 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression197 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression198 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression199 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression200 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network21 = componentPositioner21.EstablishNetwork()
    
    componentNetwork21 = network21
    componentNetwork21.MoveObjectsState = True
    
    componentNetwork21.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork21.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId104, "Assembly Constraints Dialog")
    
    componentNetwork21.MoveObjectsState = True
    
    componentNetwork21.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId105 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   Dialog Begin Assembly Constraints
    # ----------------------------------------------
    componentPositioner21.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner21.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId105, None)
    
    theSession.UndoToMark(markId104, None)
    
    theSession.DeleteUndoMark(markId104, None)
    
    theSession.DeleteUndoMark(markId99, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Undo
    # ----------------------------------------------
    marksRecycled1, undoUnavailable1 = theSession.UndoLastNVisibleMarks(1)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId106 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId107 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner22 = workPart.ComponentAssembly.Positioner
    
    componentPositioner22.ClearNetwork()
    
    componentPositioner22.PrimaryArrangement = arrangement1
    
    componentPositioner22.BeginAssemblyConstraints()
    
    allowInterpartPositioning21 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression201 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression202 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression203 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression204 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression205 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression206 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression207 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression208 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network22 = componentPositioner22.EstablishNetwork()
    
    componentNetwork22 = network22
    componentNetwork22.MoveObjectsState = True
    
    componentNetwork22.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork22.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId107, "Assembly Constraints Dialog")
    
    componentNetwork22.MoveObjectsState = True
    
    componentNetwork22.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId108 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    line11 = workPart.Lines.CreateFaceAxis(face8, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects11 = [NXOpen.TaggedObject.Null] * 1 
    objects11[0] = line11
    nErrs52 = theSession.UpdateManager.AddObjectsToDeleteList(objects11)
    
    rotMatrix21 = NXOpen.Matrix3x3()
    
    rotMatrix21.Xx = -0.17835113107216155
    rotMatrix21.Xy = -0.98024779643841631
    rotMatrix21.Xz = 0.085470062729061241
    rotMatrix21.Yx = 0.049630535908386411
    rotMatrix21.Yy = 0.077790283972698437
    rotMatrix21.Yz = 0.99573363989818764
    rotMatrix21.Zx = -0.98271444680065956
    rotMatrix21.Zy = 0.18183214593980887
    rotMatrix21.Zz = 0.034776238327298044
    translation283 = NXOpen.Point3d(71.055180058363746, -30.432673171765021, 82.159857883489337)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix21, translation283, 5.2020351878798685)
    
    markId109 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint9 = componentPositioner22.CreateConstraint(True)
    
    componentConstraint9 = constraint9
    componentConstraint9.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    constraintReference16 = componentConstraint9.CreateConstraintReference(component10, edge11, False, False, False)
    
    helpPoint15 = NXOpen.Point3d(25.837393098659891, 58.092490337762328, 24.405498633173735)
    constraintReference16.HelpPoint = helpPoint15
    
    edge13 = component2.FindObject("PROTO#.Features|EXTRUDE(4)|EDGE * 230 SIMPLE HOLE(10:1A) 3 {(8.2990381056766,61.6,21.75)(7,61.6,19.5)(5.7009618943233,61.6,21.75) EXTRUDE(4)}")
    constraintReference17 = componentConstraint9.CreateConstraintReference(component2, edge13, False, False, False)
    
    helpPoint16 = NXOpen.Point3d(13.285404809855567, 57.992490337762327, 19.79416150733287)
    constraintReference17.HelpPoint = helpPoint16
    
    constraintReference17.SetFixHint(True)
    
    componentNetwork22.Solve()
    
    line12 = workPart.Lines.CreateFaceAxis(face7, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId110 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    objects12 = [NXOpen.TaggedObject.Null] * 1 
    objects12[0] = line12
    nErrs53 = theSession.UpdateManager.AddObjectsToDeleteList(objects12)
    
    theSession.DeleteUndoMark(markId110, None)
    
    markId111 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs54 = theSession.UpdateManager.DoUpdate(markId108)
    
    componentNetwork22.Solve()
    
    componentPositioner22.ClearNetwork()
    
    nErrs55 = theSession.UpdateManager.AddToDeleteList(componentNetwork22)
    
    componentPositioner22.DeleteNonPersistentConstraints()
    
    nErrs56 = theSession.UpdateManager.DoUpdate(markId108)
    
    theSession.DeleteUndoMark(markId111, None)
    
    theSession.SetUndoMarkName(markId107, "Assembly Constraints")
    
    componentPositioner22.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner22.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId108, None)
    
    theSession.DeleteUndoMark(markId109, None)
    
    theSession.DeleteUndoMark(markId106, None)
    
    scaleAboutPoint79 = NXOpen.Point3d(4.9844273885494603, -2.1870446704859505, 0.0)
    viewCenter79 = NXOpen.Point3d(-4.984427388549534, 2.1870446704860589, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint79, viewCenter79)
    
    rotMatrix22 = NXOpen.Matrix3x3()
    
    rotMatrix22.Xx = 0.86611995446926082
    rotMatrix22.Xy = -0.49975968991772529
    rotMatrix22.Xz = -0.0087451016862055801
    rotMatrix22.Yx = 0.064542112838409313
    rotMatrix22.Yy = 0.094472482604904373
    rotMatrix22.Yz = 0.9934330705693365
    rotMatrix22.Zx = -0.49565163183481725
    rotMatrix22.Zy = -0.86099663318958708
    rotMatrix22.Zz = 0.11408004863111619
    translation284 = NXOpen.Point3d(-17.600965805690223, -32.767966787135421, 105.37437525712572)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix22, translation284, 4.161628150303895)
    
    scaleAboutPoint80 = NXOpen.Point3d(-15.004143669613324, 2.3523445583716351, 0.0)
    viewCenter80 = NXOpen.Point3d(15.004143669613269, -2.3523445583715215, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint80, viewCenter80)
    
    scaleAboutPoint81 = NXOpen.Point3d(-18.755179587016649, 2.9404306979645227, 0.0)
    viewCenter81 = NXOpen.Point3d(18.755179587016581, -2.9404306979644144, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint81, viewCenter81)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Components->Add Component...
    # ----------------------------------------------
    markId112 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder6 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner23 = workPart.ComponentAssembly.Positioner
    
    componentPositioner23.ClearNetwork()
    
    componentPositioner23.PrimaryArrangement = arrangement1
    
    componentPositioner23.BeginAssemblyConstraints()
    
    allowInterpartPositioning22 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression209 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression210 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression211 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression212 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression213 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression214 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression215 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression216 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network23 = componentPositioner23.EstablishNetwork()
    
    componentNetwork23 = network23
    componentNetwork23.MoveObjectsState = True
    
    componentNetwork23.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId112, "Add Component Dialog")
    
    componentNetwork23.MoveObjectsState = True
    
    markId113 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder6.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder6.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder6.SetCount(1)
    
    addComponentBuilder6.SetScatterOption(True)
    
    addComponentBuilder6.ReferenceSet = "Unknown"
    
    addComponentBuilder6.Layer = -1
    
    addComponentBuilder6.ReferenceSet = "Use Model"
    
    addComponentBuilder6.Layer = -1
    
    partstouse6 = [NXOpen.BasePart.Null] * 1 
    partstouse6[0] = part4
    addComponentBuilder6.SetPartsToAdd(partstouse6)
    
    productinterfaceobjects6 = addComponentBuilder6.GetAllProductInterfaceObjects()
    
    partstoremove1 = [NXOpen.BasePart.Null] * 1 
    partstoremove1[0] = part4
    addComponentBuilder6.RemovePartsFromSelection(partstoremove1)
    
    partstouse7 = []
    addComponentBuilder6.SetPartsToAdd(partstouse7)
    
    productinterfaceobjects7 = addComponentBuilder6.GetAllProductInterfaceObjects()
    
    addComponentBuilder6.ReferenceSet = "Use Model"
    
    addComponentBuilder6.Layer = -1
    
    partstouse8 = [NXOpen.BasePart.Null] * 1 
    partstouse8[0] = part4
    addComponentBuilder6.SetPartsToAdd(partstouse8)
    
    productinterfaceobjects8 = addComponentBuilder6.GetAllProductInterfaceObjects()
    
    coordinates7 = NXOpen.Point3d(12.343242532238841, 62.292490337762466, 57.0)
    point251 = workPart.Points.CreatePoint(coordinates7)
    
    origin19 = NXOpen.Point3d(12.343242532238841, 62.292490337762466, 57.0)
    vector9 = NXOpen.Vector3d(-2.3852447794681098e-15, -1.0, -2.6481536735324493e-31)
    direction248 = workPart.Directions.CreateDirection(origin19, vector9, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin20 = NXOpen.Point3d(12.343242532238841, 62.292490337762466, 57.0)
    vector10 = NXOpen.Vector3d(1.0, -2.3852447794681098e-15, 1.1102230246251565e-16)
    direction249 = workPart.Directions.CreateDirection(origin20, vector10, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin21 = NXOpen.Point3d(12.343242532238841, 62.292490337762466, 57.0)
    matrix5 = NXOpen.Matrix3x3()
    
    matrix5.Xx = 1.0
    matrix5.Xy = -2.3852447794681098e-15
    matrix5.Xz = 1.1102230246251565e-16
    matrix5.Yx = -1.1102230246251565e-16
    matrix5.Yy = 0.0
    matrix5.Yz = 1.0
    matrix5.Zx = -2.3852447794681098e-15
    matrix5.Zy = -1.0
    matrix5.Zz = -2.6481536735324493e-31
    plane5 = workPart.Planes.CreateFixedTypePlane(origin21, matrix5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform5 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane5, direction249, point251, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem5 = workPart.CoordinateSystems.CreateCoordinateSystem(xform5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point252 = NXOpen.Point3d(12.343242532238841, 62.292490337762466, 57.0)
    orientation5 = NXOpen.Matrix3x3()
    
    orientation5.Xx = 1.0
    orientation5.Xy = 0.0
    orientation5.Xz = 0.0
    orientation5.Yx = -0.0
    orientation5.Yy = 0.0
    orientation5.Yz = 1.0
    orientation5.Zx = 0.0
    orientation5.Zy = -1.0
    orientation5.Zz = 0.0
    addComponentBuilder6.SetInitialLocationAndOrientation(point252, orientation5)
    
    movableObjects12 = [NXOpen.NXObject.Null] * 1 
    component11 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT y_link 1")
    movableObjects12[0] = component11
    componentNetwork23.SetMovingGroup(movableObjects12)
    
    componentPositioner23.ClearNetwork()
    
    addComponentBuilder6.RemoveAddedComponents()
    
    addComponentBuilder6.Destroy()
    
    componentPositioner23.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner23.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId113, None)
    
    theSession.UndoToMark(markId112, None)
    
    theSession.DeleteUndoMark(markId112, None)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Components->Create New Component...
    # ----------------------------------------------
    markId114 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create New Component")
    
    markId115 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    fileNew2 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId115, "New Component File Dialog")
    
    theSession.UndoToMark(markId115, None)
    
    theSession.DeleteUndoMark(markId115, None)
    
    exists1 = theSession.DoesUndoMarkExist(markId114, "Create New Component")
    
    theSession.UndoToMark(markId114, "Create New Component")
    
    theSession.DeleteUndoMark(markId114, "Create New Component")
    
    # ----------------------------------------------
    #   Menu: Assemblies->Components->Add Component...
    # ----------------------------------------------
    markId116 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder7 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner24 = workPart.ComponentAssembly.Positioner
    
    componentPositioner24.ClearNetwork()
    
    componentPositioner24.PrimaryArrangement = arrangement1
    
    componentPositioner24.BeginAssemblyConstraints()
    
    allowInterpartPositioning23 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression217 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression218 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression219 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression220 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression221 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression222 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression223 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression224 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network24 = componentPositioner24.EstablishNetwork()
    
    componentNetwork24 = network24
    componentNetwork24.MoveObjectsState = True
    
    componentNetwork24.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId116, "Add Component Dialog")
    
    componentNetwork24.MoveObjectsState = True
    
    markId117 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder7.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder7.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder7.SetCount(1)
    
    addComponentBuilder7.SetScatterOption(True)
    
    addComponentBuilder7.ReferenceSet = "Unknown"
    
    addComponentBuilder7.Layer = -1
    
    addComponentBuilder7.ReferenceSet = "Use Model"
    
    addComponentBuilder7.Layer = -1
    
    partstouse9 = [NXOpen.BasePart.Null] * 1 
    partstouse9[0] = part4
    addComponentBuilder7.SetPartsToAdd(partstouse9)
    
    productinterfaceobjects9 = addComponentBuilder7.GetAllProductInterfaceObjects()
    
    coordinates8 = NXOpen.Point3d(259.81838068125182, 494.98013646980968, 0.0)
    point253 = workPart.Points.CreatePoint(coordinates8)
    
    coordinates9 = NXOpen.Point3d(259.81838068125182, 494.98013646980968, 0.0)
    point254 = workPart.Points.CreatePoint(coordinates9)
    
    origin22 = NXOpen.Point3d(259.81838068125182, 494.98013646980968, 0.0)
    vector11 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction250 = workPart.Directions.CreateDirection(origin22, vector11, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin23 = NXOpen.Point3d(259.81838068125182, 494.98013646980968, 0.0)
    vector12 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction251 = workPart.Directions.CreateDirection(origin23, vector12, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin24 = NXOpen.Point3d(259.81838068125182, 494.98013646980968, 0.0)
    matrix6 = NXOpen.Matrix3x3()
    
    matrix6.Xx = 1.0
    matrix6.Xy = 0.0
    matrix6.Xz = 0.0
    matrix6.Yx = 0.0
    matrix6.Yy = 1.0
    matrix6.Yz = 0.0
    matrix6.Zx = 0.0
    matrix6.Zy = 0.0
    matrix6.Zz = 1.0
    plane6 = workPart.Planes.CreateFixedTypePlane(origin24, matrix6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform6 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane6, direction251, point254, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem6 = workPart.CoordinateSystems.CreateCoordinateSystem(xform6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point255 = NXOpen.Point3d(259.81838068125182, 494.98013646980968, 0.0)
    orientation6 = NXOpen.Matrix3x3()
    
    orientation6.Xx = 1.0
    orientation6.Xy = 0.0
    orientation6.Xz = 0.0
    orientation6.Yx = 0.0
    orientation6.Yy = 1.0
    orientation6.Yz = 0.0
    orientation6.Zx = 0.0
    orientation6.Zy = 0.0
    orientation6.Zz = 1.0
    addComponentBuilder7.SetInitialLocationAndOrientation(point255, orientation6)
    
    movableObjects13 = [NXOpen.NXObject.Null] * 1 
    component12 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT y_link 1")
    movableObjects13[0] = component12
    componentNetwork24.SetMovingGroup(movableObjects13)
    
    markId118 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    theSession.DeleteUndoMark(markId118, None)
    
    markId119 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId120 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork24.Solve()
    
    componentPositioner24.ClearNetwork()
    
    nErrs57 = theSession.UpdateManager.AddToDeleteList(componentNetwork24)
    
    nErrs58 = theSession.UpdateManager.DoUpdate(markId117)
    
    componentPositioner24.EndAssemblyConstraints()
    
    logicalobjects6 = addComponentBuilder7.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder7.ComponentName = "Y_LINK"
    
    nXObject7 = addComponentBuilder7.Commit()
    
    errorList6 = addComponentBuilder7.GetOperationFailures()
    
    errorList6.Dispose()
    theSession.DeleteUndoMark(markId119, None)
    
    theSession.SetUndoMarkName(markId116, "Add Component")
    
    addComponentBuilder7.Destroy()
    
    workPart.Points.DeletePoint(point253)
    
    componentPositioner24.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId117, None)
    
    scaleAboutPoint82 = NXOpen.Point3d(-55.03373671190262, 24.536702108014381, 0.0)
    viewCenter82 = NXOpen.Point3d(55.033736711902513, -24.536702108014271, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint82, viewCenter82)
    
    scaleAboutPoint83 = NXOpen.Point3d(-68.79217088987825, 30.670877635017955, 0.0)
    viewCenter83 = NXOpen.Point3d(68.792170889878165, -30.670877635017838, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint83, viewCenter83)
    
    scaleAboutPoint84 = NXOpen.Point3d(-85.990213612347802, 38.338597043772424, 0.0)
    viewCenter84 = NXOpen.Point3d(85.990213612347702, -38.33859704377231, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint84, viewCenter84)
    
    rotMatrix23 = NXOpen.Matrix3x3()
    
    rotMatrix23.Xx = 0.52661427969974495
    rotMatrix23.Xy = -0.84719369933353983
    rotMatrix23.Xz = 0.070286814025572283
    rotMatrix23.Yx = 0.12627975157402155
    rotMatrix23.Yy = 0.159721622493913
    rotMatrix23.Yz = 0.97905180028960404
    rotMatrix23.Zx = -0.84067284050260405
    rotMatrix23.Zy = -0.50670685718417063
    rotMatrix23.Zz = 0.19109509706902267
    translation285 = NXOpen.Point3d(48.760940562574788, -31.706181174982795, 61.409990260785506)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix23, translation285, 1.3636823122915809)
    
    scaleAboutPoint85 = NXOpen.Point3d(-73.146007517723618, 43.460757782414078, 0.0)
    viewCenter85 = NXOpen.Point3d(73.146007517723547, -43.460757782413964, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint85, viewCenter85)
    
    scaleAboutPoint86 = NXOpen.Point3d(-109.37947410641034, 58.93395168039406, 0.0)
    viewCenter86 = NXOpen.Point3d(109.37947410641027, -58.933951680393932, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint86, viewCenter86)
    
    scaleAboutPoint87 = NXOpen.Point3d(-87.697600525228395, 47.147161344315272, 0.0)
    viewCenter87 = NXOpen.Point3d(87.697600525228253, -47.147161344315158, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint87, viewCenter87)
    
    scaleAboutPoint88 = NXOpen.Point3d(-70.313297412262742, 37.717729075452233, 0.0)
    viewCenter88 = NXOpen.Point3d(70.313297412262628, -37.717729075452105, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint88, viewCenter88)
    
    scaleAboutPoint89 = NXOpen.Point3d(-56.498985117138297, 30.174183260361797, 0.0)
    viewCenter89 = NXOpen.Point3d(56.498985117138169, -30.17418326036168, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint89, viewCenter89)
    
    scaleAboutPoint90 = NXOpen.Point3d(-45.199188093710625, 24.139346608289433, 0.0)
    viewCenter90 = NXOpen.Point3d(45.199188093710525, -24.139346608289323, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint90, viewCenter90)
    
    scaleAboutPoint91 = NXOpen.Point3d(-36.477234874748454, 18.993592886851612, 0.0)
    viewCenter91 = NXOpen.Point3d(36.477234874748341, -18.993592886851509, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint91, viewCenter91)
    
    scaleAboutPoint92 = NXOpen.Point3d(-45.894560218229245, 23.543313358702047, 0.0)
    viewCenter92 = NXOpen.Point3d(45.894560218229145, -23.54331335870193, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint92, viewCenter92)
    
    scaleAboutPoint93 = NXOpen.Point3d(-57.492373866450592, 29.30496810471351, 0.0)
    viewCenter93 = NXOpen.Point3d(57.492373866450464, -29.304968104713392, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint93, viewCenter93)
    
    scaleAboutPoint94 = NXOpen.Point3d(-71.865467333063222, 36.47599313881183, 0.0)
    viewCenter94 = NXOpen.Point3d(71.865467333063108, -36.47599313881171, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint94, viewCenter94)
    
    scaleAboutPoint95 = NXOpen.Point3d(-90.025855406429116, 45.594991423514756, 0.0)
    viewCenter95 = NXOpen.Point3d(90.025855406428974, -45.594991423514642, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint95, viewCenter95)
    
    scaleAboutPoint96 = NXOpen.Point3d(-113.01737235828652, 56.751212729268332, 0.0)
    viewCenter96 = NXOpen.Point3d(113.01737235828635, -56.751212729268232, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint96, viewCenter96)
    
    scaleAboutPoint97 = NXOpen.Point3d(-141.87803182317086, 70.635857723929064, 0.0)
    viewCenter97 = NXOpen.Point3d(141.8780318231706, -70.63585772392895, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint97, viewCenter97)
    
    scaleAboutPoint98 = NXOpen.Point3d(-177.34753977896361, 88.294822154911344, 0.0)
    viewCenter98 = NXOpen.Point3d(177.34753977896321, -88.294822154911202, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint98, viewCenter98)
    
    scaleAboutPoint99 = NXOpen.Point3d(-223.10547872834346, 112.26326636649125, 0.0)
    viewCenter99 = NXOpen.Point3d(223.10547872834329, -112.26326636649117, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint99, viewCenter99)
    
    scaleAboutPoint100 = NXOpen.Point3d(-278.88184841042931, 140.32908295811413, 0.0)
    viewCenter100 = NXOpen.Point3d(278.88184841042914, -140.32908295811401, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint100, viewCenter100)
    
    scaleAboutPoint101 = NXOpen.Point3d(-348.60231051303663, 175.41135369764262, 0.0)
    viewCenter101 = NXOpen.Point3d(348.60231051303634, -175.41135369764248, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint101, viewCenter101)
    
    scaleAboutPoint102 = NXOpen.Point3d(-435.75288814129556, 219.26419212205326, 0.0)
    viewCenter102 = NXOpen.Point3d(435.75288814129544, -219.26419212205312, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint102, viewCenter102)
    
    scaleAboutPoint103 = NXOpen.Point3d(-647.61575732252004, 296.05291763315205, 0.0)
    viewCenter103 = NXOpen.Point3d(647.61575732251981, -296.05291763315194, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint103, viewCenter103)
    
    scaleAboutPoint104 = NXOpen.Point3d(-518.09260585801599, 236.84233410652169, 0.0)
    viewCenter104 = NXOpen.Point3d(518.09260585801587, -236.84233410652152, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint104, viewCenter104)
    
    scaleAboutPoint105 = NXOpen.Point3d(-415.21421698049573, 189.47386728521732, 0.0)
    viewCenter105 = NXOpen.Point3d(415.21421698049545, -189.47386728521721, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint105, viewCenter105)
    
    scaleAboutPoint106 = NXOpen.Point3d(-333.94769109019541, 152.7633054987065, 0.0)
    viewCenter106 = NXOpen.Point3d(333.94769109019529, -152.76330549870636, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint106, viewCenter106)
    
    scaleAboutPoint107 = NXOpen.Point3d(-282.31606225497382, 123.63169840360437, 0.0)
    viewCenter107 = NXOpen.Point3d(282.31606225497364, -123.63169840360425, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint107, viewCenter107)
    
    scaleAboutPoint108 = NXOpen.Point3d(-225.85284980397915, 98.905358722883491, 0.0)
    viewCenter108 = NXOpen.Point3d(225.85284980397898, -98.90535872288342, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint108, viewCenter108)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Move Component...
    # ----------------------------------------------
    markId121 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner25 = workPart.ComponentAssembly.Positioner
    
    componentPositioner25.ClearNetwork()
    
    componentPositioner25.PrimaryArrangement = arrangement1
    
    componentPositioner25.BeginMoveComponent()
    
    allowInterpartPositioning24 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression225 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression226 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression227 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression228 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression229 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression230 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression231 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression232 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network25 = componentPositioner25.EstablishNetwork()
    
    componentNetwork25 = network25
    componentNetwork25.MoveObjectsState = True
    
    componentNetwork25.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork25.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    expression233 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression234 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression235 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression236 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression237 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    componentNetwork25.RemoveAllConstraints()
    
    movableObjects14 = []
    componentNetwork25.SetMovingGroup(movableObjects14)
    
    componentNetwork25.Solve()
    
    theSession.SetUndoMarkName(markId121, "Move Component Dialog")
    
    componentNetwork25.MoveObjectsState = True
    
    componentNetwork25.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId122 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component Update")
    
    componentPositioner25.EndMoveComponent()
    
    componentPositioner25.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMarksUpToMark(markId122, None, False)
    
    theSession.UndoToMark(markId121, None)
    
    theSession.DeleteUndoMark(markId121, None)
    
    rotMatrix24 = NXOpen.Matrix3x3()
    
    rotMatrix24.Xx = 0.41693872413913369
    rotMatrix24.Xy = -0.88786995584998096
    rotMatrix24.Xz = 0.19454830200282236
    rotMatrix24.Yx = -0.096696678483717075
    rotMatrix24.Yy = 0.16949734547862375
    rotMatrix24.Yz = 0.98077540866699653
    rotMatrix24.Zx = -0.9037764395487643
    rotMatrix24.Zy = -0.4277354221649754
    rotMatrix24.Zz = -0.015184068687351109
    translation286 = NXOpen.Point3d(103.57954050891843, 1.3909928769316053, 58.378569860764429)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix24, translation286, 0.87275667986661254)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId123 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId124 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner26 = workPart.ComponentAssembly.Positioner
    
    componentPositioner26.ClearNetwork()
    
    componentPositioner26.PrimaryArrangement = arrangement1
    
    componentPositioner26.BeginAssemblyConstraints()
    
    allowInterpartPositioning25 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression238 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression239 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression240 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression241 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression242 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression243 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression244 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression245 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network26 = componentPositioner26.EstablishNetwork()
    
    componentNetwork26 = network26
    componentNetwork26.MoveObjectsState = True
    
    componentNetwork26.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork26.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId124, "Assembly Constraints Dialog")
    
    componentNetwork26.MoveObjectsState = True
    
    componentNetwork26.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId125 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    component13 = nXObject7
    face10 = component13.FindObject("PROTO#.Features|EXTRUDE(12)|FACE 140 {(3,-1,48.5) EXTRUDE(2)}")
    line13 = workPart.Lines.CreateFaceAxis(face10, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    face11 = component13.FindObject("PROTO#.Features|EXTRUDE(12)|FACE 140 1 {(3,3.8,48.5) EXTRUDE(2)}")
    line14 = workPart.Lines.CreateFaceAxis(face11, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scaleAboutPoint109 = NXOpen.Point3d(-219.78968605085214, 111.56221305753594, 0.0)
    viewCenter109 = NXOpen.Point3d(219.78968605085203, -111.56221305753591, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint109, viewCenter109)
    
    scaleAboutPoint110 = NXOpen.Point3d(-175.83174884068174, 89.249770446028776, 0.0)
    viewCenter110 = NXOpen.Point3d(175.83174884068163, -89.249770446028748, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint110, viewCenter110)
    
    scaleAboutPoint111 = NXOpen.Point3d(-140.66539907254537, 71.399816356823024, 0.0)
    viewCenter111 = NXOpen.Point3d(140.66539907254528, -71.399816356822981, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint111, viewCenter111)
    
    objects13 = [NXOpen.TaggedObject.Null] * 1 
    objects13[0] = line14
    nErrs59 = theSession.UpdateManager.AddObjectsToDeleteList(objects13)
    
    objects14 = [NXOpen.TaggedObject.Null] * 1 
    objects14[0] = line13
    nErrs60 = theSession.UpdateManager.AddObjectsToDeleteList(objects14)
    
    scaleAboutPoint112 = NXOpen.Point3d(-50.135088441856226, 45.323361687374607, 0.0)
    viewCenter112 = NXOpen.Point3d(50.135088441856098, -45.323361687374579, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint112, viewCenter112)
    
    scaleAboutPoint113 = NXOpen.Point3d(-62.862881792420289, 56.266159629018105, 0.0)
    viewCenter113 = NXOpen.Point3d(62.862881792420225, -56.266159629018105, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint113, viewCenter113)
    
    scaleAboutPoint114 = NXOpen.Point3d(-78.578602240525328, 70.332699536272628, 0.0)
    viewCenter114 = NXOpen.Point3d(78.578602240525214, -70.332699536272628, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint114, viewCenter114)
    
    scaleAboutPoint115 = NXOpen.Point3d(125.81064787738416, 25.162129575476836, 0.0)
    viewCenter115 = NXOpen.Point3d(-125.81064787738426, -25.162129575476836, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint115, viewCenter115)
    
    scaleAboutPoint116 = NXOpen.Point3d(87.552084595153119, 16.00675230825513, 0.0)
    viewCenter116 = NXOpen.Point3d(-87.552084595153218, -16.006752308255169, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint116, viewCenter116)
    
    scaleAboutPoint117 = NXOpen.Point3d(70.817752636522698, 12.417359366403975, 0.0)
    viewCenter117 = NXOpen.Point3d(-70.817752636522826, -12.417359366404009, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint117, viewCenter117)
    
    scaleAboutPoint118 = NXOpen.Point3d(57.740721053778529, 9.3130195248029839, 0.0)
    viewCenter118 = NXOpen.Point3d(-57.74072105377865, -9.3130195248030105, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint118, viewCenter118)
    
    rotMatrix25 = NXOpen.Matrix3x3()
    
    rotMatrix25.Xx = -0.30181168556777471
    rotMatrix25.Xy = -0.93619117681454067
    rotMatrix25.Xz = 0.18015489698961407
    rotMatrix25.Yx = 0.026081722374709574
    rotMatrix25.Yy = 0.18078811162741723
    rotMatrix25.Yz = 0.98317618077949687
    rotMatrix25.Zx = -0.95301072932716635
    rotMatrix25.Zy = 0.3014328103388772
    rotMatrix25.Zz = -0.030146486337557361
    translation287 = NXOpen.Point3d(202.48737730761999, -41.829455725856604, -113.2606890084908)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix25, translation287, 2.1307536129555968)
    
    origin25 = NXOpen.Point3d(-77.85243559033006, 131.64321122767541, 20.403722306202585)
    workPart.ModelingViews.WorkView.SetOrigin(origin25)
    
    origin26 = NXOpen.Point3d(-77.85243559033006, 131.64321122767541, 20.403722306202585)
    workPart.ModelingViews.WorkView.SetOrigin(origin26)
    
    line15 = workPart.Lines.CreateFaceAxis(face7, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scaleAboutPoint119 = NXOpen.Point3d(41.970674658445404, -9.1888459311389834, 0.0)
    viewCenter119 = NXOpen.Point3d(-41.970674658445553, 9.1888459311389514, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint119, viewCenter119)
    
    scaleAboutPoint120 = NXOpen.Point3d(33.576539726756323, -7.4504156198424232, 0.0)
    viewCenter120 = NXOpen.Point3d(-33.576539726756458, 7.4504156198423805, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint120, viewCenter120)
    
    scaleAboutPoint121 = NXOpen.Point3d(26.861231781405039, -5.9603324958739261, 0.0)
    viewCenter121 = NXOpen.Point3d(-26.861231781405202, 5.9603324958739057, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint121, viewCenter121)
    
    scaleAboutPoint122 = NXOpen.Point3d(21.488985425124024, -4.768265996699153, 0.0)
    viewCenter122 = NXOpen.Point3d(-21.488985425124177, 4.7682659966991201, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint122, viewCenter122)
    
    scaleAboutPoint123 = NXOpen.Point3d(17.34377285199357, -3.9671973092536907, 0.0)
    viewCenter123 = NXOpen.Point3d(-17.343772851993752, 3.9671973092536645, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint123, viewCenter123)
    
    markId126 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint10 = componentPositioner26.CreateConstraint(True)
    
    componentConstraint10 = constraint10
    componentConstraint10.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge14 = component13.FindObject("PROTO#.Features|EXTRUDE(10)|EDGE * 170 EXTRUDE(12) 140 {(4.2990381056767,3.3,46.25)(3,3.3,48.5)(1.7009618943233,3.3,46.25) EXTRUDE(2)}")
    constraintReference18 = componentConstraint10.CreateConstraintReference(component13, edge14, False, False, False)
    
    helpPoint17 = NXOpen.Point3d(264.30798358307806, 498.28013646980975, 46.823695732124982)
    constraintReference18.HelpPoint = helpPoint17
    
    edge15 = component10.FindObject("PROTO#.Features|EXTRUDE(4)|EDGE * 160 EXTRUDE(2) 120 {(2.25,1.7009618943233,0)(4.5,3,0)(2.25,4.2990381056767,0) EXTRUDE(2)}")
    constraintReference19 = componentConstraint10.CreateConstraintReference(component10, edge15, False, False, False)
    
    helpPoint18 = NXOpen.Point3d(2.470783851913577, 60.792490337762324, 22.182822887457196)
    constraintReference19.HelpPoint = helpPoint18
    
    constraintReference19.SetFixHint(True)
    
    objects15 = [NXOpen.TaggedObject.Null] * 1 
    objects15[0] = line15
    nErrs61 = theSession.UpdateManager.AddObjectsToDeleteList(objects15)
    
    componentNetwork26.Solve()
    
    scaleAboutPoint124 = NXOpen.Point3d(15.25845118943715, -1.8310141427324826, 0.0)
    viewCenter124 = NXOpen.Point3d(-15.258451189437329, 1.8310141427324549, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint124, viewCenter124)
    
    scaleAboutPoint125 = NXOpen.Point3d(19.07306398679647, -2.2887676784155953, 0.0)
    viewCenter125 = NXOpen.Point3d(-19.073063986796644, 2.2887676784155695, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint125, viewCenter125)
    
    scaleAboutPoint126 = NXOpen.Point3d(23.841329983495609, -2.8609595980194999, 0.0)
    viewCenter126 = NXOpen.Point3d(-23.841329983495783, 2.8609595980194671, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint126, viewCenter126)
    
    scaleAboutPoint127 = NXOpen.Point3d(29.80166247936954, -3.5761994975243749, 0.0)
    viewCenter127 = NXOpen.Point3d(-29.801662479369714, 3.5761994975243407, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint127, viewCenter127)
    
    scaleAboutPoint128 = NXOpen.Point3d(37.252078099211943, -4.4702493719054601, 0.0)
    viewCenter128 = NXOpen.Point3d(-37.252078099212113, 4.4702493719054184, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint128, viewCenter128)
    
    scaleAboutPoint129 = NXOpen.Point3d(46.937618405007058, -4.7185965592335499, 0.0)
    viewCenter129 = NXOpen.Point3d(-46.937618405007228, 4.7185965592335082, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint129, viewCenter129)
    
    scaleAboutPoint130 = NXOpen.Point3d(58.672023006258847, -5.898245699041925, 0.0)
    viewCenter130 = NXOpen.Point3d(-58.67202300625901, 5.898245699041885, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint130, viewCenter130)
    
    scaleAboutPoint131 = NXOpen.Point3d(73.340028757823546, -7.3728071238024055, 0.0)
    viewCenter131 = NXOpen.Point3d(-73.340028757823745, 7.3728071238023718, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint131, viewCenter131)
    
    markId127 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    theSession.DeleteUndoMark(markId127, None)
    
    markId128 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs62 = theSession.UpdateManager.DoUpdate(markId125)
    
    componentNetwork26.Solve()
    
    componentPositioner26.ClearNetwork()
    
    nErrs63 = theSession.UpdateManager.AddToDeleteList(componentNetwork26)
    
    componentPositioner26.DeleteNonPersistentConstraints()
    
    nErrs64 = theSession.UpdateManager.DoUpdate(markId125)
    
    theSession.DeleteUndoMark(markId128, None)
    
    theSession.SetUndoMarkName(markId124, "Assembly Constraints")
    
    componentPositioner26.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner26.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId125, None)
    
    theSession.DeleteUndoMark(markId126, None)
    
    theSession.DeleteUndoMark(markId123, None)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId129 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId130 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner27 = workPart.ComponentAssembly.Positioner
    
    componentPositioner27.ClearNetwork()
    
    componentPositioner27.PrimaryArrangement = arrangement1
    
    componentPositioner27.BeginAssemblyConstraints()
    
    allowInterpartPositioning26 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression246 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression247 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression248 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression249 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression250 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression251 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression252 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression253 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network27 = componentPositioner27.EstablishNetwork()
    
    componentNetwork27 = network27
    componentNetwork27.MoveObjectsState = True
    
    componentNetwork27.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork27.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId130, "Assembly Constraints Dialog")
    
    componentNetwork27.MoveObjectsState = True
    
    componentNetwork27.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId131 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    face12 = component13.FindObject("PROTO#.Features|SIMPLE HOLE(4:1A)|FACE 3 {(3,1.4,1.5) EXTRUDE(2)}")
    line16 = workPart.Lines.CreateFaceAxis(face12, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line16.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint132 = NXOpen.Point3d(82.459027042526486, -56.023633078893099, 0.0)
    viewCenter132 = NXOpen.Point3d(-82.459027042526643, 56.023633078893077, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint132, viewCenter132)
    
    scaleAboutPoint133 = NXOpen.Point3d(66.54928535432137, -46.371076383914975, 0.0)
    viewCenter133 = NXOpen.Point3d(-66.54928535432154, 46.371076383914939, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint133, viewCenter133)
    
    scaleAboutPoint134 = NXOpen.Point3d(53.239428283457073, -37.252078099212035, 0.0)
    viewCenter134 = NXOpen.Point3d(-53.239428283457244, 37.252078099212, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint134, viewCenter134)
    
    scaleAboutPoint135 = NXOpen.Point3d(42.591542626765666, -30.050009666697722, 0.0)
    viewCenter135 = NXOpen.Point3d(-42.591542626765815, 30.050009666697679, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint135, viewCenter135)
    
    objects16 = [NXOpen.TaggedObject.Null] * 1 
    objects16[0] = line16
    nErrs65 = theSession.UpdateManager.AddObjectsToDeleteList(objects16)
    
    scaleAboutPoint136 = NXOpen.Point3d(40.530260971942582, 25.530090857326613, 0.0)
    viewCenter136 = NXOpen.Point3d(-40.530260971942752, -25.530090857326648, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint136, viewCenter136)
    
    scaleAboutPoint137 = NXOpen.Point3d(50.662826214928259, 31.664266384330205, 0.0)
    viewCenter137 = NXOpen.Point3d(-50.66282621492843, -31.664266384330233, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint137, viewCenter137)
    
    scaleAboutPoint138 = NXOpen.Point3d(63.328532768660352, 39.269898996252671, 0.0)
    viewCenter138 = NXOpen.Point3d(-63.328532768660509, -39.269898996252685, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint138, viewCenter138)
    
    scaleAboutPoint139 = NXOpen.Point3d(78.772623480625327, 48.505310025015632, 0.0)
    viewCenter139 = NXOpen.Point3d(-78.772623480625455, -48.505310025015667, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint139, viewCenter139)
    
    scaleAboutPoint140 = NXOpen.Point3d(98.223252800656581, 65.482168533771087, 0.0)
    viewCenter140 = NXOpen.Point3d(-98.223252800656709, -65.482168533771102, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint140, viewCenter140)
    
    scaleAboutPoint141 = NXOpen.Point3d(122.77906600082069, 81.85271066721387, 0.0)
    viewCenter141 = NXOpen.Point3d(-122.77906600082079, -81.852710667213884, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint141, viewCenter141)
    
    scaleAboutPoint142 = NXOpen.Point3d(153.47383250102595, 102.31588833401732, 0.0)
    viewCenter142 = NXOpen.Point3d(-153.4738325010261, -102.31588833401734, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint142, viewCenter142)
    
    origin27 = NXOpen.Point3d(-76.155131546524771, 137.77269723371811, 28.035763582295804)
    workPart.ModelingViews.WorkView.SetOrigin(origin27)
    
    origin28 = NXOpen.Point3d(-76.155131546524771, 137.77269723371811, 28.035763582295804)
    workPart.ModelingViews.WorkView.SetOrigin(origin28)
    
    scaleAboutPoint143 = NXOpen.Point3d(39.315827461682453, 12.315801373539111, 0.0)
    viewCenter143 = NXOpen.Point3d(-39.315827461682659, -12.315801373539111, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint143, viewCenter143)
    
    scaleAboutPoint144 = NXOpen.Point3d(33.347400642198096, 10.231588833401736, 0.0)
    viewCenter144 = NXOpen.Point3d(-33.347400642198352, -10.231588833401768, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint144, viewCenter144)
    
    scaleAboutPoint145 = NXOpen.Point3d(29.406344202665551, 8.488429254377742, 0.0)
    viewCenter145 = NXOpen.Point3d(-29.406344202665807, -8.4884292543777686, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint145, viewCenter145)
    
    scaleAboutPoint146 = NXOpen.Point3d(25.465287763133077, 7.5183230538774177, 0.0)
    viewCenter146 = NXOpen.Point3d(-25.465287763133325, -7.5183230538774382, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint146, viewCenter146)
    
    scaleAboutPoint147 = NXOpen.Point3d(21.730378891206918, 6.596722163402104, 0.0)
    viewCenter147 = NXOpen.Point3d(-21.730378891207067, -6.5967221634021378, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint147, viewCenter147)
    
    scaleAboutPoint148 = NXOpen.Point3d(22.50646385160713, 18.160388073365819, 0.0)
    viewCenter148 = NXOpen.Point3d(-22.506463851607315, -18.160388073365873, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint148, viewCenter148)
    
    scaleAboutPoint149 = NXOpen.Point3d(18.005171081285688, 14.528310458692648, 0.0)
    viewCenter149 = NXOpen.Point3d(-18.005171081285898, -14.528310458692722, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint149, viewCenter149)
    
    scaleAboutPoint150 = NXOpen.Point3d(14.404136865028534, 11.622648366954103, 0.0)
    viewCenter150 = NXOpen.Point3d(-14.404136865028736, -11.622648366954186, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint150, viewCenter150)
    
    scaleAboutPoint151 = NXOpen.Point3d(11.523309492022815, 9.3775897935082533, 0.0)
    viewCenter151 = NXOpen.Point3d(-11.523309492023019, -9.3775897935083492, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint151, viewCenter151)
    
    scaleAboutPoint152 = NXOpen.Point3d(9.2186475936182326, 7.5020718348065989, 0.0)
    viewCenter152 = NXOpen.Point3d(-9.2186475936184387, -7.5020718348066806, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint152, viewCenter152)
    
    rotMatrix26 = NXOpen.Matrix3x3()
    
    rotMatrix26.Xx = 0.55733620930031469
    rotMatrix26.Xy = -0.81692937226532236
    rotMatrix26.Xz = 0.14833324149676116
    rotMatrix26.Yx = 0.0032543029495952953
    rotMatrix26.Yy = 0.18080095243408212
    rotMatrix26.Yz = 0.98351432379566173
    rotMatrix26.Zx = -0.83028053049259098
    rotMatrix26.Zy = -0.54766542371151128
    rotMatrix26.Zz = 0.10342545313327187
    translation288 = NXOpen.Point3d(7.5086977532458103, -70.610795412386523, -80.897715311561328)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix26, translation288, 5.2020351878798792)
    
    face13 = component6.FindObject("PROTO#.Features|SIMPLE HOLE(10:1A)|FACE 3 {(7,4,-7.5) EXTRUDE(6)1}")
    line17 = workPart.Lines.CreateFaceAxis(face13, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line17.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId132 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint11 = componentPositioner27.CreateConstraint(True)
    
    componentConstraint11 = constraint11
    componentConstraint11.ConstraintType = NXOpen.Positioning.Constraint.Type.Distance
    
    constraintReference20 = componentConstraint11.CreateConstraintReference(component13, face12, False, False, False)
    
    helpPoint19 = NXOpen.Point3d(4.7058846587124332, 59.69823407112353, -22.274072560807305)
    constraintReference20.HelpPoint = helpPoint19
    
    edge16 = component6.FindObject("PROTO#.Features|EXTRUDE(6)|EDGE * 310 SIMPLE HOLE(10:1A) 3 {(8.2990381056767,3,-6.75)(7,3,-4.5)(5.7009618943233,3,-6.75) EXTRUDE(6)1}")
    constraintReference21 = componentConstraint11.CreateConstraintReference(component6, edge16, False, False, False)
    
    helpPoint20 = NXOpen.Point3d(14.305396878278964, 62.292490337762466, 62.082994182143459)
    constraintReference21.HelpPoint = helpPoint20
    
    constraintReference21.SetFixHint(True)
    
    componentConstraint11.SetExpression("0")
    
    componentConstraint11.SetExpression("85.8472539561391")
    
    objects17 = [NXOpen.TaggedObject.Null] * 1 
    objects17[0] = line17
    nErrs66 = theSession.UpdateManager.AddObjectsToDeleteList(objects17)
    
    componentNetwork27.Solve()
    
    constraintReference20.SetFixHint(False)
    
    constraintReference21.SetFixHint(True)
    
    componentNetwork27.AddConstraint(componentConstraint11)
    
    expression254 = workPart.Expressions.FindObject("p17")
    expression254.RightHandSide = "1.5"
    
    componentNetwork27.Solve()
    
    markId133 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    theSession.DeleteUndoMark(markId133, None)
    
    markId134 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs67 = theSession.UpdateManager.DoUpdate(markId131)
    
    componentNetwork27.Solve()
    
    componentPositioner27.ClearNetwork()
    
    nErrs68 = theSession.UpdateManager.AddToDeleteList(componentNetwork27)
    
    componentPositioner27.DeleteNonPersistentConstraints()
    
    nErrs69 = theSession.UpdateManager.DoUpdate(markId131)
    
    theSession.DeleteUndoMark(markId134, None)
    
    theSession.SetUndoMarkName(markId130, "Assembly Constraints")
    
    componentPositioner27.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner27.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId131, None)
    
    theSession.DeleteUndoMark(markId132, None)
    
    theSession.DeleteUndoMark(markId129, None)
    
    scaleAboutPoint153 = NXOpen.Point3d(-27.617796652881498, -4.9335658845847519, 0.0)
    viewCenter153 = NXOpen.Point3d(27.617796652881299, 4.9335658845846657, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint153, viewCenter153)
    
    scaleAboutPoint154 = NXOpen.Point3d(-34.522245816101844, -6.1669573557309283, 0.0)
    viewCenter154 = NXOpen.Point3d(34.522245816101659, 6.1669573557308413, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint154, viewCenter154)
    
    scaleAboutPoint155 = NXOpen.Point3d(-42.278625170732433, -8.1060521943885657, 0.0)
    viewCenter155 = NXOpen.Point3d(42.278625170732241, 8.106052194388484, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint155, viewCenter155)
    
    scaleAboutPoint156 = NXOpen.Point3d(-32.781828727306674, -21.159180360352462, 0.0)
    viewCenter156 = NXOpen.Point3d(32.781828727306433, 21.159180360352369, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint156, viewCenter156)
    
    scaleAboutPoint157 = NXOpen.Point3d(-40.977285909133322, -26.448975450440557, 0.0)
    viewCenter157 = NXOpen.Point3d(40.977285909133087, 26.448975450440464, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint157, viewCenter157)
    
    origin29 = NXOpen.Point3d(-53.770002642266988, -47.82640623207871, 97.274506948467391)
    workPart.ModelingViews.WorkView.SetOrigin(origin29)
    
    origin30 = NXOpen.Point3d(-53.770002642266988, -47.82640623207871, 97.274506948467391)
    workPart.ModelingViews.WorkView.SetOrigin(origin30)
    
    rotMatrix27 = NXOpen.Matrix3x3()
    
    rotMatrix27.Xx = 0.56499143884332137
    rotMatrix27.Xy = -0.81877178601907974
    rotMatrix27.Xz = 0.101967820673346
    rotMatrix27.Yx = 0.014894398651015965
    rotMatrix27.Yy = 0.13368359795763674
    rotMatrix27.Yz = 0.99091213158681435
    rotMatrix27.Zx = -0.824962320910821
    rotMatrix27.Zy = -0.55833812162185392
    rotMatrix27.Zz = 0.087725201745009654
    translation289 = NXOpen.Point3d(-22.135269739171896, -85.279823921355359, -80.045019418080457)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix27, translation289, 1.7046028903644794)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId135 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId136 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner28 = workPart.ComponentAssembly.Positioner
    
    componentPositioner28.ClearNetwork()
    
    componentPositioner28.PrimaryArrangement = arrangement1
    
    componentPositioner28.BeginAssemblyConstraints()
    
    allowInterpartPositioning27 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression255 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression256 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression257 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression258 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression259 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression260 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression261 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression262 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network28 = componentPositioner28.EstablishNetwork()
    
    componentNetwork28 = network28
    componentNetwork28.MoveObjectsState = True
    
    componentNetwork28.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork28.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId136, "Assembly Constraints Dialog")
    
    componentNetwork28.MoveObjectsState = True
    
    componentNetwork28.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId137 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    scaleAboutPoint158 = NXOpen.Point3d(-58.516806014178947, -19.246907017926251, 0.0)
    viewCenter158 = NXOpen.Point3d(58.516806014178734, 19.246907017926144, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint158, viewCenter158)
    
    scaleAboutPoint159 = NXOpen.Point3d(-46.937618405007207, -14.900831239684825, 0.0)
    viewCenter159 = NXOpen.Point3d(46.93761840500698, 14.90083123968475, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint159, viewCenter159)
    
    scaleAboutPoint160 = NXOpen.Point3d(-37.649433598937044, -11.82132611681665, 0.0)
    viewCenter160 = NXOpen.Point3d(37.649433598936795, 11.821326116816564, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint160, viewCenter160)
    
    scaleAboutPoint161 = NXOpen.Point3d(-30.993728978544485, -8.1855232943335547, 0.0)
    viewCenter161 = NXOpen.Point3d(30.993728978544244, 8.1855232943334659, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint161, viewCenter161)
    
    scaleAboutPoint162 = NXOpen.Point3d(-24.794983182835615, -6.548418635466855, 0.0)
    viewCenter162 = NXOpen.Point3d(24.794983182835377, 6.5484186354667742, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint162, viewCenter162)
    
    scaleAboutPoint163 = NXOpen.Point3d(-19.835986546268508, -5.2387349083734929, 0.0)
    viewCenter163 = NXOpen.Point3d(19.835986546268284, 5.2387349083734058, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint163, viewCenter163)
    
    rotMatrix28 = NXOpen.Matrix3x3()
    
    rotMatrix28.Xx = -0.40025544470918306
    rotMatrix28.Xy = -0.90855406686062889
    rotMatrix28.Xz = 0.11968745369362142
    rotMatrix28.Yx = 0.015172805687730325
    rotMatrix28.Yy = 0.12401748192882971
    rotMatrix28.Yz = 0.99216402381037527
    rotMatrix28.Zx = -0.91627799545127853
    rotMatrix28.Zy = 0.3989350470528269
    rotMatrix28.Zz = -0.035853358067863314
    translation290 = NXOpen.Point3d(54.354457168549523, -71.647829941759099, -122.09578485532491)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix28, translation290, 6.5025439848498525)
    
    line18 = workPart.Lines.CreateFaceAxis(face12, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId138 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint12 = componentPositioner28.CreateConstraint(True)
    
    componentConstraint12 = constraint12
    componentConstraint12.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    constraintReference22 = componentConstraint12.CreateConstraintReference(component6, edge16, False, False, False)
    
    helpPoint21 = NXOpen.Point3d(13.895713289051697, 62.292490337762466, 60.606732800607524)
    constraintReference22.HelpPoint = helpPoint21
    
    edge17 = component13.FindObject("PROTO#.Features|EXTRUDE(2)|EDGE * 170 SIMPLE HOLE(4:1A) 3 {(2.25,2.8,4.2990381056767)(4.5,2.8,3)(2.25,2.8,1.7009618943233) EXTRUDE(2)}")
    constraintReference23 = componentConstraint12.CreateConstraintReference(component13, edge17, False, False, False)
    
    helpPoint22 = NXOpen.Point3d(15.328203379235964, 60.292490337762224, 61.00700360373262)
    constraintReference23.HelpPoint = helpPoint22
    
    constraintReference23.SetFixHint(True)
    
    objects18 = [NXOpen.TaggedObject.Null] * 1 
    objects18[0] = line18
    nErrs70 = theSession.UpdateManager.AddObjectsToDeleteList(objects18)
    
    componentNetwork28.Solve()
    
    markId139 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    theSession.DeleteUndoMark(markId139, None)
    
    markId140 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs71 = theSession.UpdateManager.DoUpdate(markId137)
    
    componentNetwork28.Solve()
    
    componentPositioner28.ClearNetwork()
    
    nErrs72 = theSession.UpdateManager.AddToDeleteList(componentNetwork28)
    
    componentPositioner28.DeleteNonPersistentConstraints()
    
    nErrs73 = theSession.UpdateManager.DoUpdate(markId137)
    
    theSession.DeleteUndoMark(markId140, None)
    
    theSession.SetUndoMarkName(markId136, "Assembly Constraints")
    
    componentPositioner28.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner28.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId137, None)
    
    theSession.DeleteUndoMark(markId138, None)
    
    theSession.DeleteUndoMark(markId135, None)
    
    scaleAboutPoint164 = NXOpen.Point3d(4.1502987235268156, -7.3240565709299155, 0.0)
    viewCenter164 = NXOpen.Point3d(-4.1502987235270439, 7.3240565709298284, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint164, viewCenter164)
    
    scaleAboutPoint165 = NXOpen.Point3d(5.8490729559508132, -9.3076552255567524, 0.0)
    viewCenter165 = NXOpen.Point3d(-5.8490729559510557, 9.3076552255566654, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint165, viewCenter165)
    
    rotMatrix29 = NXOpen.Matrix3x3()
    
    rotMatrix29.Xx = 0.31453103521592979
    rotMatrix29.Xy = -0.94319099928895267
    rotMatrix29.Xz = 0.10705590477081246
    rotMatrix29.Yx = -0.018003172881204035
    rotMatrix29.Yy = 0.10683225676847824
    rotMatrix29.Yz = 0.99411405516669105
    rotMatrix29.Zx = -0.94907645300692156
    rotMatrix29.Zy = -0.31460706885582806
    rotMatrix29.Zz = 0.016621629695648787
    translation291 = NXOpen.Point3d(33.762703132042311, -73.785308995336777, -84.935768197073571)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix29, translation291, 4.1616281503039065)
    
    scaleAboutPoint166 = NXOpen.Point3d(11.888876551769728, -13.351144790757617, 0.0)
    viewCenter166 = NXOpen.Point3d(-11.888876551769956, 13.35114479075753, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint166, viewCenter166)
    
    scaleAboutPoint167 = NXOpen.Point3d(14.861095689712188, -16.688930988447016, 0.0)
    viewCenter167 = NXOpen.Point3d(-14.861095689712419, 16.688930988446931, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint167, viewCenter167)
    
    scaleAboutPoint168 = NXOpen.Point3d(21.059841485421043, -21.65587473500862, 0.0)
    viewCenter168 = NXOpen.Point3d(-21.059841485421281, 21.655874735008528, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint168, viewCenter168)
    
    scaleAboutPoint169 = NXOpen.Point3d(26.448975450440397, -27.069843418760751, 0.0)
    viewCenter169 = NXOpen.Point3d(-26.448975450440621, 27.069843418760669, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint169, viewCenter169)
    
    rotMatrix30 = NXOpen.Matrix3x3()
    
    rotMatrix30.Xx = 0.10351126305589359
    rotMatrix30.Xy = -0.99449903296549391
    rotMatrix30.Xz = -0.01603408404808793
    rotMatrix30.Yx = -0.058484922327416741
    rotMatrix30.Yy = -0.022178539237727744
    rotMatrix30.Yz = 0.99804189604326488
    rotMatrix30.Zx = -0.99290731303627799
    rotMatrix30.Zy = -0.1023708250819932
    rotMatrix30.Zz = -0.060458927306909577
    translation292 = NXOpen.Point3d(73.406328353073093, -83.919938026087692, -90.869188539618378)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix30, translation292, 1.7046028903644803)
    
    scaleAboutPoint170 = NXOpen.Point3d(19.557341002086183, -32.906002320970615, 0.0)
    viewCenter170 = NXOpen.Point3d(-19.557341002086396, 32.906002320970551, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint170, viewCenter170)
    
    scaleAboutPoint171 = NXOpen.Point3d(15.645872801668945, -26.200628263112471, 0.0)
    viewCenter171 = NXOpen.Point3d(-15.645872801669137, 26.200628263112385, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint171, viewCenter171)
    
    scaleAboutPoint172 = NXOpen.Point3d(12.516698241335124, -20.960502610489986, 0.0)
    viewCenter172 = NXOpen.Point3d(-12.516698241335344, 20.960502610489893, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint172, viewCenter172)
    
    scaleAboutPoint173 = NXOpen.Point3d(10.013358593068071, -16.768402088392008, 0.0)
    viewCenter173 = NXOpen.Point3d(-10.013358593068288, 16.768402088391912, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint173, viewCenter173)
    
    scaleAboutPoint174 = NXOpen.Point3d(8.0106868744544357, -13.414721670713613, 0.0)
    viewCenter174 = NXOpen.Point3d(-8.0106868744546578, 13.41472167071352, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint174, viewCenter174)
    
    scaleAboutPoint175 = NXOpen.Point3d(6.4085494995635228, -10.731777336570904, 0.0)
    viewCenter175 = NXOpen.Point3d(-6.4085494995637484, 10.731777336570804, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint175, viewCenter175)
    
    scaleAboutPoint176 = NXOpen.Point3d(5.1268395996508049, -8.5854218692567379, 0.0)
    viewCenter176 = NXOpen.Point3d(-5.1268395996510199, 8.5854218692566295, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint176, viewCenter176)
    
    scaleAboutPoint177 = NXOpen.Point3d(4.1014716797206194, -6.8683374954054006, 0.0)
    viewCenter177 = NXOpen.Point3d(-4.1014716797208308, 6.8683374954052869, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint177, viewCenter177)
    
    rotMatrix31 = NXOpen.Matrix3x3()
    
    rotMatrix31.Xx = -0.078762107342554108
    rotMatrix31.Xy = -0.9964491217074104
    rotMatrix31.Xz = -0.029760347704428661
    rotMatrix31.Yx = -0.024762071891134406
    rotMatrix31.Yy = -0.027888358562580276
    rotMatrix31.Yz = 0.99930429762527451
    rotMatrix31.Zx = -0.99658585693487367
    rotMatrix31.Zy = 0.079444240226799523
    rotMatrix31.Zz = -0.022477598896863005
    translation293 = NXOpen.Point3d(69.772251783278534, -58.509544541866916, -104.45932591962659)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix31, translation293, 10.1602249763279)
    
    rotMatrix32 = NXOpen.Matrix3x3()
    
    rotMatrix32.Xx = -0.76939656259249734
    rotMatrix32.Xy = -0.63634802331335261
    rotMatrix32.Xz = -0.055588872052200311
    rotMatrix32.Yx = -0.072717626629006687
    rotMatrix32.Yy = 0.00079674218265513193
    rotMatrix32.Yz = 0.99735225070149502
    rotMatrix32.Zx = -0.63461884328176976
    rotMatrix32.Zy = 0.77140168422624056
    rotMatrix32.Zz = -0.046886728662014189
    translation294 = NXOpen.Point3d(92.859702649942875, -57.128906036783938, -169.79273761279305)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix32, translation294, 10.1602249763279)
    
    scaleAboutPoint178 = NXOpen.Point3d(2.2134926525475853, -3.4634649739864494, 0.0)
    viewCenter178 = NXOpen.Point3d(-2.2134926525477985, 3.4634649739863339, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint178, viewCenter178)
    
    scaleAboutPoint179 = NXOpen.Point3d(2.7668658156845152, -4.3293312174830367, 0.0)
    viewCenter179 = NXOpen.Point3d(-2.766865815684715, 4.3293312174829426, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint179, viewCenter179)
    
    scaleAboutPoint180 = NXOpen.Point3d(3.4585822696056714, -5.411664021853789, 0.0)
    viewCenter180 = NXOpen.Point3d(-3.4585822696058655, 5.4116640218536878, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint180, viewCenter180)
    
    scaleAboutPoint181 = NXOpen.Point3d(9.0533477057326497, -6.2559649876693104, 0.0)
    viewCenter181 = NXOpen.Point3d(-9.0533477057328415, 6.2559649876692065, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint181, viewCenter181)
    
    scaleAboutPoint182 = NXOpen.Point3d(11.507415272033798, -7.8199562345866269, 0.0)
    viewCenter182 = NXOpen.Point3d(-11.507415272033994, 7.8199562345865186, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint182, viewCenter182)
    
    scaleAboutPoint183 = NXOpen.Point3d(14.463740189987245, -9.7749452932332712, 0.0)
    viewCenter183 = NXOpen.Point3d(-14.463740189987433, 9.7749452932331771, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint183, viewCenter183)
    
    rotMatrix33 = NXOpen.Matrix3x3()
    
    rotMatrix33.Xx = -0.060692292655773805
    rotMatrix33.Xy = -0.99771805431483873
    rotMatrix33.Xz = -0.029582591272516928
    rotMatrix33.Yx = -0.029272580026190848
    rotMatrix33.Yy = -0.027845359954960357
    rotMatrix33.Yz = 0.99918354269252707
    rotMatrix33.Zx = -0.99772719802097942
    rotMatrix33.Zy = 0.061508698760334581
    rotMatrix33.Zz = -0.027515782853014696
    translation295 = NXOpen.Point3d(77.285604157026171, -67.664729764839223, -108.13353344435305)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix33, translation295, 2.663442016194502)
    
    # ----------------------------------------------
    #   Menu: Edit->Undo
    # ----------------------------------------------
    marksRecycled2, undoUnavailable2 = theSession.UndoLastNVisibleMarks(1)
    
    # ----------------------------------------------
    #   Menu: Edit->Undo
    # ----------------------------------------------
    marksRecycled3, undoUnavailable3 = theSession.UndoLastNVisibleMarks(1)
    
    scaleAboutPoint184 = NXOpen.Point3d(-16.788269863378293, -12.218681616541565, 0.0)
    viewCenter184 = NXOpen.Point3d(16.78826986337809, 12.218681616541481, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint184, viewCenter184)
    
    scaleAboutPoint185 = NXOpen.Point3d(-19.246907017926272, -17.0117823319735, 0.0)
    viewCenter185 = NXOpen.Point3d(19.246907017926091, 17.011782331973436, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint185, viewCenter185)
    
    scaleAboutPoint186 = NXOpen.Point3d(-22.972114827847484, -22.351246859527215, 0.0)
    viewCenter186 = NXOpen.Point3d(22.972114827847275, 22.351246859527137, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint186, viewCenter186)
    
    scaleAboutPoint187 = NXOpen.Point3d(-19.014081529806212, -54.713989708217625, 0.0)
    viewCenter187 = NXOpen.Point3d(19.014081529806013, 54.713989708217525, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint187, viewCenter187)
    
    rotMatrix34 = NXOpen.Matrix3x3()
    
    rotMatrix34.Xx = 0.65338899972687503
    rotMatrix34.Xy = -0.65546331576591321
    rotMatrix34.Xz = 0.37874880425033819
    rotMatrix34.Yx = -0.28337800216685
    rotMatrix34.Yy = 0.25216617294661908
    rotMatrix34.Yz = 0.925261654403432
    rotMatrix34.Zx = -0.70198270842224408
    rotMatrix34.Zy = -0.71188486632783765
    rotMatrix34.Zz = -0.020981281408856085
    translation296 = NXOpen.Point3d(-17.335007168845959, -91.492964721934555, -84.617518169168648)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix34, translation296, 1.0909458498332663)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId141 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId142 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner29 = workPart.ComponentAssembly.Positioner
    
    componentPositioner29.ClearNetwork()
    
    componentPositioner29.PrimaryArrangement = arrangement1
    
    componentPositioner29.BeginAssemblyConstraints()
    
    allowInterpartPositioning28 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression263 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression264 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression265 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression266 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression267 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression268 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression269 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression270 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network29 = componentPositioner29.EstablishNetwork()
    
    componentNetwork29 = network29
    componentNetwork29.MoveObjectsState = True
    
    componentNetwork29.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork29.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId142, "Assembly Constraints Dialog")
    
    componentNetwork29.MoveObjectsState = True
    
    componentNetwork29.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId143 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    rotMatrix35 = NXOpen.Matrix3x3()
    
    rotMatrix35.Xx = -0.71214331503646977
    rotMatrix35.Xy = -0.69859802631732315
    rotMatrix35.Xz = 0.069373600702317892
    rotMatrix35.Yx = -0.12754552890773563
    rotMatrix35.Yy = 0.22592234349996876
    rotMatrix35.Yz = 0.96575940728689103
    rotMatrix35.Zx = -0.69035066227570896
    rotMatrix35.Zy = 0.67891081323913249
    rotMatrix35.Zz = -0.24999214140141904
    translation297 = NXOpen.Point3d(80.561830461630706, -101.07804786783093, -156.2416639665808)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix35, translation297, 1.0909458498332663)
    
    scaleAboutPoint188 = NXOpen.Point3d(35.408876318261221, -32.983610817010643, 0.0)
    viewCenter188 = NXOpen.Point3d(-35.408876318261427, 32.983610817010558, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint188, viewCenter188)
    
    scaleAboutPoint189 = NXOpen.Point3d(28.327101054608971, -26.386888653608509, 0.0)
    viewCenter189 = NXOpen.Point3d(-28.327101054609169, 26.386888653608441, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint189, viewCenter189)
    
    scaleAboutPoint190 = NXOpen.Point3d(22.661680843687151, -21.109510922886834, 0.0)
    viewCenter190 = NXOpen.Point3d(-22.661680843687364, 21.109510922886741, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint190, viewCenter190)
    
    face14 = component6.FindObject("PROTO#.Features|SIMPLE HOLE(8:1A)|FACE 3 {(7,-4,-7.5) EXTRUDE(6)}")
    line19 = workPart.Lines.CreateFaceAxis(face14, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId144 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint13 = componentPositioner29.CreateConstraint(True)
    
    componentConstraint13 = constraint13
    componentConstraint13.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge18 = component13.FindObject("PROTO#.Features|EXTRUDE(2)|EDGE * 150 SIMPLE HOLE(4:1A) 3 {(4.2990381056767,0,2.25)(3,0,4.5)(1.7009618943233,0,2.25) EXTRUDE(2)}")
    constraintReference24 = componentConstraint13.CreateConstraintReference(component13, edge18, False, False, False)
    
    helpPoint23 = NXOpen.Point3d(4.7922448457425544, 57.492490337762213, -22.458896935130554)
    constraintReference24.HelpPoint = helpPoint23
    
    edge19 = component6.FindObject("PROTO#.Features|EXTRUDE(6)|EDGE * 270 SIMPLE HOLE(8:1A) 3 {(8.2990381056767,-5,-6.75)(7,-5,-4.5)(5.7009618943233,-5,-6.75) EXTRUDE(6)}")
    constraintReference25 = componentConstraint13.CreateConstraintReference(component6, edge19, False, False, False)
    
    helpPoint24 = NXOpen.Point3d(16.498840888385033, 54.292490337762459, 61.956343264352405)
    constraintReference25.HelpPoint = helpPoint24
    
    constraintReference25.SetFixHint(True)
    
    objects19 = [NXOpen.TaggedObject.Null] * 1 
    objects19[0] = line19
    nErrs74 = theSession.UpdateManager.AddObjectsToDeleteList(objects19)
    
    componentNetwork29.Solve()
    
    rotMatrix36 = NXOpen.Matrix3x3()
    
    rotMatrix36.Xx = 0.13235803712464031
    rotMatrix36.Xy = -0.96634004323979228
    rotMatrix36.Xz = 0.22060886391943074
    rotMatrix36.Yx = -0.12284501138485639
    rotMatrix36.Yy = 0.20485869238321353
    rotMatrix36.Yz = 0.97105201680079589
    rotMatrix36.Zx = -0.98356009129404876
    rotMatrix36.Zy = -0.15562723728945968
    rotMatrix36.Zz = -0.091595359201671958
    translation298 = NXOpen.Point3d(18.035598183222646, -84.325562131329633, -97.490385262324466)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix36, translation298, 2.1307536129555982)
    
    rotMatrix37 = NXOpen.Matrix3x3()
    
    rotMatrix37.Xx = 0.98905688685311077
    rotMatrix37.Xy = -0.037619381813319953
    rotMatrix37.Xz = 0.14265783077144864
    rotMatrix37.Yx = -0.14468828983597343
    rotMatrix37.Yy = -0.058309821931985362
    rotMatrix37.Yz = 0.98775769470584285
    rotMatrix37.Zx = -0.028840481146697412
    rotMatrix37.Zy = -0.99758946805699722
    rotMatrix37.Zz = -0.063114814972264482
    translation299 = NXOpen.Point3d(-85.168064669349306, -69.050412513480211, -113.40943695276002)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix37, translation299, 2.1307536129555982)
    
    markId145 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    theSession.DeleteUndoMark(markId145, None)
    
    markId146 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs75 = theSession.UpdateManager.DoUpdate(markId143)
    
    componentNetwork29.Solve()
    
    componentPositioner29.ClearNetwork()
    
    nErrs76 = theSession.UpdateManager.AddToDeleteList(componentNetwork29)
    
    componentPositioner29.DeleteNonPersistentConstraints()
    
    nErrs77 = theSession.UpdateManager.DoUpdate(markId143)
    
    theSession.DeleteUndoMark(markId146, None)
    
    theSession.SetUndoMarkName(markId142, "Assembly Constraints")
    
    componentPositioner29.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner29.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId143, None)
    
    theSession.DeleteUndoMark(markId144, None)
    
    theSession.DeleteUndoMark(markId141, None)
    
    rotMatrix38 = NXOpen.Matrix3x3()
    
    rotMatrix38.Xx = 0.57441488500679272
    rotMatrix38.Xy = -0.80607202598453065
    rotMatrix38.Xz = 0.14246202584486037
    rotMatrix38.Yx = -0.012306694759530891
    rotMatrix38.Yy = 0.16551498356403066
    rotMatrix38.Yz = 0.98613048603107911
    rotMatrix38.Zx = -0.81847179862639374
    rotMatrix38.Zy = -0.56820126640213131
    rotMatrix38.Zz = 0.085154187872845954
    translation300 = NXOpen.Point3d(-16.163773646459198, -89.829273663939631, -92.131291013712911)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix38, translation300, 2.1307536129555982)
    
    scaleAboutPoint191 = NXOpen.Point3d(-40.977285909133265, -23.965503577159762, 0.0)
    viewCenter191 = NXOpen.Point3d(40.977285909133037, 23.965503577159645, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint191, viewCenter191)
    
    scaleAboutPoint192 = NXOpen.Point3d(-51.221607386416551, -29.956879471449675, 0.0)
    viewCenter192 = NXOpen.Point3d(51.221607386416323, 29.956879471449557, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint192, viewCenter192)
    
    scaleAboutPoint193 = NXOpen.Point3d(-64.027009233020678, -37.446099339312077, 0.0)
    viewCenter193 = NXOpen.Point3d(64.027009233020451, 37.446099339311957, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint193, viewCenter193)
    
    scaleAboutPoint194 = NXOpen.Point3d(-79.548708441025681, -46.807624174140123, 0.0)
    viewCenter194 = NXOpen.Point3d(79.548708441025425, 46.807624174139974, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint194, viewCenter194)
    
    rotMatrix39 = NXOpen.Matrix3x3()
    
    rotMatrix39.Xx = 0.97662758137857553
    rotMatrix39.Xy = 0.093358738448902912
    rotMatrix39.Xz = 0.19360452795805369
    rotMatrix39.Yx = -0.19373391609834936
    rotMatrix39.Yy = -0.0077623877945731425
    rotMatrix39.Yz = 0.9810234019068681
    rotMatrix39.Zx = 0.093089940615671954
    rotMatrix39.Zy = -0.99560227565577297
    rotMatrix39.Zz = 0.010505791984170988
    translation301 = NXOpen.Point3d(-152.50042135459182, -102.97607109136636, -124.1779183938533)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix39, translation301, 0.87275667986661309)
    
    # 此一區段嘗試將已經完成的組立檔案轉為 binary STL 
    sTLCreator = theSession.DexManager.CreateStlCreator()
    
    sTLCreator.AutoNormalGen = True
    
    sTLCreator.ChordalTol = 0.080000000000000002
    
    sTLCreator.AdjacencyTol = 0.080000000000000002
    
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
    added1 = sTLCreator.ExportSelectionBlock.Add(objects1)
    
    STLfileName = current_directory + "\\platform_assembly.stl"
    
    if os.path.exists(STLfileName):
        # 若希望存檔的組立檔案存在, 則先刪除該檔案
        os.remove(STLfileName)
    
    sTLCreator.OutputFile = STLfileName
    nXObject = sTLCreator.Commit()
    sTLCreator.Destroy()
    
    # 嘗試將完成的平台組立檔儲存為 platform_assembly.prt
    # 但是可能需要將先前的同名組立檔案移除
    
    fileName = current_directory + "\\platform_assembly.prt"
    
    if os.path.exists(fileName):
        # 若希望存檔的組立檔案存在, 則先刪除該檔案
        os.remove(fileName)
    
    # 將前面所完成的組立檔案存檔
    partSaveStatus1 = workPart.SaveAs(fileName)
    
    partSaveStatus1.Dispose()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    print("已經完成組立檔案與 STL 檔案的儲存!")
    
if __name__ == '__main__':
    main()