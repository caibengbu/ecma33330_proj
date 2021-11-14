import numpy as np
from .other_utils import get_output_filename

def three_state(df_sa,theDir):
    ei = df_sa.ei.values
    eu = df_sa.eu.values
    ie = df_sa.ie.values
    iu = df_sa.iu.values
    ue = df_sa.ue.values
    ui = df_sa.ui.values

    Lambda_list = []
    for t in range(len(ei)):
        if ei[t] == 0.:
            Lambda_list.append(np.array([0.,0.,0.,0.,0.,0.]))
        else:
            discrete = np.matrix([
                [1-ei[t]-eu[t],ie[t],ue[t]],
                [ei[t],1-ie[t]-iu[t],ui[t]],
                [eu[t],iu[t],1-ue[t]-ui[t]]
            ])
            eig_vals,eig_vecs = np.linalg.eig(discrete)
            continous = np.dot(np.dot(np.linalg.inv(np.transpose(eig_vecs)),np.diag(np.log(eig_vals))),np.transpose(eig_vecs))
            lambda_ab = np.array([continous[0,1],continous[0,2],continous[1,0],continous[1,2],continous[2,0],continous[2,1]])
            Lambda_list.append(lambda_ab)

    transitional_rate = np.stack(Lambda_list, axis=0)

    def fill_missing(vec):
        vec_copy = vec.copy()
        n = len(vec_copy)
        for i in range(n):
            if vec_copy[i]==0:
                r = 1
                while True:
                    left = max(0,i-r)
                    right = min(n,i+r+1)
                    selected_val = vec_copy[left:right]
                    num_of_missing = sum(selected_val!=0)
                    if num_of_missing>0:
                        break
                    else:
                        r += 1
                filler = sum(selected_val)/num_of_missing
                vec_copy[i] = filler
        return vec_copy

    lambda_eiM = fill_missing(transitional_rate[:,0])
    lambda_euM = fill_missing(transitional_rate[:,1])
    lambda_ieM = fill_missing(transitional_rate[:,2])
    lambda_iuM = fill_missing(transitional_rate[:,3])
    lambda_ueM = fill_missing(transitional_rate[:,4])
    lambda_uiM = fill_missing(transitional_rate[:,5])

    np.savetxt(get_output_filename(theDir,"eiM_rate.txt"),lambda_eiM)
    np.savetxt(get_output_filename(theDir,"euM_rate.txt"),lambda_euM)
    np.savetxt(get_output_filename(theDir,"ieM_rate.txt"),lambda_ieM)
    np.savetxt(get_output_filename(theDir,"iuM_rate.txt"),lambda_iuM)
    np.savetxt(get_output_filename(theDir,"ueM_rate.txt"),lambda_ueM)
    np.savetxt(get_output_filename(theDir,"uiM_rate.txt"),lambda_uiM)


    """ for item in ["ei","eu","ie","iu",'ue',"ui"]:
        ab_M = np.loadtxt("../output/"+item+"_M.dat")
        lambda_abM = eval("lambda_"+item+"M")
        err = max(abs(ab_M-lambda_abM))
        print(err) """

    # transitional_probability
    np.savetxt(get_output_filename(theDir,"eiM_prob.txt"),1-np.exp(-lambda_eiM))
    np.savetxt(get_output_filename(theDir,"euM_prob.txt"),1-np.exp(-lambda_euM))
    np.savetxt(get_output_filename(theDir,"ieM_prob.txt"),1-np.exp(-lambda_ieM))
    np.savetxt(get_output_filename(theDir,"iuM_prob.txt"),1-np.exp(-lambda_iuM))
    np.savetxt(get_output_filename(theDir,"ueM_prob.txt"),1-np.exp(-lambda_ueM))
    np.savetxt(get_output_filename(theDir,"uiM_prob.txt"),1-np.exp(-lambda_uiM))

        



