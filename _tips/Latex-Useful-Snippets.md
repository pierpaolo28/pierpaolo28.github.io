---
layout: post
date: 2020-06-11
---

# Latex Useful Snippets

## Set-Up

```
\documentclass[12pt]{article}
\usepackage{arxiv}
\usepackage{subfig}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{hyperref}    
\usepackage{url}     
\usepackage{booktabs}     
\usepackage{amsfonts}
\usepackage{nicefrac}  
\usepackage{microtype}
\usepackage{lipsum}
\usepackage[title]{appendix}
\usepackage{graphicx}
\usepackage{graphics}
\usepackage{multirow}
\usepackage{epigraph}
\usepackage{xparse}
\usepackage{amsmath}
\usepackage{svg}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{listings,multicol}
\usepackage{xcolor}
\usepackage{algorithm,algorithmic}
\usepackage{cite}
\hypersetup{urlcolor=black}

\definecolor{airforceblue}{rgb}{0.36, 0.54, 0.66}
\hypersetup{
  colorlinks=true,
  citecolor=black,
  urlcolor= airforceblue
}

\newenvironment{conditions}
  {\par\vspace{\abovedisplayskip}\noindent\begin{tabular}{>{$}l<{$} @{${}={}$} l}}
  {\end{tabular}\par\vspace{\belowdisplayskip}}

\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2
}

\lstset{style=mystyle}

\let\oldquote\quote
\let\endoldquote\endquote

\RenewDocumentEnvironment{quote}{om}
  {\oldquote}
  {\par\nobreak\smallskip
   \hfill(#2\IfValueT{#1}{~---~#1})\endoldquote
   \addvspace{\bigskipamount}}
```

## Equations with conditions

In order to reference the equation, then just use `\ref{example}` when writing in the body of the document.

```
\vspace{-0.2cm}
\begin{align}
\ \hat v(s, w) = \sum_{i=1}^{d}w_{i}x_{i}(s) \label{example}
\end{align}
\vspace{-0.4cm}
where:
\begin{conditions}
 $w_{i}$  &  Weight vector \\
 $x_{i}$  &  Feature representation via RBF\\
\end{conditions}
\vspace{-0.2cm}
```

## Multiple Equations

```
\vspace{-0.2cm}
\begin{align}
\ d_{1} = \dfrac{ln(\dfrac{80}{90}) + (0.17 + \dfrac{0.2^{2}}{2})(2)}{0.2\sqrt{2}} = 0.927
\ d_{2} = d_{1} - 0.2\sqrt{2} = 0.6442
\\  C(S,t) = 80\mathcal{N}(0.927) - 90e^{(-0.17(2))}\mathcal{N}(0.6442) = \$18.42
\label{eq:3}
\vspace{-0.3cm}
\end{align}
```

## PNG Image

```
\vspace{-0.3cm}
\begin{figure}[ht!]%
    \centering
    \includegraphics[width=6.5cm]{images/best_j.png}%
    \vspace{-0.2cm}
    \caption{Number of Basis Functions vs Residual Error}%
    \vspace{-0.3cm}
\end{figure}
```

### Images in row

```
\begin{figure}[ht!]%
    \centering
    \hspace{-0.6cm}
    \subfloat[Tabular Method]{\includegraphics[width=5cm]{images/q_table.png}}%
    \label{fig:example2}%
    \subfloat[Tabular RBF Approximation]{\includegraphics[width=5cm]{images/rbf.png}}%
    \label{fig:example3}%
    \subfloat[Q Learning RBF Approximation]{\includegraphics[width=5cm]{images/q_rbf.png}}%
    \vspace{-0.2cm}
    \caption{Cost-to-go function}%
    \label{fig:example4}%
    \vspace{-0.25cm}
\end{figure}
```

## SVG Images

```
\vspace{-0.3cm}
\begin{figure}[ht!]%
    \centering
    \includesvg[width=15.5cm]{images/ARprocess.svg}%
    \vspace{-0.4cm}
    \caption{Autoregressive Process with slowly changing parameters}%
    \vspace{-0.3cm}
\end{figure}
```

## Tables

### Standard

```
{
\begin{table}[h!]
\centering
\begin{tabular}{|c|c|c|c|}
\hline
Specifics & Stock 1 & Stock 2 \\
\hline
Weight & 70\% & 30\% \\
Expected Return & 15\% & 18\% \\
Standard Deviation & 20\% & 17\% \\
\hline
\end{tabular}
\caption{Stocks Parameters}
\label{five}
\end{table}
}
```

