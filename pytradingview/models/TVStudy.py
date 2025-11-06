from ..core.TVBridge import TVBridge
from ..core.TVBridgeObject import TVMethodResponse
from ..core.TVObject import TVObject

import sys
from typing import Any, Dict, Optional, List


class TVStudy(TVObject):
    """
    TradingView Study API implementation.
    API object for interacting with a study.
    Corresponds to the IStudyApi interface in TypeScript.
    
    You can retrieve this interface by using the IChartWidgetApi.getStudyById method.
    """
    async def isUserEditEnabled(self) -> bool:
        """
        Get if user editing is enabled for the study.
        
        :return: True if editing is enabled, False otherwise
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setUserEditEnabled(self, enabled: bool) -> None:
        """
        Set if user editing is enabled for the study.
        
        :param enabled: True if editing should be enabled, False otherwise
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"enabled": enabled}
        )

    async def getInputsInfo(self) -> List[Any]:
        """
        Get descriptions of the study inputs.
        
        :return: List of study input information
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def getInputValues(self) -> List[Any]:
        """
        Get current values of the study inputs.
        
        :return: List of study input values
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setInputValues(self, values: List[Any]) -> None:
        """
        Set the value of one or more study inputs.
        
        :param values: Study input values to set
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"values": values}
        )

    async def getStyleInfo(self) -> Dict[str, Any]:
        """
        Get descriptions of study styles.
        
        :return: Study style information
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def getStyleValues(self) -> Dict[str, Any]:
        """
        Get current values of the study styles.
        
        :return: Study style values
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def mergeUp(self) -> None:
        """
        Merge the study into the pane above, if possible.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )

    async def mergeDown(self) -> None:
        """
        Merge the study into the pane below, if possible.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )

    async def unmergeUp(self) -> None:
        """
        Unmerge the study into the pane above, if possible.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )

    async def unmergeDown(self) -> None:
        """
        Unmerge the study into the pane below, if possible.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )

    async def changePriceScale(self, newPriceScale: Any) -> None:
        """
        Change the price scale that the study is attached to.
        
        :param newPriceScale: Price scale identifier, or the ID of another study whose price scale the study should be moved to
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"newPriceScale": newPriceScale}
        )

    async def isVisible(self) -> bool:
        """
        Get if the study is visible.
        
        :return: True if visible, False otherwise
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def setVisible(self, visible: bool) -> None:
        """
        Set the study visibility.
        
        :param visible: True if the study should be visible, False otherwise
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"visible": visible}
        )

    async def bringToFront(self) -> None:
        """
        Move the study visually in front of all other chart objects.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )

    async def sendToBack(self) -> None:
        """
        Move the study visually behind of all other chart objects.
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )

    async def applyOverrides(self, overrides: Any) -> None:
        """
        Override one or more of the indicator's properties.
        Refer to Indicator Overrides for more information.
        Overrides for built-in indicators are listed in SingleIndicatorOverrides.
        
        :param overrides: Property values to override
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={"overrides": overrides}
        )

    async def applyToEntireLayout(self) -> None:
        """
        Copies the study to all charts in the layout.
        Only applicable to multi-chart layouts (Trading Platform).
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )

    async def onDataLoaded(self) -> Any:
        """
        Get a subscription that can be used to subscribe a callback when the study data has loaded.
        
        :return: A subscription
        
        Example:
            studyApi.onDataLoaded().subscribe(
                null,
                () => console.log('Study data is loaded'),
                true
            );
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result

    async def onStudyError(self) -> Any:
        """
        Get a subscription that can be used to subscribe a callback when the study has an error.
        
        :return: A subscription
        
        Example:
            studyApi.onStudyError().subscribe(
                null,
                () => console.log('Study error'),
                true
            );
        """
        resp: TVMethodResponse = await self.call_web_object_method(
            method_name=sys._getframe(0).f_code.co_name, kwargs={}
        )
        return resp.result
