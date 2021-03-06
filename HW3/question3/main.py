# python 3
import numpy as np
import matplotlib.pyplot as plt

import load
import jackknife as jackk
import bootstrap as boots
import chi_2 as chi

if __name__ == "__main__":

    '''
    solution for (3a)
    '''
    C = load.loadData('data2.dat')
    mean = C.mean(axis=0).reshape(1,32)

    sum = np.zeros((1,32))
    for line in C:
        sum = sum + (line - mean)**2
    deviation = np.sqrt(sum / (200*199))

    rel_dev = deviation / mean * 100
    # output = open('3a.txt','w')

    # # form format ouput
    # for i in range(32):
    #     line = "|{}".format(i+1) +"|{:.3e}|".format(mean[0][i]) + "{:.2f}|".format(deviation[0][i]) + "{:.2f}%| \n".format(rel_dev[0][i])
    #     output.write(line)
    # output.close()

    # plt.plot(np.arange(0,32),np.abs(rel_dev).reshape(32,),'o-')
    # plt.ylabel("$\Delta C / C \%$",fontsize='x-large')
    # plt.xlabel('$t$',fontsize='x-large')
    # plt.savefig("3a.jpg")
    # plt.show()


    '''
    solution for (3b),(3c),(3d). 
    index 1 for (3b) & (3c) ; index 2 for (3d)
    '''
    # calculation part
    m_eff_time1, m_err_time1 = jackk.get_list('data2.dat',1)
    m_eff_time2, m_err_time2 = jackk.get_list('data2.dat',2)

    list1 = chi.chi_2(1)
    list2 = chi.chi_2(2)

    m_1 = np.array(list1[0])
    m_err_1 = np.array(list1[1])
    m_2 = np.array(list2[0])
    m_err_2 = np.array(list2[1])
    start1 = list1[4]
    end1 = list1[5]
    start2 = list2[4]
    end2 = list2[5]
    m_1_list = m_1.repeat(end1-start1)
    m_err_1_list = m_err_1.repeat(end1-start1)
    m_2_list = m_2.repeat(end2-start2)
    m_err_2_list = m_err_2.repeat(end2-start2)
    print(list1)
    print(list2)

    #plot part
    Ys1 = m_eff_time1[1:]
    errs1 = m_err_time1[1:]

    output1 = open('3b.txt','w')

    for i in range(len(m_eff_time1)):
        line1 = "|{}".format(i) +"|{:.5f}|".format(m_eff_time1[i]) + "{:.5f}| \n".format(m_err_time1[i])
        #print(line)
        output1.write(line1)
    output1.close()

    plt.errorbar(x=np.arange(1,len(Ys1)+1), y=Ys1, yerr=errs1,fmt='o',marker='o',markersize='2',capsize=2)
    plt.plot(np.arange(start1,end1),m_1_list,linewidth=2)
    plt.plot(np.arange(start1,end1),m_1_list+m_err_1_list,linewidth=1,linestyle=':',color='red')
    plt.plot(np.arange(start1,end1),m_1_list-m_err_1_list,linewidth=1,linestyle=':',color='red') 

    plt.ylabel("$m_{eff}$",fontsize='x-large')
    plt.xlabel('$t$',fontsize='x-large')
    plt.savefig("./images_and_data/3b.jpg")
    plt.show()

    Ys2 = m_eff_time2[1:]
    errs2 = m_err_time2[1:]

    output2 = open('3d.txt','w')

    for i in range(len(m_eff_time2)):
        line2 = "|{}".format(i+1) +"|{:.5f}|".format(m_eff_time2[i]) + "{:.5f}| \n".format(m_err_time2[i])
        #print(line)
        output2.write(line2)
    output2.close()

    plt.errorbar(x=np.arange(1,len(Ys2)+1), y=Ys2, yerr=errs2,fmt='o',marker='o',markersize='2',capsize=2)
    plt.plot(np.arange(start2,end2),m_2_list,linewidth=2)
    plt.plot(np.arange(start2,end2),m_2_list+m_err_2_list,linewidth=1,linestyle=':',color='red')
    plt.plot(np.arange(start2,end2),m_2_list-m_err_2_list,linewidth=1,linestyle=':',color='red') 

    plt.ylabel("$m_{eff}$",fontsize='x-large')
    plt.xlabel('$t$',fontsize='x-large')
    plt.savefig("./images_and_data/3d.jpg")
    plt.show()

    # zoomed in image
    Ys1_1 = m_eff_time1[start1:end1]
    errs1_1 = m_err_time1[start1:end1]

    plt.errorbar(x=np.arange(start1,end1), y=Ys1_1, yerr=errs1_1,fmt='o',marker='o',markersize='2',capsize=2)
    plt.plot(np.arange(start1,end1),m_1_list,linewidth=2)
    plt.plot(np.arange(start1,end1),m_1_list+m_err_1_list,linewidth=1,linestyle=':',color='red')
    plt.plot(np.arange(start1,end1),m_1_list-m_err_1_list,linewidth=1,linestyle=':',color='red') 

    plt.ylabel("$m_{eff}$",fontsize='x-large')
    plt.xlabel('$t$',fontsize='x-large')
    plt.savefig("./images_and_data/3b_zoomed_in.jpg")
    plt.show()

    Ys2_1 = m_eff_time2[start2:end2]
    errs2_1 = m_err_time2[start2:end2]

    plt.errorbar(x=np.arange(start2,end2), y=Ys2_1, yerr=errs2_1,fmt='o',marker='o',markersize='2',capsize=2)
    plt.plot(np.arange(start2,end2),m_2_list,linewidth=2)
    plt.plot(np.arange(start2,end2),m_2_list+m_err_2_list,linewidth=1,linestyle=':',color='red')
    plt.plot(np.arange(start2,end2),m_2_list-m_err_2_list,linewidth=1,linestyle=':',color='red') 

    plt.ylabel("$m_{eff}$",fontsize='x-large')
    plt.xlabel('$t$',fontsize='x-large')
    plt.savefig("./images_and_data/3d_zoomed_in.jpg")
    plt.show()
    '''
    solution for (3e)
    '''
    # covs = boots.cov(C)
    # print(boots.rho_helper(covs, 3, 4))
    # print(boots.rho_helper(covs, 3, 5))