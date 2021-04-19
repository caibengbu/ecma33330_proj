#!/usr/bin/env wolframscript
(* ::Package:: *)

temp=DSolve[{Derivative[1][xue][\[Tau]]==(1-xue[\[Tau]]-xui[\[Tau]]) \[Lambda]ue+xui[\[Tau]] \[Lambda]ie-xue[\[Tau]] (\[Lambda]eu+\[Lambda]ei),Derivative[1][xui][\[Tau]]==(1-xue[\[Tau]]-xui[\[Tau]]) \[Lambda]ui+xue[\[Tau]] \[Lambda]ei-xui[\[Tau]] (\[Lambda]iu+\[Lambda]ie)},{xue,xui},\[Tau]][[1]];
solu={Xue==xue[1],Xui==xui[1]}/. temp/.Solve[Evaluate[Limit[{xue[\[Tau]],xui[\[Tau]]}/. temp,\[Tau]->0]=={0,0}],{C[1],C[2]}][[1]];
temp=DSolve[{Derivative[1][xie][\[Tau]]==(1-xiu[\[Tau]]-xie[\[Tau]]) \[Lambda]ie+xiu[\[Tau]] \[Lambda]ue-xie[\[Tau]] (\[Lambda]eu+\[Lambda]ei),Derivative[1][xiu][\[Tau]]==(1-xiu[\[Tau]]-xie[\[Tau]]) \[Lambda]iu+xie[\[Tau]] \[Lambda]eu-xiu[\[Tau]] (\[Lambda]ui+\[Lambda]ue)},{xie,xiu},\[Tau]][[1]];
soli={Xie==xie[1],Xiu==xiu[1]}/. temp/. Solve[Evaluate[Limit[{xie[\[Tau]],xiu[\[Tau]]}/. temp,\[Tau]->0]=={0,0}],{C[1],C[2]}][[1]];
temp=DSolve[{xei'[\[Tau]]==(1-xei[\[Tau]]-xeu[\[Tau]])\[Lambda]ei+xeu[\[Tau]]\[Lambda]ui-xei[\[Tau]](\[Lambda]iu+\[Lambda]ie),xeu'[\[Tau]]==(1-xei[\[Tau]]-xeu[\[Tau]])\[Lambda]eu+xei[\[Tau]]\[Lambda]iu-xeu[\[Tau]](\[Lambda]ui+\[Lambda]ue)},{xei,xeu},\[Tau]][[1]];
sole={Xei==xei[1],Xeu==xeu[1]}/. temp/.Solve[Evaluate[Limit[{xei[\[Tau]],xeu[\[Tau]]}/. temp,\[Tau]->0]=={0,0}],{C[1],C[2]}][[1]];

sol=Simplify[Flatten[{solu,soli,sole}]];

X=Transpose[{Import["../input/ei.txt","List"],Import["../input/eu.txt","List"],Import["../input/ie.txt","List"],Import["../input/iu.txt","List"],Import["../input/ue.txt","List"],Import["../input/ui.txt","List"]}]
t=1;
\[CapitalLambda]={};
While[t<=Length[X],
{Xei,Xeu,Xie,Xiu,Xue,Xui}=X[[t]];
If[Xei!=0,
\[CapitalLambda]=Append[\[CapitalLambda],{\[Lambda]ei,\[Lambda]eu,\[Lambda]ie,\[Lambda]iu,\[Lambda]ue,\[Lambda]ui}/.FindRoot[sol,{\[Lambda]ei,Xei},{\[Lambda]eu,Xeu},{\[Lambda]ie,Xie},{\[Lambda]iu,Xiu},{\[Lambda]ue,Xue},{\[Lambda]ui,Xui}]],
\[CapitalLambda]=Append[\[CapitalLambda],{0,0,0,0,0,0}]];t+=1];

\[Lambda]eiM=Transpose[\[CapitalLambda]][[1]];
\[Lambda]euM=Transpose[\[CapitalLambda]][[2]];
\[Lambda]ieM=Transpose[\[CapitalLambda]][[3]];
\[Lambda]iuM=Transpose[\[CapitalLambda]][[4]];
\[Lambda]ueM=Transpose[\[CapitalLambda]][[5]];
\[Lambda]uiM=Transpose[\[CapitalLambda]][[6]];

FillwithMA[x_]:=
Module[{MatchFail,len,Neighborhood,NumOfValidDataInNeighborhood,MeanNeighborhood,result,temp},
MatchFail=Flatten[Position[x,0]];
len = Length[MatchFail];
temp=x;
For[i=1,i<=len,i++,
Neighborhood={MatchFail[[i]]-1,MatchFail[[i]]+1};
NumOfValidDataInNeighborhood=Total[1-Boole[MemberQ[MatchFail,#]&/@Neighborhood]];
MeanNeighborhood=Total[x[[MatchFail[[i]]-1;;MatchFail[[i]]+1]]]/NumOfValidDataInNeighborhood;
temp=ReplacePart[temp,MatchFail[[i]]->MeanNeighborhood]];
Return[temp]
];
\[Lambda]eiM=FillwithMA[\[Lambda]eiM];
\[Lambda]euM=FillwithMA[\[Lambda]euM];
\[Lambda]ieM=FillwithMA[\[Lambda]ieM];
\[Lambda]iuM=FillwithMA[\[Lambda]iuM];
\[Lambda]ueM=FillwithMA[\[Lambda]ueM];
\[Lambda]uiM=FillwithMA[\[Lambda]uiM];
Export["../output/ei_M.dat",\[Lambda]eiM];
Export["../output/eu_M.dat",\[Lambda]euM];
Export["../output/ie_M.dat",\[Lambda]ieM];
Export["../output/iu_M.dat",\[Lambda]iuM];
Export["../output/ue_M.dat",\[Lambda]ueM];
Export["../output/ui_M.dat",\[Lambda]uiM];
