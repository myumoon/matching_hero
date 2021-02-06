// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "Blueprint/UserWidget.h"
#include "Rendering/RenderingCommon.h"
#include "UMGDrawer.generated.h"


USTRUCT(BlueprintType)
struct MATCHING_HERO_API FSlateVertexBP {
	GENERATED_BODY()

	UPROPERTY(BlueprintReadWrite)
	FVector4 TexCoords;
	
	UPROPERTY(BlueprintReadWrite)
	FVector2D MaterialTexCoords;
	
	UPROPERTY(BlueprintReadWrite)
	FVector2D Position;
	
	UPROPERTY(BlueprintReadWrite)
	FColor Color;
	
	UPROPERTY(BlueprintReadWrite)
	int32 PixelWidth;
	
	UPROPERTY(BlueprintReadWrite)
	int32 PixelHeight;

	FSlateVertex Make() const
	{
		FSlateVertex result;
		result.TexCoords[0] = TexCoords.X;
		result.TexCoords[1] = TexCoords.Y;
		result.TexCoords[2] = TexCoords.Z;
		result.TexCoords[3] = TexCoords.W;
		result.MaterialTexCoords = MaterialTexCoords;
		result.Position = Position;
		result.Color = Color;
		result.PixelSize[0] = PixelWidth;
		result.PixelSize[1] = PixelHeight;
		return result;
	}
};


/**
 *	UMGï`âÊä÷êî
 */
UCLASS()
class MATCHING_HERO_API UUMGDrawer : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

public:
	UFUNCTION(BlueprintCallable, Category = "Painting")
	static void DrawCustomVerts(UPARAM(ref) FPaintContext& Context, class USlateBrushAsset* Brush, const TArray<FSlateVertexBP>& InVerts, const TArray<int32>& InIndices);

	UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Painting")
	static FVector2D TransformPointFromPaintContext(UPARAM(ref) FPaintContext& Context, const FVector2D& Point);

	UFUNCTION(BlueprintCallable, BlueprintPure, Category = "Painting")
	static FVector2D GetLocalSizeFromPaintContext(UPARAM(ref) FPaintContext& Context);
};