### Multirow, multicolumns

```
\vspace{-0.3cm}
{
\begin{table}[h!]
\centering
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\multirow{2}{*}{Coefficient} & \multicolumn{5}{c|}{Percentage Error (\%)} \\\cline{2-6}
& First Estimate & Second Estimate & Third Estimate & Fourth Estimate & Fifth Estimate \\
\hline
First Coefficient (1.4) & 4.683 & 4.687 & 4.690 & 4.689 & 4.689 &
Second Coefficient (-0.7) & 2.175 & 2.182 & 2.187 & 2.187 & 2.186 &
\hline
\end{tabular}
\caption{Linear Kalman filter estimated percentage errors}
\label{table:1}
\vspace{-0.8cm}
\end{table}
}
```

## Listings

### Standard

```
\begin{lstlisting}[language=Python, caption=Helper functions]
def two_assets_variance(w, std, corr):
    return (w[0]**2)*(std[0]**2)+(w[1]**2)*(std[1]**2)+2*w[0]*w[1]*std[0]*std[1]*corr

def var_to_std(var):
    return np.sqrt(var)

def portfolio_return(weight, ret):
    port_ret = 0
    for i in range(len(weight)):
        port_ret += weight[i]*ret[i]
    return port_ret
\end{lstlisting}
```

### Multicolumn

```
\vspace{-0.3cm}
\begin{figure}[ht!]%
    \centering
\begin{lstlisting}[numbers=left,xleftmargin=0.5em, multicols=2]
Input: X, Y, N, beta
th_n1_n1 = np.random.randn(len(X[0]),1)
P_n1_n1 = 0.001 * np.eye(len(X[0]))
R = 0.2 * np.std(X[0:10])
Q = beta * np.eye(len(X[0]))
for n in range(0, N):
   x = X[n].reshape(len(X[n]), 1)
   th_n_n1 = th_n1_n1.copy()
   P_n_n1 = P_n1_n1 + Q
   yh = sigmoid(th_n_n1.T @ x)
   en = Y[n] - yh
   f = sigmoid_derivative(yh) * x
   den = f.T @ P_n1_n1 @ f + R
   kn = (P_n1_n1 @ f) / den
   th_n_n = th_n_n1 + kn * en
   I_mat = np.eye(len(X[0]))
   P_n_n = (I_mat - kn @ f.T) @ P_n_n1
   th_n1_n1 = th_n_n.copy()
   P_n1_n1 = P_n_n.copy()
return th_n_n\end{lstlisting}
    \caption{Extended Kalman Filter Pseudocode}
    \vspace{-0.3cm}
\end{figure}
```

### Algorithm

```
\begin{algorithm}
\caption{Calculate $y = x^n$}
\label{alg1}
\vspace*{-.5cm}
\begin{multicols}{2}
\begin{algorithmic}[1]
  \REQUIRE $n \geq 0 \vee x \neq 0$
  \ENSURE $y = x^n$
  \STATE $y \Leftarrow 1$
  \IF{$n < 0$}
  \STATE $X \Leftarrow 1 / x$
  \STATE $N \Leftarrow -n$
  \ELSE
  \STATE $X \Leftarrow x$
  \STATE $N \Leftarrow n$
  \ENDIF
  \WHILE{$N \neq 0$}
  \IF{$N$ is even}
  \STATE $X \Leftarrow X \times X$
  \STATE $N \Leftarrow N / 2$
  \ELSE[$N$ is odd]
  \STATE $y \Leftarrow y \times X$
  \STATE $N \Leftarrow N - 1$
  \ENDIF
  \ENDWHILE
\end{algorithmic}
\end{multicols}
\vspace*{-.4cm}
\end{algorithm}
```

## Bibliography

```
\bibliographystyle{unsrt}  
\begin{thebibliography}{1}
\vspace{-0.2cm}
\bibitem{one}
Arulampalam, MS, Maskell, S, Gordon, N &Tim Clapp, T.
\newblock A Tutorial on Particle Filters for Online Nonlinear/Non-Gaussian
Bayesian Tracking, IEEE Trans. Signal Processing 50(2), 174-188, 2002.

\bibitem{data}
Rain in Australia, Joe Young.
\newblock Kaggle.
\newblock Accessed at: {\em
\href{https://www.kaggle.com/jsphyg/weather-dataset-rattle-package}
{https://www.kaggle.com/jsphyg/weather-dataset-rattle-package}},
March 2020.

\end{thebibliography}
```
