# Amazon Reviews Scraper

Add ASIN numbers in config/asins.csv file and run the reviews spider

Alternate HTML for price

```html

<table class="a-lineitem a-align-top">
    <tbody>
    <tr>
        <td class="a-color-secondary a-size-base a-text-right a-nowrap">M.R.P.:</td>
        <td class="a-span12 a-color-secondary a-size-base"><span class="a-price a-text-price a-size-base"
                                                                 data-a-size="b" data-a-strike="true"
                                                                 data-a-color="secondary"><span class="a-offscreen">₹400.00</span><span
                aria-hidden="true">₹400.00</span></span> <span id="basisPriceLegalMessage_feature_div" class="celwidget"
                                                               data-feature-name="basisPriceLegalMessage"
                                                               data-csa-c-id="rzzamr-2cmlr3-np5g23-qaw1kn"
                                                               data-cel-widget="basisPriceLegalMessage_feature_div">
                                          <span id="listPriceLegalMessage">  </span> <style>
    #listPriceLegalMessageText {
        margin-left: 5px !important;
    }
    
    #listPriceLegalMessage .a-popover-trigger:hover {
        text-decoration: underline !important;
    }
    
    #listPriceLegalMessage .a-icon-popover {
        display: inline-block !important;
        margin-left: 0px !important;
        margin-top: 6px !important;
    }
</style>                           </span>
        </td>
    </tr>
    <tr>
        <td class="a-color-secondary a-size-base a-text-right a-nowrap">Price:</td>
        <td class="a-span12"><span class="a-price a-text-price a-size-medium apexPriceToPay" data-a-size="b"
                                   data-a-color="price"><span class="a-offscreen">₹379.00</span><span
                aria-hidden="true">₹379.00</span></span> <span class="a-size-small a-color-price">(<span
                class="a-price a-text-price a-size-small" data-a-size="b" data-a-color="price"><span
                class="a-offscreen">₹37.90</span><span aria-hidden="true">₹37.90</span></span> /100 g)</span> <span
                class="">
                          <span id="jewelryPriceBreakup_feature_div" class="celwidget"
                                data-feature-name="jewelryPriceBreakup" data-csa-c-id="a8pfts-uta579-px3d1w-1lubki"
                                data-cel-widget="jewelryPriceBreakup_feature_div">
                                           </span>
              <span id="agsIfdInsidePrice_feature_div" class="celwidget" data-feature-name="agsIfdInsidePrice"
                    data-csa-c-id="zkn7y-7u2ofo-g73yra-cq8xka" data-cel-widget="agsIfdInsidePrice_feature_div">
                    <!-- For LightningDeal use case, agsShippingAndIfdInsideBuyBox is only configured on regular offer, so set defaultPageContext as buyingPrice -->
                         </span>
              <span id="regulatoryDeposit_feature_div" class="celwidget" data-feature-name="regulatoryDeposit"
                    data-csa-c-id="g3k6sa-mffw4z-s8flcz-ewalmp" data-cel-widget="regulatoryDeposit_feature_div">
                                   </span>
              <span id="deliveryPriceBadging_feature_div" class="celwidget" data-feature-name="deliveryPriceBadging"
                    data-csa-c-id="ltpnsz-t3mwnt-iiiz7v-l2dmtf" data-cel-widget="deliveryPriceBadging_feature_div">
                                  </span>
              <span id="freeShippingPriceBadging_feature_div" class="celwidget"
                    data-feature-name="freeShippingPriceBadging" data-csa-c-id="6fd8zm-x22lp5-su1gj3-15hlg6"
                    data-cel-widget="freeShippingPriceBadging_feature_div">
            <span class="a-size-base"><i class="a-icon-wrapper a-icon-fba-with-text"><i class="a-icon a-icon-fba"
                                                                                        role="img"
                                                                                        aria-label="Fulfilled"></i><span
                    class="a-icon-text-fba">Fulfilled</span></i></span>                       </span>
              <span id="freeReturns_feature_div" class="celwidget" data-feature-name="freeReturns"
                    data-csa-c-id="vmokyr-r09zxk-gb7v4m-cnknx1" data-cel-widget="freeReturns_feature_div">
                                 </span>
       </span>
        </td>
    </tr>
    <tr>
        <td class="a-color-secondary a-size-base a-text-right a-nowrap"> You Save:</td>
        <td class="a-span12 a-color-price a-size-base"><span class="a-color-price"> <span
                class="a-price a-text-price a-size-base" data-a-size="b" data-a-color="price"><span class="a-offscreen">₹21.00</span><span
                aria-hidden="true">₹21.00</span></span> (5%)</span> <span id="bundleLTBSSavings_feature_div"
                                                                          class="celwidget"
                                                                          data-feature-name="bundleLTBSSavings"
                                                                          data-csa-c-id="ikn99n-2n7sj6-ni22pt-dpuf53"
                                                                          data-cel-widget="bundleLTBSSavings_feature_div">
                                 </span>
            <span id="volumeAwarePricingTableLoader_feature_div" class="celwidget"
                  data-feature-name="volumeAwarePricingTableLoader" data-csa-c-id="cf44ml-ns5lld-w2j6jv-edw3sb"
                  data-cel-widget="volumeAwarePricingTableLoader_feature_div">
                                        </span>
        </td>
    </tr>
    <tr id="vatMessage">
        <td></td>
        <td><span class="a-size-base"> Inclusive of all taxes</span></td>
    </tr>
    </tbody>
</table>
```