
import numpy as np

def euclid(a,b):
    '''A simple egcd returns u,v, d where ux+bv=d'''
    u0,v0=1,0
    u,v = 0,1
    while b!=0:
        q = a//b
        a,b = b, a-q*b
        u,u0 = u0-q*u, u
        v, v0 = v0 -q*v, v
    return u0,v0,a

def rowOp(A,i,j,k):
    '''invertible row operation eliminating putting d in A[k,k]'''
    u,v,d = euclid(A[i,k],A[j,k])
    newAi = u*A[i,:]+v*A[j,:]
    newAj = A[i,k]/d*A[j,:]-A[j,k]/d*A[i,:]
    B=A.copy()
    if newAi[k]!=0:
        B[i,:]=newAi
        B[j,:]=newAj
    else:
        B[i,:]=newAj
        B[j,:]=newAi
    return B

def colOp(A,i,j,k):
    '''invertible column operation'''
    u,v,d = euclid(A[k,i],A[k,j])
    newAi = u*A[:,i]+v*A[:,j]
    newAj = A[k,i]/d*A[:,j]-A[k,j]/d*A[:,i]
    B=A.copy()
    if newAi[k]!=0:
        B[:,i]=newAi
        B[:,j]=newAj
    else:
        B[:,i]=newAj
        B[:,j]=newAi
    return B




def snf(A):
    '''compute smith normal form on small matrices'''
    rows, cols = A.shape
    if rows != cols:
        return "Expecting Square Matrix"
    B=A.copy()
    t=0
    while t<rows:
        if B[t,t]==0:
            r,c = np.nonzero(B[t:,t:])
            if len(r)==0:
                return B
            else:
                newFirstRow=B[(r[0]+t),:].copy()
                B[r[0]+t,:]=B[t,:]
                B[t,:]=newFirstRow
                newFirstCol=B[:,(t+c[0])].copy()
                B[:,t+c[0]]=B[:,t]
                B[:,t]=newFirstCol
        while B[t,(t+1):].any() or B[(t+1):,t].any():
            if np.mod(B[t,(t+1):],B[t,t]).any():
                for i in range(t+1,cols):
                    B = colOp(B,t,i,t)
            else:
                for i in range(t+1,cols):
                    B[:,i]=B[:,i]-B[t,i]/B[t,t]*B[:,t]
            if np.mod(B[(t+1):,t],B[t,t]).any():    
                for i in range(t+1,rows):
                    B = rowOp(B,t,i,t)
            else:
                for i in range(t+1,rows):
                    B[i,:] = B[i,:]-B[i,t]/B[t,t]*B[t,:]
        r,c = np.nonzero(np.mod(B[(t+1):,(t+1):],B[t,t]))
        if len(r)==0:
            t=t+1
            continue
        B[t,:] = B[t,:]+B[t+1+r[0],:]
    return B
    
