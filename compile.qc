$modelname									"MODELPATH"
$body 			MODELNAME					"MODELNAME.smd"
$staticprop
$surfaceprop								SURFACE
$cdmaterials								"modelsMODELPATH"

$sequence 		idle						"MODELNAME.smd"

$collisionmodel								"MODELNAME_phys.smd" { $concave }
