#!/usr/bin/env wolframscript
(* ::Package:: *)

dateQ[x_]:=Transpose[{Table[1994.25+(i-1)/4.,{i,1,Length[x]}],x}];

temp=DSolve[{Derivative[1][xue][\[Tau]]==(1-xue[\[Tau]]-xui[\[Tau]]) \[Lambda]ue+xui[\[Tau]] \[Lambda]ie-xue[\[Tau]] (\[Lambda]eu+\[Lambda]ei),Derivative[1][xui][\[Tau]]==(1-xue[\[Tau]]-xui[\[Tau]]) \[Lambda]ui+xue[\[Tau]] \[Lambda]ei-xui[\[Tau]] (\[Lambda]iu+\[Lambda]ie)},{xue,xui},\[Tau]][[1]];
solu={Xue==xue[1],Xui==xui[1]}/. temp/.Solve[Evaluate[Limit[{xue[\[Tau]],xui[\[Tau]]}/. temp,\[Tau]->0]=={0,0}],{C[1],C[2]}][[1]];
temp=DSolve[{Derivative[1][xie][\[Tau]]==(1-xiu[\[Tau]]-xie[\[Tau]]) \[Lambda]ie+xiu[\[Tau]] \[Lambda]ue-xie[\[Tau]] (\[Lambda]eu+\[Lambda]ei),Derivative[1][xiu][\[Tau]]==(1-xiu[\[Tau]]-xie[\[Tau]]) \[Lambda]iu+xie[\[Tau]] \[Lambda]eu-xiu[\[Tau]] (\[Lambda]ui+\[Lambda]ue)},{xie,xiu},\[Tau]][[1]];
soli={Xie==xie[1],Xiu==xiu[1]}/. temp/. Solve[Evaluate[Limit[{xie[\[Tau]],xiu[\[Tau]]}/. temp,\[Tau]->0]=={0,0}],{C[1],C[2]}][[1]];
temp=DSolve[{xei'[\[Tau]]==(1-xei[\[Tau]]-xeu[\[Tau]])\[Lambda]ei+xeu[\[Tau]]\[Lambda]ui-xei[\[Tau]](\[Lambda]iu+\[Lambda]ie),xeu'[\[Tau]]==(1-xei[\[Tau]]-xeu[\[Tau]])\[Lambda]eu+xei[\[Tau]]\[Lambda]iu-xeu[\[Tau]](\[Lambda]ui+\[Lambda]ue)},{xei,xeu},\[Tau]][[1]];
sole={Xei==xei[1],Xeu==xeu[1]}/. temp/.Solve[Evaluate[Limit[{xei[\[Tau]],xeu[\[Tau]]}/. temp,\[Tau]->0]=={0,0}],{C[1],C[2]}][[1]];

sol=Simplify[Flatten[{solu,soli,sole}]];
X=Transpose[{Import["ei.txt","List"],Import["eu.txt","List"],Import["ie.txt","List"],Import["iu.txt","List"],Import["ue.txt","List"],Import["ui.txt","List"]}]

t=1;
\[CapitalLambda]={};
While[t<=Length[X],
	{Xei,Xeu,Xie,Xiu,Xue,Xui}=X[[t]];
	If[Xei!=0,
		\[CapitalLambda]=Append[\[CapitalLambda],{\[Lambda]ei,\[Lambda]eu,\[Lambda]ie,\[Lambda]iu,\[Lambda]ue,\[Lambda]ui}/.FindRoot[sol,{\[Lambda]ei,Xei},{\[Lambda]eu,Xeu},{\[Lambda]ie,Xie},{\[Lambda]iu,Xiu},{\[Lambda]ue,Xue},{\[Lambda]ui,Xui}]],
		\[CapitalLambda]=Append[\[CapitalLambda],{0,0,0,0,0,0}]];
	t+=1];

