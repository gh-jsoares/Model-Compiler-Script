import os


class COLORS:
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    RED = '\033[91m'
    REDBG = '\033[41m'

    GREEN = '\033[92m'
    GREENBG = '\033[42m'

    BLUE = '\033[94m'
    BLUEBG = '\033[44m'


def errorMessage(msg):
    print(
        f"{COLORS.RED}{COLORS.BOLD}{COLORS.UNDERLINE}[ERROR]{COLORS.ENDC} {COLORS.RED}{msg}{COLORS.ENDC}")


def successMessage(msg):
    print(
        f"{COLORS.GREEN}{COLORS.BOLD}{COLORS.UNDERLINE}[SUCCESS]{COLORS.ENDC} {COLORS.GREEN}{msg}{COLORS.ENDC}")


def infoMessage(msg):
    print(
        f"{COLORS.BLUE}{COLORS.BOLD}{COLORS.UNDERLINE}[INFO]{COLORS.ENDC} {COLORS.BLUE}{msg}{COLORS.ENDC}")


def promptMessage(msg):
    print(
        f"{COLORS.BLUE}{msg}{COLORS.ENDC}")


PARENT_DIR = "../exported"
TEMPLATE = open("compile.qc", "r")
QC_CONTENT = TEMPLATE.readlines()
TEMPLATE.close()


def main():
    propDirs = [f for f in os.listdir(
        PARENT_DIR) if os.path.isdir(f"{PARENT_DIR}/{f}")]
    for propDir in propDirs:
        currentDir = f"{PARENT_DIR}/{propDir}"
        smdfiles = [f for f in os.listdir(f"{currentDir}") if os.path.isfile(
            f"{currentDir}/{f}") and f.find(".smd") != -1 and f.find("phys") == -1]
        qcfiles = [f for f in os.listdir(f"{currentDir}") if os.path.isfile(
            f"{currentDir}/{f}") and f.find(".qc") != -1]

        # no smd or already compiled
        if len(smdfiles) == 0 or len(qcfiles) != 0:
            continue

        modelName = smdfiles[0].split(".smd")[0]
        infoMessage(f"Selected model '{currentDir}/{modelName}'")
        chosenPath = requestModelCategory()
        chosenSurface = requestSurfaceProp()
        saveFile(f"{currentDir}",
                 modelName, chosenPath, chosenSurface)


def saveFile(propDir, modelName, modelPath, surface):
    newcontent = list(map(lambda x: x.replace(
        "MODELNAME", modelName).replace("MODELPATH", modelPath).replace("SURFACE", surface), QC_CONTENT))

    qcFile = f"{propDir}/{modelName}.qc"
    output = open(qcFile, "w")
    output.writelines(newcontent)
    output.close()
    successMessage(f"Saved {qcFile}")


def requestSurfaceProp():
    SURFACES = {
        "Special": [
            "default",
            "default_silent",
            "floatingstandable",
            "item",
            "ladder",
            "no_decal",
            "player",
            "player_control_clip",
        ],
        "Concrete / Rock": [
            "brick",
            "concrete",
            "concrete_block",
            "gravel",
            "rock",
        ],
        "Metal": [
            "canister",
            "chain",
            "chainlink",
            "combine_metal",
            "crowbar",
            "floating_metal_barrel",
            "grenade",
            "gunship",
            "metal",
            "metal_barrel",
            "metal_bouncy",
            "Metal_Box",
            "metal_seafloorcar",
            "metalgrate",
            "metalpanel",
            "metalvent",
            "metalvehicle",
            "paintcan",
            "popcan",
            "roller",
            "slipperymetal",
            "solidmetal",
            "strider",
            "weapon",
        ],
        "Wood": [
            "Wood",
            "Wood_Box",
            "Wood_Furniture",
            "Wood_Plank",
            "Wood_Panel",
            "Wood_Solid",
        ],
        "Terrain": [
            "dirt",
            "grass",
            "gravel",
            "mud",
            "quicksand",
            "sand",
            "slipperyslime",
            "antlionsand",
        ],
        "Liquid": [
            "slime",
            "water",
            "wade",
            "puddle",
        ],
        "Frozen": [
            "ice",
            "snow",
        ],
        "Organic": [
            "alienflesh",
            "antlion",
            "armorflesh",
            "bloodyflesh",
            "flesh",
            "foliage",
            "watermelon",
            "zombieflesh",
        ],
        "Manufactured": [
            "glass",
            "glassbottle",
            "combine_glass",
            "tile",
            "paper",
            "papercup",
            "cardboard",
            "plaster",
            "plastic_barrel",
            "plastic_barrel_buoyant",
            "Plastic_Box",
            "plastic",
            "rubber",
            "rubbertire",
            "slidingrubbertire",
            "slidingrubbertire_front",
            "slidingrubbertire_rear",
            "jeeptire",
            "brakingrubbertire",
        ],
        "Miscellaneous": [
            "carpet",
            "ceiling_tile",
            "computer",
            "pottery",
        ],
    }

    surfaceKeys = list(SURFACES.keys())
    while True:
        infoMessage("Choose the category of the surface for this prop:")
        for i, category in enumerate(surfaceKeys):
            promptMessage(f"\t[{i + 1}]: '{category}'")

        option = input("> ")
        if not option.isnumeric() or not (0 < int(option) <= len(surfaceKeys)):
            errorMessage("Invalid option")
        else:
            category = surfaceKeys[int(option) - 1]
            chosen = None
            while True:
                surfacesVals = SURFACES[category]
                infoMessage(
                    f"Choose the surface for this prop from '{category}':")
                lenSurfaces = len(surfacesVals)
                for i, surface in enumerate(surfacesVals):
                    promptMessage(f"\t[{i + 1}]: '{surface}'")
                promptMessage(f"\t[{lenSurfaces + 1}]: Back")

                option = input("> ")
                if not option.isnumeric() or not (0 < int(option) <= lenSurfaces + 1):
                    errorMessage("Invalid option")
                elif int(option) - 1 == lenSurfaces:
                    break
                else:
                    chosen = surfacesVals[int(option) - 1]
                    successMessage(f"Chosen '{chosen}' from '{category}'")
                    break
            if not chosen is None:
                return chosen


def requestModelCategory():
    paths = [
        "\\ayjay\\props\\furniture\\",
        "\\ayjay\\props\\furniture\\casino\\",
        "\\ayjay\\props\\environment\\",
        "\\ayjay\\props\\environment\\casino\\",
        "\\ayjay\\props\\environment\\street\\",
    ]
    while True:
        infoMessage("Choose the path for this model:")
        for i, path in enumerate(paths):
            promptMessage(f"\t[{i + 1}]: '{path}'")

        option = input("> ")
        if not option.isnumeric() or not (0 < int(option) <= len(paths)):
            errorMessage("Invalid option")
        else:
            chosen = paths[int(option) - 1]
            successMessage(f"Chosen '{chosen}'")
            return chosen


if __name__ == "__main__":
    main()
