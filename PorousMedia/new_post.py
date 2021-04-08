# trace generated using paraview version 5.8.1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
casefoam = OpenFOAMReader(FileName='case.foam')
casefoam.MeshRegions = ['internalMesh']

# Properties modified on casefoam
casefoam.CaseType = 'Decomposed Case'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [774, 792]

# get layout
layout1 = GetLayout()

# show data in view
casefoamDisplay = Show(casefoam, renderView1, 'UnstructuredGridRepresentation')

# Properties modified on animationScene1
animationScene1.AnimationTime = 1000.0

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [3.255275876447244, 0.0, 0.0]
renderView1.CameraViewUp = [0.0, 1.0, 2.220446049250313e-16]
renderView1.CameraParallelScale = 0.8437983842594279

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# trace defaults for the display properties.
casefoamDisplay.Representation = 'Surface'
casefoamDisplay.ColorArrayName = ['POINTS', 'p']
casefoamDisplay.LookupTable = pLUT
casefoamDisplay.OSPRayScaleArray = 'p'
casefoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
casefoamDisplay.SelectOrientationVectors = 'U'
casefoamDisplay.ScaleFactor = 0.12000000476837158
casefoamDisplay.SelectScaleArray = 'p'
casefoamDisplay.GlyphType = 'Arrow'
casefoamDisplay.GlyphTableIndexArray = 'p'
casefoamDisplay.GaussianRadius = 0.006000000238418579
casefoamDisplay.SetScaleArray = ['POINTS', 'p']
casefoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
casefoamDisplay.OpacityArray = ['POINTS', 'p']
casefoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
casefoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
casefoamDisplay.PolarAxes = 'PolarAxesRepresentation'
casefoamDisplay.ScalarOpacityFunction = pPWF
casefoamDisplay.ScalarOpacityUnitDistance = 0.036150676204188645
casefoamDisplay.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
casefoamDisplay.ScaleTransferFunction.Points = [-2.8482005291152745e-05, 0.0, 0.5, 0.0, 0.035639699548482895, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
casefoamDisplay.OpacityTransferFunction.Points = [-2.8482005291152745e-05, 0.0, 0.5, 0.0, 0.035639699548482895, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
casefoamDisplay.SetScalarBarVisibility(renderView1, True)

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# create a new 'Clip'
clip1 = Clip(Input=casefoam)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'p']
clip1.Value = 0.01780560877159587

# Properties modified on casefoam
casefoam.CellArrays = ['U', 'UMean', 'UPrime2Mean', 'epsilon', 'k', 'nut', 'p', 'pMean', 'pPrime2Mean']

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'p']
clip1Display.LookupTable = pLUT
clip1Display.OSPRayScaleArray = 'p'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'U'
clip1Display.ScaleFactor = 0.12000000476837158
clip1Display.SelectScaleArray = 'p'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'p'
clip1Display.GaussianRadius = 0.006000000238418579
clip1Display.SetScaleArray = ['POINTS', 'p']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'p']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = pPWF
clip1Display.ScalarOpacityUnitDistance = 0.04031182078484797
clip1Display.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [-2.8482005291152745e-05, 0.0, 0.5, 0.0, 0.03410074859857559, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [-2.8482005291152745e-05, 0.0, 0.5, 0.0, 0.03410074859857559, 1.0, 0.5, 0.0]

# hide data in view
Hide(casefoam, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=clip1,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [-0.4000000059604645, -0.6000000238418579, -0.4000000059604645]
plotOverLine1.Source.Point2 = [2.7232109254225756e-18, 0.6000000238418579, 0.4000000059604645]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1Display.LookupTable = pLUT
plotOverLine1Display.OSPRayScaleArray = 'p'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'U'
plotOverLine1Display.ScaleFactor = 0.12000000476837158
plotOverLine1Display.SelectScaleArray = 'p'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'p'
plotOverLine1Display.GaussianRadius = 0.006000000238418579
plotOverLine1Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'p']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [0.00019653234630823135, 0.0, 0.5, 0.0, 0.02836770936846733, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [0.00019653234630823135, 0.0, 0.5, 0.0, 0.02836770936846733, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')
# uncomment following to set a specific view size
# lineChartView2.ViewSize = [400, 400]

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView2, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [0]
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['epsilon', 'k', 'nut', 'p', 'pMean', 'pPrime2Mean', 'U_Magnitude', 'UMean_Magnitude', 'UPrime2Mean_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'epsilon', 'epsilon', 'k', 'k', 'nut', 'nut', 'p', 'p', 'pMean', 'pMean', 'pPrime2Mean', 'pPrime2Mean', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'UMean_X', 'UMean_X', 'UMean_Y', 'UMean_Y', 'UMean_Z', 'UMean_Z', 'UMean_Magnitude', 'UMean_Magnitude', 'UPrime2Mean_XX', 'UPrime2Mean_XX', 'UPrime2Mean_YY', 'UPrime2Mean_YY', 'UPrime2Mean_ZZ', 'UPrime2Mean_ZZ', 'UPrime2Mean_XY', 'UPrime2Mean_XY', 'UPrime2Mean_YZ', 'UPrime2Mean_YZ', 'UPrime2Mean_XZ', 'UPrime2Mean_XZ', 'UPrime2Mean_Magnitude', 'UPrime2Mean_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'epsilon', '0.89', '0.1', '0.11', 'k', '0.22', '0.49', '0.72', 'nut', '0.3', '0.69', '0.29', 'p', '0.6', '0.31', '0.64', 'pMean', '1', '0.5', '0', 'pPrime2Mean', '0.65', '0.34', '0.16', 'U_X', '0', '0', '0', 'U_Y', '0.89', '0.1', '0.11', 'U_Z', '0.22', '0.49', '0.72', 'U_Magnitude', '0.3', '0.69', '0.29', 'UMean_X', '0.6', '0.31', '0.64', 'UMean_Y', '1', '0.5', '0', 'UMean_Z', '0.65', '0.34', '0.16', 'UMean_Magnitude', '0', '0', '0', 'UPrime2Mean_XX', '0.89', '0.1', '0.11', 'UPrime2Mean_YY', '0.22', '0.49', '0.72', 'UPrime2Mean_ZZ', '0.3', '0.69', '0.29', 'UPrime2Mean_XY', '0.6', '0.31', '0.64', 'UPrime2Mean_YZ', '1', '0.5', '0', 'UPrime2Mean_XZ', '0.65', '0.34', '0.16', 'UPrime2Mean_Magnitude', '0', '0', '0', 'vtkValidPointMask', '0.89', '0.1', '0.11', 'Points_X', '0.22', '0.49', '0.72', 'Points_Y', '0.3', '0.69', '0.29', 'Points_Z', '0.6', '0.31', '0.64', 'Points_Magnitude', '1', '0.5', '0']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'pMean', '0', 'pPrime2Mean', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'UMean_X', '0', 'UMean_Y', '0', 'UMean_Z', '0', 'UMean_Magnitude', '0', 'UPrime2Mean_XX', '0', 'UPrime2Mean_YY', '0', 'UPrime2Mean_ZZ', '0', 'UPrime2Mean_XY', '0', 'UPrime2Mean_YZ', '0', 'UPrime2Mean_XZ', '0', 'UPrime2Mean_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'epsilon', '1', 'k', '1', 'nut', '1', 'p', '1', 'pMean', '1', 'pPrime2Mean', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'UMean_X', '1', 'UMean_Y', '1', 'UMean_Z', '1', 'UMean_Magnitude', '1', 'UPrime2Mean_XX', '1', 'UPrime2Mean_YY', '1', 'UPrime2Mean_ZZ', '1', 'UPrime2Mean_XY', '1', 'UPrime2Mean_YZ', '1', 'UPrime2Mean_XZ', '1', 'UPrime2Mean_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'epsilon', '2', 'k', '2', 'nut', '2', 'p', '2', 'pMean', '2', 'pPrime2Mean', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'UMean_X', '2', 'UMean_Y', '2', 'UMean_Z', '2', 'UMean_Magnitude', '2', 'UPrime2Mean_XX', '2', 'UPrime2Mean_YY', '2', 'UPrime2Mean_ZZ', '2', 'UPrime2Mean_XY', '2', 'UPrime2Mean_YZ', '2', 'UPrime2Mean_XZ', '2', 'UPrime2Mean_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'pMean', '0', 'pPrime2Mean', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'UMean_X', '0', 'UMean_Y', '0', 'UMean_Z', '0', 'UMean_Magnitude', '0', 'UPrime2Mean_XX', '0', 'UPrime2Mean_YY', '0', 'UPrime2Mean_ZZ', '0', 'UPrime2Mean_XY', '0', 'UPrime2Mean_YZ', '0', 'UPrime2Mean_XZ', '0', 'UPrime2Mean_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'epsilon', '4', 'k', '4', 'nut', '4', 'p', '4', 'pMean', '4', 'pPrime2Mean', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'UMean_X', '4', 'UMean_Y', '4', 'UMean_Z', '4', 'UMean_Magnitude', '4', 'UPrime2Mean_XX', '4', 'UPrime2Mean_YY', '4', 'UPrime2Mean_ZZ', '4', 'UPrime2Mean_XY', '4', 'UPrime2Mean_YZ', '4', 'UPrime2Mean_XZ', '4', 'UPrime2Mean_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView2, layout=layout1, hint=1)

# update the view to ensure updated data information
lineChartView2.Update()

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = []
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'epsilon', '0.889998', '0.100008', '0.110002', 'k', '0.220005', '0.489998', '0.719997', 'nut', '0.300008', '0.689998', '0.289998', 'p', '0.6', '0.310002', '0.639994', 'pMean', '1', '0.500008', '0', 'pPrime2Mean', '0.650004', '0.340002', '0.160006', 'U_X', '0', '0', '0', 'U_Y', '0.889998', '0.100008', '0.110002', 'U_Z', '0.220005', '0.489998', '0.719997', 'U_Magnitude', '0.300008', '0.689998', '0.289998', 'UMean_X', '0.6', '0.310002', '0.639994', 'UMean_Y', '1', '0.500008', '0', 'UMean_Z', '0.650004', '0.340002', '0.160006', 'UMean_Magnitude', '0', '0', '0', 'UPrime2Mean_XX', '0.889998', '0.100008', '0.110002', 'UPrime2Mean_YY', '0.220005', '0.489998', '0.719997', 'UPrime2Mean_ZZ', '0.300008', '0.689998', '0.289998', 'UPrime2Mean_XY', '0.6', '0.310002', '0.639994', 'UPrime2Mean_YZ', '1', '0.500008', '0', 'UPrime2Mean_XZ', '0.650004', '0.340002', '0.160006', 'UPrime2Mean_Magnitude', '0', '0', '0', 'vtkValidPointMask', '0.889998', '0.100008', '0.110002', 'Points_X', '0.220005', '0.489998', '0.719997', 'Points_Y', '0.300008', '0.689998', '0.289998', 'Points_Z', '0.6', '0.310002', '0.639994', 'Points_Magnitude', '1', '0.500008', '0']
plotOverLine1Display_1.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'UMean_Magnitude', '0', 'UMean_X', '0', 'UMean_Y', '0', 'UMean_Z', '0', 'UPrime2Mean_Magnitude', '0', 'UPrime2Mean_XX', '0', 'UPrime2Mean_XY', '0', 'UPrime2Mean_XZ', '0', 'UPrime2Mean_YY', '0', 'UPrime2Mean_YZ', '0', 'UPrime2Mean_ZZ', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'pMean', '0', 'pPrime2Mean', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'UMean_Magnitude', '1', 'UMean_X', '1', 'UMean_Y', '1', 'UMean_Z', '1', 'UPrime2Mean_Magnitude', '1', 'UPrime2Mean_XX', '1', 'UPrime2Mean_XY', '1', 'UPrime2Mean_XZ', '1', 'UPrime2Mean_YY', '1', 'UPrime2Mean_YZ', '1', 'UPrime2Mean_ZZ', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'epsilon', '1', 'k', '1', 'nut', '1', 'p', '1', 'pMean', '1', 'pPrime2Mean', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'UMean_Magnitude', '2', 'UMean_X', '2', 'UMean_Y', '2', 'UMean_Z', '2', 'UPrime2Mean_Magnitude', '2', 'UPrime2Mean_XX', '2', 'UPrime2Mean_XY', '2', 'UPrime2Mean_XZ', '2', 'UPrime2Mean_YY', '2', 'UPrime2Mean_YZ', '2', 'UPrime2Mean_ZZ', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'epsilon', '2', 'k', '2', 'nut', '2', 'p', '2', 'pMean', '2', 'pPrime2Mean', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'UMean_Magnitude', '0', 'UMean_X', '0', 'UMean_Y', '0', 'UMean_Z', '0', 'UPrime2Mean_Magnitude', '0', 'UPrime2Mean_XX', '0', 'UPrime2Mean_XY', '0', 'UPrime2Mean_XZ', '0', 'UPrime2Mean_YY', '0', 'UPrime2Mean_YZ', '0', 'UPrime2Mean_ZZ', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'pMean', '0', 'pPrime2Mean', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'UMean_Magnitude', '4', 'UMean_X', '4', 'UMean_Y', '4', 'UMean_Z', '4', 'UPrime2Mean_Magnitude', '4', 'UPrime2Mean_XX', '4', 'UPrime2Mean_XY', '4', 'UPrime2Mean_XZ', '4', 'UPrime2Mean_YY', '4', 'UPrime2Mean_YZ', '4', 'UPrime2Mean_ZZ', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'epsilon', '4', 'k', '4', 'nut', '4', 'p', '4', 'pMean', '4', 'pPrime2Mean', '4', 'vtkValidPointMask', '4']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['p']