\[CapitalLambda]1=Drop[\[CapitalLambda],1];
\[CapitalLambda]1=Prepend[Prepend[\[CapitalLambda],{0,0,0,0,0,0}],{0,0,0,0,0,0}];
temp=Mean/@DeleteCases[Partition[Transpose[\[CapitalLambda]1][[1]],3],0,2];
\[Lambda]eiQ=Flatten[ReplacePart[temp,(temp[[Position[temp,Mean[{}]][[1]]-1]]+temp[[Position[temp,Mean[{}]][[1]]+1]])/2,Position[temp,Mean[{}]]]];
temp=Mean/@DeleteCases[Partition[Transpose[\[CapitalLambda]1][[2]],3],0,2];
\[Lambda]euQ=Flatten[ReplacePart[temp,(temp[[Position[temp,Mean[{}]][[1]]-1]]+temp[[Position[temp,Mean[{}]][[1]]+1]])/2,Position[temp,Mean[{}]]]];
temp=Mean/@DeleteCases[Partition[Transpose[\[CapitalLambda]1][[3]],3],0,2];
\[Lambda]ieQ=Flatten[ReplacePart[temp,(temp[[Position[temp,Mean[{}]][[1]]-1]]+temp[[Position[temp,Mean[{}]][[1]]+1]])/2,Position[temp,Mean[{}]]]];
temp=Mean/@DeleteCases[Partition[Transpose[\[CapitalLambda]1][[4]],3],0,2];
\[Lambda]iuQ=Flatten[ReplacePart[temp,(temp[[Position[temp,Mean[{}]][[1]]-1]]+temp[[Position[temp,Mean[{}]][[1]]+1]])/2,Position[temp,Mean[{}]]]];
temp=Mean/@DeleteCases[Partition[Transpose[\[CapitalLambda]1][[5]],3],0,2];
\[Lambda]ueQ=Flatten[ReplacePart[temp,(temp[[Position[temp,Mean[{}]][[1]]-1]]+temp[[Position[temp,Mean[{}]][[1]]+1]])/2,Position[temp,Mean[{}]]]];
temp=Mean/@DeleteCases[Partition[Transpose[\[CapitalLambda]1][[6]],3],0,2];
\[Lambda]uiQ=Flatten[ReplacePart[temp,(temp[[Position[temp,Mean[{}]][[1]]-1]]+temp[[Position[temp,Mean[{}]][[1]]+1]])/2,Position[temp,Mean[{}]]]];

Export["ei.dat",dateQ[\[Lambda]eiQ]];
Export["eu.dat",dateQ[\[Lambda]euQ]];
Export["ie.dat",dateQ[\[Lambda]ieQ]];
Export["iu.dat",dateQ[\[Lambda]iuQ]];
Export["ue.dat",dateQ[\[Lambda]ueQ]];
Export["ui.dat",dateQ[\[Lambda]uiQ]];

sse = \[Lambda]iuQ \[Lambda]ueQ+\[Lambda]uiQ \[Lambda]ieQ+\[Lambda]ueQ \[Lambda]ieQ;
ssu = \[Lambda]eiQ \[Lambda]iuQ+\[Lambda]ieQ \[Lambda]euQ+\[Lambda]iuQ \[Lambda]euQ;
ssi = \[Lambda]euQ \[Lambda]uiQ+\[Lambda]ueQ \[Lambda]eiQ+\[Lambda]uiQ \[Lambda]eiQ;
ssurate=ssu/(ssu+sse);sserate=sse/(ssi+ssu+sse);

sse = \[Lambda]iuQ Mean[\[Lambda]ueQ]+Mean[\[Lambda]uiQ]Mean[\[Lambda]ieQ]+Mean[\[Lambda]ueQ] Mean[\[Lambda]ieQ];
ssu = Mean[\[Lambda]eiQ] \[Lambda]iuQ+Mean[\[Lambda]ieQ]Mean[\[Lambda]euQ]+\[Lambda]iuQ Mean[\[Lambda]euQ];
ssi = Mean[\[Lambda]euQ] Mean[\[Lambda]uiQ]+Mean[\[Lambda]ueQ] Mean[\[Lambda]eiQ]+Mean[\[Lambda]uiQ] Mean[\[Lambda]eiQ];
ssurateiu=ssu/(ssu+sse);sserateiu=sse/(ssi+ssu+sse);

sse = Mean[\[Lambda]iuQ] Mean[\[Lambda]ueQ]+Mean[\[Lambda]uiQ]\[Lambda]ieQ+Mean[\[Lambda]ueQ] \[Lambda]ieQ;
ssu = Mean[\[Lambda]eiQ] Mean[\[Lambda]iuQ]+\[Lambda]ieQ Mean[\[Lambda]euQ]+Mean[\[Lambda]iuQ] Mean[\[Lambda]euQ];
ssi = Mean[\[Lambda]euQ] Mean[\[Lambda]uiQ]+Mean[\[Lambda]ueQ] Mean[\[Lambda]eiQ]+Mean[\[Lambda]uiQ] Mean[\[Lambda]eiQ];
ssurateie=ssu/(ssu+sse);sserateie=sse/(ssi+ssu+sse);

