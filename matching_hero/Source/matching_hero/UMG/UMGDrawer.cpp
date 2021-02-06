// Fill out your copyright notice in the Description page of Project Settings.
#include "UMGDrawer.h"

#include "Rendering/DrawElements.h"
#include "Framework/Application/SlateApplication.h"
#include "Slate/SlateBrushAsset.h"

void UUMGDrawer::DrawCustomVerts(FPaintContext& Context, USlateBrushAsset* Brush, const TArray<FSlateVertexBP>& InVerts, const TArray<int32>& InIndices)
{
	++Context.MaxLayer;

	if(Brush != nullptr) {
		TArray<FSlateVertex> inVertsNative;
		inVertsNative.Reserve(InVerts.Num());
		for(const auto& v : InVerts) {
			inVertsNative.Add(v.Make());
		}

		TArray<SlateIndex> inIndicesNative;
		inIndicesNative.Reserve(InIndices.Num());
		for(const auto& i : InIndices) {
			inIndicesNative.Add(static_cast<SlateIndex>(i));
		}

		FSlateDrawElement::MakeCustomVerts(
			Context.OutDrawElements,
			Context.MaxLayer,
			FSlateApplication::Get().GetRenderer()->GetResourceHandle(Brush->Brush),
			inVertsNative,
			inIndicesNative,
			nullptr,
			0,
			0
		);
	}
}

FVector2D UUMGDrawer::TransformPointFromPaintContext(FPaintContext& Context, const FVector2D& Point)
{
	return Context.AllottedGeometry.ToPaintGeometry().GetAccumulatedRenderTransform().TransformPoint(Point);
}

FVector2D UUMGDrawer::GetLocalSizeFromPaintContext(FPaintContext& Context)
{
	return Context.AllottedGeometry.GetLocalSize();
}
