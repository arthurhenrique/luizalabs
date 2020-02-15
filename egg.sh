prolado(){
    
    echo "  __                  __                            __                  __                 "
    echo "/  |                /  |                          /  |                /  |                "
    echo "LL |       __    __ LL/  ________   ______        LL |        ______  LL |____    _______ "
    echo "LL |      /  |  /  |/  |/        | /      \       LL |       /      \ LL      \  /       |"
    echo "LL |      LL |  LL |LL |LLLLLLLL/  LLLLLL  |      LL |       LLLLLL  |LLLLLLL  |/LLLLLLL/ "
    echo "LL |      LL |  LL |LL |  /  LL/   /    LL |      LL |       /    LL |LL |  LL |LL      \ "
    echo "LL |_____ LL \__LL |LL | /LLLL/__ /LLLLLLL |      LL |_____ /LLLLLLL |LL |__LL | LLLLLL  |"
    echo "LL       |LL    LL/ LL |/LL      |LL    LL |      LL       |LL    LL |LL    LL/ /     LL/ "
    echo "LLLLLLLL/  LLLLLL/  LL/ LLLLLLLL/  LLLLLLL/       LLLLLLLL/  LLLLLLL/ LLLLLLL/  LLLLLLL/  "
}

prooutro(){
    
    echo " /LL                 /LL                           /LL                 /LL                "
    echo "| LL                |__/                          | LL                | LL                "
    echo "| LL       /LL   /LL /LL /LLLLLLLL  /LLLLLL       | LL        /LLLLLL | LLLLLLL   /LLLLLLL"
    echo "| LL      | LL  | LL| LL|____ /LL/ |____  LL      | LL       |____  LL| LL__  LL /LL_____/"
    echo "| LL      | LL  | LL| LL   /LLLL/   /LLLLLLL      | LL        /LLLLLLL| LL  \ LL|  LLLLLL "
    echo "| LL      | LL  | LL| LL  /LL__/   /LL__  LL      | LL       /LL__  LL| LL  | LL \____  LL"
    echo "| LLLLLLLL|  LLLLLL/| LL /LLLLLLLL|  LLLLLLL      | LLLLLLLL|  LLLLLLL| LLLLLLL/ /LLLLLLL/"
    echo "|________/ \______/ |__/|________/ \_______/      |________/ \_______/|_______/ |_______/ "
    
}

egg="$(python -c 'print("clear ; prolado ; sleep 1 ; clear ; prooutro; sleep 1;" * (0xDEADBEAF - (0xDEADBEAF - 42)))')"
eval $egg