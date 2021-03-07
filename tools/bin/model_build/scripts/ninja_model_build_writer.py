#!usr/bin/python
# -*- coding: utf-8 -*-
# 

import os
import sys
import optparse
import codecs
import glob


import ply_path

sys.path.append(os.path.join(os.path.dirname(__file__),'..','..'))
import proj_def

sys.path.append(os.path.join(os.path.dirname(__file__),'..','..','..','thirdparty','ninja','misc'))
from ninja_syntax import Writer

def getUE4ContentPath(fbxPath):
	meshPath = fbxPath.replace("$res_dest", "$ue4_proj_root")
	meshPath = meshPath.replace(".fbx", ".uasset")
	texPath  = meshPath.replace("Meshes", "Textures")
	matPath  = meshPath.replace("Meshes", "Material")
	return (meshPath, texPath, matPath)

def makeUE4ImportingFileList(fbxList):
	importFiles = []
	for f in fbxList:
		meshPath, texPath, materialPath = getUE4ContentPath(f)
		importFiles.append(meshPath)
		importFiles.append(texPath)
		importFiles.append(materialPath)
	return importFiles

def main():	
	print("{}".format(os.path.basename(__file__)))
	current_dir = os.path.abspath(os.path.dirname(__file__))
	parser = optparse.OptionParser(description=u"Make a ninja build file.")
	parser.add_option("-o", "--out", default=os.path.join(current_dir, "ninja", "build.ninja"), help=u"ninja config path")
	parser.add_option("-r", "--rule", default="rule.ninja", help=u"ninja rule path")

	options, args = parser.parse_args()

	if not os.path.exists(os.path.dirname(options.out)):
		os.makedirs(os.path.dirname(options.out))

	with codecs.open(options.out, 'w', 'utf-8') as f:
		writer = Writer(f)

		writer.comment("ビルド設定")
		writer.newline()

		# ルールファイルインクルード
		writer.include(options.rule)
		writer.newline()
		
		writer.comment("plyをfbxにビルド")
		fbxList = []

		if True:
			fileItereter = lambda : glob.glob(os.path.join(proj_def.ResRoot, "models", "characters") + "/**/**.ply", recursive=True)
		else:
			fileItereter = lambda : ["D:/prog/0_myprogram/matching_hero_resources/models/characters/p006_hashiyasume/01_otnk/p006_01-3.ply"]
			#fileItereter = lambda : ["D:/prog/0_myprogram/matching_hero_resources/models/characters/p003_chitti/09_hidetheblue/p003_09-0.ply"]

		maxCount = -1   # デバッグ用 書き込み数の上限
		for path in fileItereter():
			# デバッグ処理
			if 0 <= maxCount:
				maxCount = maxCount - 1
				if maxCount < 0:
					break

			fbxPath    = ply_path.makeRelativeFbxContentsPath(path)
			#texPath = ply_path.makeRelativeTexContentsPath(path)
			#destFbxPath = os.path.join("$res_root", "Content", "Characters", fbxPath)
			destFbxPath = os.path.join("$res_dest", "MatchingHero", "Characters", fbxPath)
			inputPath   = os.path.join("$res_root", os.path.relpath(path, proj_def.ResRoot))
			writer.build(outputs=[destFbxPath], rule="convert_ply", inputs=[inputPath], implicit=None)
			fbxList.append(destFbxPath)
			

		writer.comment("インポート用csvを作成")
		writer.build(outputs=["$convert_csv"], rule="make_import_csv", inputs=fbxList, implicit=None)

		writer.comment("UE4にインポート")
		ue4ImportFiles = makeUE4ImportingFileList(fbxList)
		writer.build(outputs=ue4ImportFiles, rule="import_ue4", inputs="$convert_csv", implicit=None)

	return 0

if __name__ == "__main__":
	exit(main())