sse = Mean[\[Lambda]iuQ] Mean[\[Lambda]ueQ]+Mean[\[Lambda]uiQ]Mean[\[Lambda]ieQ]+Mean[\[Lambda]ueQ] Mean[\[Lambda]ieQ];
ssu = \[Lambda]eiQ Mean[\[Lambda]iuQ]+Mean[\[Lambda]ieQ]Mean[\[Lambda]euQ]+Mean[\[Lambda]iuQ] Mean[\[Lambda]euQ];
ssi = Mean[\[Lambda]euQ] Mean[\[Lambda]uiQ]+Mean[\[Lambda]ueQ] \[Lambda]eiQ+Mean[\[Lambda]uiQ] \[Lambda]eiQ;
ssurateei=ssu/(ssu+sse);sserateei=sse/(ssi+ssu+sse);

sse = Mean[\[Lambda]iuQ] Mean[\[Lambda]ueQ]+Mean[\[Lambda]uiQ]Mean[\[Lambda]ieQ]+Mean[\[Lambda]ueQ] Mean[\[Lambda]ieQ];
ssu = Mean[\[Lambda]eiQ] Mean[\[Lambda]iuQ]+Mean[\[Lambda]ieQ]\[Lambda]euQ+Mean[\[Lambda]iuQ] \[Lambda]euQ;
ssi = \[Lambda]euQ Mean[\[Lambda]uiQ]+Mean[\[Lambda]ueQ] Mean[\[Lambda]eiQ]+Mean[\[Lambda]uiQ] Mean[\[Lambda]eiQ];
ssurateeu=ssu/(ssu+sse);sserateeu=sse/(ssi+ssu+sse);

sse = Mean[\[Lambda]iuQ] \[Lambda]ueQ+Mean[\[Lambda]uiQ]Mean[\[Lambda]ieQ]+\[Lambda]ueQ Mean[\[Lambda]ieQ];
ssu = Mean[\[Lambda]eiQ] Mean[\[Lambda]iuQ]+Mean[\[Lambda]ieQ]Mean[\[Lambda]euQ]+Mean[\[Lambda]iuQ] Mean[\[Lambda]euQ];
ssi = Mean[\[Lambda]euQ] Mean[\[Lambda]uiQ]+\[Lambda]ueQ Mean[\[Lambda]eiQ]+Mean[\[Lambda]uiQ] Mean[\[Lambda]eiQ];
ssurateue=ssu/(ssu+sse);sserateue=sse/(ssi+ssu+sse);

sse = Mean[\[Lambda]iuQ] Mean[\[Lambda]ueQ]+\[Lambda]uiQ Mean[\[Lambda]ieQ]+Mean[\[Lambda]ueQ] Mean[\[Lambda]ieQ];
ssu = Mean[\[Lambda]eiQ] Mean[\[Lambda]iuQ]+Mean[\[Lambda]ieQ]Mean[\[Lambda]euQ]+Mean[\[Lambda]iuQ] Mean[\[Lambda]euQ];
ssi = Mean[\[Lambda]euQ] \[Lambda]uiQ+Mean[\[Lambda]ueQ] Mean[\[Lambda]eiQ]+\[Lambda]uiQ Mean[\[Lambda]eiQ];
ssurateui=ssu/(ssu+sse);sserateui=sse/(ssi+ssu+sse);


Export["urate.dat",dateQ[ssurate]];
Export["urate_ei.dat",dateQ[ssurateei]];
Export["urate_eu.dat",dateQ[ssurateeu]];
Export["urate_ie.dat",dateQ[ssurateie]];
Export["urate_iu.dat",dateQ[ssurateiu]];
Export["urate_ue.dat",dateQ[ssurateue]];
Export["urate_ui.dat",dateQ[ssurateui]];

Export["erate.dat",dateQ[sserate]];
Export["erate_ei.dat",dateQ[sserateei]];
Export["erate_eu.dat",dateQ[sserateeu]];
Export["erate_ie.dat",dateQ[sserateie]];
Export["erate_iu.dat",dateQ[sserateiu]];
Export["erate_ue.dat",dateQ[sserateue]];
Export["erate_ui.dat",dateQ[sserateui]];
