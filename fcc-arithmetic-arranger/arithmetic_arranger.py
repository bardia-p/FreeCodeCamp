def arithmetic_arranger(problems,solve=False):
    if len(problems)>5:
      return "Error: Too many problems."
    first=""
    second=""
    third=""
    fourth=""
    for i in problems:
      l=i.split()
      if len(l[0])>4 or len(l[2])>4:
        return "Error: Numbers cannot be more than four digits."
      if l[1]!="+" and l[1]!="-":
        return "Error: Operator must be '+' or '-'."
      try:
        n1=int(l[0])
        n2=int(l[2])
        if solve:
          if l[1]=="+":
            res=str(n1+n2)
          else:
            res=str(n1-n2)
        else:
          res=""
      except:
        return "Error: Numbers must only contain digits."

      n=max(len(l[0]),len(l[2]))
      first+=" "*(n+2-len(l[0]))+l[0]+"    "
      second+=l[1]+" "+" "*(n-len(l[2]))+l[2]+"    "
      third+=(n+2)*"-"+"    "
      if solve:
        fourth+=" "*(n+2-len(res))+res+"    "
    
    arranged_problems=first.rstrip()+"\n"+second.rstrip()+"\n"+third.rstrip()
    if solve:
      arranged_problems+="\n"+fourth.rstrip()
    return arranged_problems