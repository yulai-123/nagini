from urllib.parse import quote

def generate_okx_deeplink(address: str) -> str:    
    # 构建基础深度链接
    deep_link = f"okx://wallet/dex/swap?fromChainId=501&fromTokenContractAddress=&toChainId=501&toTokenContractAddress={address}&isFromNative=1&isToNative=0&amount=0.1"
    
    # 对完整深度链接进行二次编码
    encoded_deep_link = quote(deep_link, safe='')
    
    # 生成最终可跳转链接
    final_url = f"https://www.okx.com/download?deeplink={encoded_deep_link}"
    
    return final_url

if __name__ == "__main__":
    address = "CvUo8ZZ5ZfcBNR7V7GKy2A3Sz1bSfZWrfojWxDmjiBox"
    print(generate_okx_deeplink(address))