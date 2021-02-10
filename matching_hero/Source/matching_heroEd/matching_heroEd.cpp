// Fill out your copyright notice in the Description page of Project Settings.

#include "matching_heroEd.h"
#include "Modules/ModuleManager.h"


DEFINE_LOG_CATEGORY(MatchingHeroEd);


class FMatchingHeroEd : public IMatchingHeroEd
{
	/** IModuleInterface implementation */
	virtual void StartupModule() override;
	virtual void ShutdownModule() override;
};
IMPLEMENT_MODULE(FMatchingHeroEd, matching_heroEd)

void FMatchingHeroEd::StartupModule()
{
	// This code will execute after your module is loaded into memory (but after global variables are initialized, of course.) 
}
void FMatchingHeroEd::ShutdownModule()
{
	// This function may be called during shutdown to clean up your module.  For modules that support dynamic reloading, 
	// we call this function before unloading the module. 
}
