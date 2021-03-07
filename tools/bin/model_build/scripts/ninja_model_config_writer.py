#!usr/bin/python
# -*- coding: utf-8 -*-
# 

import os
import sys
import optparse
import codecs

# プロジェクト変数
sys.path.append(os.path.join(os.path.dirname(__file__),'..','..'))
import proj_def

# ninja/miscにパスを通す 
sys.path.append(os.path.join(os.path.dirname(__file__),'..','..','..','thirdparty','ninja','misc'))
from ninja_syntax import Writer

def main():	
	print("{}".format(os.path.basename(__file__)))
	current_dir = os.path.abspath(os.path.dirname(__file__))
	parser = optparse.OptionParser(description=u"Make a ninja config file.")
	parser.add_option("-o", "--out", default=os.path.join(current_dir, "ninja", "config.ninja"), help=u"ninja config path")

	options, args = parser.parse_args()

	if not os.path.exists(os.path.dirname(options.out)):
		os.makedirs(os.path.dirname(options.out))

	with codecs.open(options.out, 'w', 'utf-8') as f:
		writer = Writer(f)

		writer.comment("設定定義")
		writer.newline()

		# UE4エンジンコマンド
		writer.comment("UE4エンジンコマンド")
		writer.variable(key="ue4_cmd", value=os.path.join(proj_def.UE4EngineDir, "UE4Editor-Cmd.exe"))

		# リポジトリルート
		writer.comment("プロジェクトルート")
		writer.variable(key="proj_root", value=proj_def.Root)

		# UE4プロジェクトルート
		writer.comment("UE4プロジェクトルート")
		writer.variable(key="ue4_proj_root", value=proj_def.UE4ProjRoot)

		# UE4プロジェクトファイル
		writer.comment("UE4プロジェクトファイル")
		writer.variable(key="ue4_proj_file", value=os.path.join(proj_def.UE4ProjRoot, proj_def.ProjectName + ".uproject"))

		# ツールディレクトリ
		writer.comment("ツールディレクトリ")
		writer.variable(key="tool_dir", value=proj_def.ToolDir)

		# リソースディレクトリ
		writer.comment("リソースディレクトリ")
		writer.variable(key="res_root", value=proj_def.ResRoot)

		# リソース出力ディレクトリ
		writer.comment("出力ディレクトリ")
		writer.variable(key="res_dest", value=proj_def.DestFbxDir)

		# 一時ディレクトリ
		writer.comment("一時ディレクトリ")
		writer.variable(key="temp_dir", value=proj_def.TempDir)

		# モデル変換csv
		writer.comment("モデル変換csv")
		writer.variable(key="convert_csv", value=proj_def.ConvertCsvPath)

		# モデル変換用csv生成
		writer.comment("インポートcsv作成")
		writer.variable(key="import_csv_name", value="../scripts/import_csv_maker.py")

		# モデル変換
		writer.comment("fbx生成")
		writer.variable(key="ply2fbx", value="../../ply2fbx_recursive.py")

	return 0

if __name__ == "__main__":
	exit(main())
